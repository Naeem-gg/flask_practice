-- phpMyAdmin SQL Dump
-- version 4.9.5deb2
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Jun 11, 2022 at 04:16 PM
-- Server version: 8.0.29-0ubuntu0.20.04.3
-- PHP Version: 7.4.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cleanblog`
--

-- --------------------------------------------------------

--
-- Table structure for table `contact`
--

CREATE TABLE `contact` (
  `srno` int NOT NULL,
  `name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone_num` varchar(13) NOT NULL,
  `message` text NOT NULL,
  `date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `contact`
--

INSERT INTO `contact` (`srno`, `name`, `email`, `phone_num`, `message`, `date`) VALUES
(1, 'naeem', 'naeem@gmail.com', '+91654789321', 'this is my sample message.', '2022-06-07 17:29:48'),
(2, 'faisal', 'faisal@gmail.com', '+654789321021', 'this is random message', '2022-06-07 17:30:25'),
(3, 'naeem', 'naeem@gmail.com', '1324567890', 'send hojana plz bassa', '2022-06-09 18:57:10'),
(4, 'shoeb', 'shoebupgrady@gmail.com', '7984561230', 'good work', '2022-06-10 14:34:32'),
(6, 'elon bhayya', 'somemail@someone.com', '1234567890', 'good work bro keep it up', '2022-06-10 17:54:18'),
(7, 'elon bhayya', 'somemail@someone.com', '1234567890', 'good work bro keep it up', '2022-06-10 17:55:04'),
(8, 'elon bhayya', 'somemail@someone.com', '1234567890', 'good work bro keep it up', '2022-06-10 17:56:23'),
(9, 'elon bhayya', 'somemail@someone.com', '1234567890', 'good work bro keep it up', '2022-06-10 17:56:36'),
(10, 'elon bhayya', 'somemail@someone.com', '1234567890', 'good work bro keep it up', '2022-06-10 17:58:02'),
(11, 'elon bhayya', 'somemail@someone.com', '1234567890', 'good work bro keep it up', '2022-06-10 17:59:45'),
(12, 'elon bhayya', 'somemail@someone.com', '1234567890', 'good work bro keep it up', '2022-06-10 18:02:55'),
(13, 'elon bhayya', 'somemail@someone.com', '1234567890', 'good work bro keep it up', '2022-06-10 18:03:58'),
(14, 'elon bhayya', 'somemail@someone.com', '1234567890', 'good work bro keep it up', '2022-06-10 18:05:14'),
(15, 'elon bhayya', 'somemail@someone.com', '1234567890', 'good work bro keep it up', '2022-06-10 18:05:30'),
(16, 'elon bhayya', 'somemail@someone.com', '1234567890', 'good work bro keep it up', '2022-06-10 18:11:17'),
(17, 'elon bhayya', 'somemail@someone.com', '1234567890', 'good work bro keep it up', '2022-06-10 18:12:14'),
(18, 'elon bhayya', 'somemail@someone.com', '1234567890', 'good work bro keep it up', '2022-06-10 18:13:30'),
(19, 'elon bhayya', 'hsadg@gasdgsaj.com', '1234567890', 'good work bro keep it up', '2022-06-10 18:13:48'),
(20, 'elon bhayya', 'hsadg@gasdgsaj.com', '1234567890', 'good work bro keep it up', '2022-06-10 18:14:36'),
(21, 'elon bhayya', 'ansarifaisalmalik123@gmail.com', '1234567890', 'good work bro keep it up', '2022-06-10 18:15:09'),
(22, 'elon bhayya', 'upgradecomputers.edu@gmail.com', '1234567890', 'good work bro keep it up', '2022-06-10 18:15:55'),
(23, 'elon bhayya', 'naeem_gg@yahoo.com', '1234567890', 'good work bro keep it up', '2022-06-10 18:17:18'),
(24, 'someone', 'sabbb@yahoo.com', '7894561230', 'sending something special', '2022-06-10 18:33:28');

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `srno` int NOT NULL,
  `title` varchar(60) NOT NULL,
  `content` text NOT NULL,
  `post_by` varchar(50) NOT NULL,
  `date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`srno`, `title`, `content`, `post_by`, `date`) VALUES
(1, 'first flask  post', 'Welcome to Flask’s documentation. Get started with Installation and then get an overview with the Quickstart. There is also a more detailed Tutorial that shows how to create a small but complete application with Flask. Common patterns are described in the Patterns for Flask section. The rest of the docs describe each component of Flask in detail, with a full reference in the API section.\r\n\r\nFlask depends on the Jinja template engine and the Werkzeug WSGI toolkit. The documentation for these libraries can be found at:', 'flask officials', '2022-06-07 17:31:40');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contact`
--
ALTER TABLE `contact`
  ADD PRIMARY KEY (`srno`);

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`srno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contact`
--
ALTER TABLE `contact`
  MODIFY `srno` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `srno` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
