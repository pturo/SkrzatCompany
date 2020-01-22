# SkrzatCompany
Python + Flask microframework excersise project

# Table of Contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
SkrzatCompany is a practice project where we have a site with users verification and magement by admin who can add or delete users to the specific organizations (like Earth(Ziemia) ogranization or Moon(Księżyc) organization). The whole project is written in Python with Flask microframerowk and basic SQL queries with database in XAMPP's server package. Content of SkrzatCompany is written in Polish language.

After installing XAMPP and adding project to a valid directory, you can launch it by typing in your browser http://localhost:[port number]/index.html. You should see main page.

![MainPage](./images/image01.png)

You can verify user by choosing an organization, like "Ziemia":

![ZiemiaVerify](./images/image02.png)

If you don't have a user to check, go to your admin panel:

![AdminPanel](./images/image03.png)

Then click "Dodaj użytkownika" (Add user) below the list of users. Try to remember password you are typing because it is hashed and you will not restore it from database. 

![UserAdd](./images/image04.png)

If you would like to delete user from database, click "Usuń" (Delete) red button near password field.

![UserToDelete](./images/image05.png)

![UserDeleted](./images/image06.png)

As you can see, everyting works propely.

## Technologies
Project was made with:
* Python 3.7
* Flask
* Bootstrap 4.3.1 (to improve appearance)

## Setup
To run this project make sure you have installed XAMPP and you have configured your admin account on phpMyAdmin. It would be better, if you prepared simple database (which is included into the project). If so, you can run your project by typing "run appname.py" command and everything should work. If not, have a look at this site: https://flask.palletsprojects.com/en/1.1.x/quickstart/
