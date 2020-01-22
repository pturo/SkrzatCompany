from flask import Flask, render_template, request, session, logging, url_for, redirect, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from passlib.hash import sha256_crypt

import pymysql

# połączenie do bazy przez admina
login = create_engine("mysql+pymysql://rootadmin:rootadm@localhost/administracjabd")
db = scoped_session(sessionmaker(bind=login))

# bazy, do których będziemy dodawać i usuwać użytkowników
# dodawanie użytkowników
ziemia = create_engine("mysql+pymysql://rootadmin:rootadm@localhost/ziemiabd")
z = scoped_session(sessionmaker(bind=ziemia))
mars = create_engine("mysql+pymysql://rootadmin:rootadm@localhost/marsbd")
m = scoped_session(sessionmaker(bind=mars))
ksiezyc = create_engine("mysql+pymysql://rootadmin:rootadm@localhost/ksiezycbd")
k = scoped_session(sessionmaker(bind=ksiezyc))

# usuwanie użytkowników
zConn = pymysql.connect(host="localhost", user="rootadmin", password="rootadm",
db="ziemiabd", autocommit=True)
mConn = pymysql.connect(host="localhost", user="rootadmin", password="rootadm",
db="marsbd", autocommit=True)
kConn = pymysql.connect(host="localhost", user="rootadmin", password="rootadm",
db="ksiezycbd", autocommit=True)

app = Flask(__name__)

# strona główna
@app.route("/")
def home():
    return render_template("home.html")

# logowanie
@app.route("/login", methods=["GET","POST"])
def admlogin():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        usernamedata = db.execute("SELECT username FROM users WHERE username=:username",{"username":username}).fetchone()
        passwordhash = db.execute("SELECT password FROM users WHERE username=:username",{"username":username}).fetchone()

        if username is None:
            flash("Nieprawidłowa nazwa użytkownika!","danger")
            return render_template("admin/login.html")
        else:
            for phash in passwordhash:
                if sha256_crypt.verify(password,phash):
                    session["log"] = True
                    flash("Jesteś zalogowany.","success")
                    return redirect(url_for('adminpanel'))
                else:
                    flash("Niewłaściwe hasło!","danger")
                    return render_template("admin/login.html")
    return render_template("admin/login.html")

# autoryzacja
# sprawdź, czy użytkownik jest zalogowany, w przeciwnym razie odeślj na stronę logowania
def is_logged_in():
    if "log" in session:
        return redirect(url_for('adminpanel'))
    else:
        flash("Błąd autoryzacji użytkownika! Prosimy się zalogować.","danger")
        return redirect(url_for('login'))

# panel administatora
@app.route("/adminpanel")
def adminpanel():
    query = db.execute("SELECT id, username, password, oddzial FROM ksiezycbd.ksiezyc UNION SELECT id, username, password, oddzial FROM ziemiabd.ziemia UNION SELECT id, username, password, oddzial FROM marsbd.mars")
    return render_template("admin/adminpanel.html", users = query.fetchall())

# dodawanie użytkownika do bazy
@app.route("/add", methods=["GET","POST"])
def add():
    if request.method == "POST":
        usern = request.form.get("username")
        passw = request.form.get("password")
        confi = request.form.get("confirmpassword")
        oddzi = request.form.get("oddzial")
        sec_pass = sha256_crypt.hash(str(passw))

        if passw == confi:
            if oddzi == "Ziemia":
                z.execute("INSERT INTO ziemia(username, password, oddzial) VALUES(:username,:password,:oddzial)",
                {"username":usern,"password":sec_pass,"oddzial":oddzi})
                z.commit()
                flash("Dodano użytkownika do bazy.","success")
                return redirect(url_for('adminpanel'))
            elif oddzi == "Mars":
                m.execute("INSERT INTO mars(username, password, oddzial) VALUES(:username,:password,:oddzial)",
                {"username":usern,"password":sec_pass,"oddzial":oddzi})
                m.commit()
                flash("Dodano użytkownika do bazy.","success")
                return redirect(url_for('adminpanel'))
            elif oddzi == "Księżyc":
                k.execute("INSERT INTO ksiezyc(username, password, oddzial) VALUES(:username,:password,:oddzial)",
                {"username":usern,"password":sec_pass,"oddzial":oddzi})
                k.commit()
                flash("Dodano użytkownika do bazy.","success")
                return redirect(url_for('adminpanel'))
            else:
                flash("Problem z dodawaniem użytkownika do bazy!","danger")
                return render_template("admin/add.html")
        else:
            flash("Hasła nie są takie same!","danger")
    return render_template("admin/add.html")

# usuwanie użytkownika z bazy
@app.route("/delete/<string:id>/<string:oddzial>", methods=["GET", "POST"])
def delete(id, oddzial):
    if request.method == "POST":
        if oddzial == "Ziemia":
            zCur = zConn.cursor()
            zSQL = "DELETE from ziemia WHERE id=%s AND oddzial=%s"
            zCur.execute(zSQL, (id, oddzial))
            zConn.commit()
            zCur.close()
            flash("Usunięto użytkownika z bazy.","success")
            return redirect(url_for('adminpanel'))
        elif oddzial == "Mars":
            mCur = mConn.cursor()
            mSQL = "DELETE from mars WHERE id=%s AND oddzial=%s"
            mCur.execute(mSQL, (id, oddzial))
            mConn.commit()
            mCur.close()
            flash("Usunięto użytkownika z bazy.","success")
            return redirect(url_for('adminpanel'))
        elif oddzial == "Księżyc":
            kCur = kConn.cursor()
            kSQL = "DELETE from ksiezyc WHERE id=%s AND oddzial=%s"
            kCur.execute(kSQL, (id, oddzial))
            kConn.commit()
            mCur.close()
            flash("Usunięto użytkownika z bazy.","success")
            return redirect(url_for('adminpanel'))
        else:
            flash("Problem z usuwaniem użytkownika z bazy!","danger")
            return redirect(url_for('adminpanel'))
    return render_template("admin/adminpanel.html")

# wylogowanie
@app.route("/logout")
def admlogout():
    session.clear()
    flash("Zostałeś wylogowany","success")
    return redirect(url_for('admlogin'))

# weryfikacje użytkowników
@app.route("/ziemia", methods=["GET", "POST"])
def ziemia():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        uuser = z.execute("SELECT username FROM ziemia WHERE username=:username",{"username":username}).fetchone()
        upass = z.execute("SELECT password FROM ziemia WHERE username=:username",{"username":username}).fetchone()

        if username is None:
            flash("Nie podano nazwy użytkownika!","danger")
            return render_template("ziemia/ziemia.html")
        elif password is None:
            flash("Nie podano hasła!","danger")
            return render_template("ziemia/ziemia.html")
        else:
            for u_pass in upass:
                if sha256_crypt.verify(password,u_pass):
                    flash("Jesteś użytkownikiem należącym do tego oddziału. Gratulujemy!","success")
                    return render_template("ziemia/ziemia.html")
                elif sha256_crypt.verify(password,u_pass):
                    flash("Niewłaściwe hasło!","danger")
                    return render_template("admin/login.html")
                else:
                    flash("Przykro nam, ale nie należysz do tego oddziału :(","danger")
                    render_template("ziemia/ziemia.html")
    return render_template("ziemia/ziemia.html")

@app.route("/mars", methods=["GET", "POST"])
def mars():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        uuser = m.execute("SELECT username FROM mars WHERE username=:username",{"username":username}).fetchone()
        upass = m.execute("SELECT password FROM mars WHERE username=:username",{"username":username}).fetchone()

        if username is None:
            flash("Nie podano nazwy użytkownika!","danger")
            return render_template("mars/mars.html")
        elif password is None:
            flash("Nie podano hasła!","danger")
            return render_template("mars/mars.html")
        else:
            for u_pass in upass:
                if sha256_crypt.verify(password,u_pass):
                    flash("Jesteś użytkownikiem należącym do tego oddziału. Gratulujemy!","success")
                    return render_template("mars/mars.html")
                elif sha256_crypt.verify(password,u_pass):
                    flash("Niewłaściwe hasło!","danger")
                    return render_template("mars/mars.html")
                else:
                    flash("Przykro nam, ale nie należysz do tego oddziału :(","danger")
                    render_template("mars/mars.html")
    return render_template("mars/mars.html")

@app.route("/ksiezyc", methods=["GET", "POST"])
def ksiezyc():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        uuser = k.execute("SELECT username FROM ksiezyc WHERE username=:username",{"username":username}).fetchone()
        upass = k.execute("SELECT password FROM ksiezyc WHERE username=:username",{"username":username}).fetchone()

        if username is None:
            flash("Nie podano nazwy użytkownika!","danger")
            return render_template("ksiezyc/ksiezyc.html")
        elif password is None:
            flash("Nie podano hasła!","danger")
            return render_template("ksiezyc/ksiezyc.html")
        else:
            for u_pass in upass:
                if sha256_crypt.verify(password,u_pass):
                    flash("Jesteś użytkownikiem należącym do tego oddziału. Gratulujemy!","success")
                    return render_template("ksiezyc/ksiezyc.html")
                elif sha256_crypt.verify(password,u_pass):
                    flash("Niewłaściwe hasło!","danger")
                    return render_template("admin/login.html")
                else:
                    flash("Przykro nam, ale nie należysz do tego oddziału :(","danger")
                    render_template("ksiezyc/ksiezyc.html")
    return render_template("ksiezyc/ksiezyc.html")

if __name__ == "__main__":
    app.secret_key="skrzatcompany123"
    app.run(debug=True)