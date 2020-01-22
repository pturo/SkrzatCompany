-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Czas generowania: 28 Maj 2019, 11:01
-- Wersja serwera: 10.1.40-MariaDB
-- Wersja PHP: 7.3.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Baza danych: `administracjabd`
--
CREATE DATABASE IF NOT EXISTS `administracjabd` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `administracjabd`;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `test`
--

CREATE TABLE `test` (
  `id` int(50) NOT NULL,
  `imie` varchar(50) NOT NULL,
  `nazwisko` varchar(50) NOT NULL,
  `plec` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Zrzut danych tabeli `test`
--

INSERT INTO `test` (`id`, `imie`, `nazwisko`, `plec`) VALUES
(1, 'Jan', 'Kowalski', 'M'),
(2, 'Anna', 'Kowalska', 'K');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `users`
--

CREATE TABLE `users` (
  `id` int(50) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Zrzut danych tabeli `users`
--

INSERT INTO `users` (`id`, `username`, `password`) VALUES
(1, 'rootadmin', '$5$rounds=535000$M4pgiySo1zVUXTq7$EJOjoefAdFTFIRgQITK8oGEjGKq7CG2mhfT6C6JBKB3');

--
-- Indeksy dla zrzutów tabel
--

--
-- Indeksy dla tabeli `test`
--
ALTER TABLE `test`
  ADD PRIMARY KEY (`id`);

--
-- Indeksy dla tabeli `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT dla tabeli `test`
--
ALTER TABLE `test`
  MODIFY `id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT dla tabeli `users`
--
ALTER TABLE `users`
  MODIFY `id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- Baza danych: `ksiezycbd`
--
CREATE DATABASE IF NOT EXISTS `ksiezycbd` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `ksiezycbd`;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `ksiezyc`
--

CREATE TABLE `ksiezyc` (
  `id` int(50) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(150) NOT NULL,
  `oddzial` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Indeksy dla zrzutów tabel
--

--
-- Indeksy dla tabeli `ksiezyc`
--
ALTER TABLE `ksiezyc`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT dla tabeli `ksiezyc`
--
ALTER TABLE `ksiezyc`
  MODIFY `id` int(50) NOT NULL AUTO_INCREMENT;
--
-- Baza danych: `marsbd`
--
CREATE DATABASE IF NOT EXISTS `marsbd` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `marsbd`;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `mars`
--

CREATE TABLE `mars` (
  `id` int(50) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(150) NOT NULL,
  `oddzial` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Indeksy dla zrzutów tabel
--

--
-- Indeksy dla tabeli `mars`
--
ALTER TABLE `mars`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT dla tabeli `mars`
--
ALTER TABLE `mars`
  MODIFY `id` int(50) NOT NULL AUTO_INCREMENT;
--
-- Baza danych: `ziemiabd`
--
CREATE DATABASE IF NOT EXISTS `ziemiabd` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `ziemiabd`;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `ziemia`
--

CREATE TABLE `ziemia` (
  `id` int(50) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(150) NOT NULL,
  `oddzial` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Zrzut danych tabeli `ziemia`
--

INSERT INTO `ziemia` (`id`, `username`, `password`, `oddzial`) VALUES
(1, 'Mandolina', '$5$rounds=535000$awBi68EMsAeensZx$Kxp6Gr6jKlGG8F8PwH2GNYetQ6GewoJYxh/R1UAyZa2', 'Ziemia');

--
-- Indeksy dla zrzutów tabel
--

--
-- Indeksy dla tabeli `ziemia`
--
ALTER TABLE `ziemia`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT dla tabeli `ziemia`
--
ALTER TABLE `ziemia`
  MODIFY `id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
