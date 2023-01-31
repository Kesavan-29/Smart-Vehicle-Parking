-- phpMyAdmin SQL Dump
-- version 2.11.6
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Nov 11, 2022 at 03:34 AM
-- Server version: 5.0.51
-- PHP Version: 5.2.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `1vehicleparkdb`
--

-- --------------------------------------------------------

--
-- Table structure for table `entrytb`
--

CREATE TABLE `entrytb` (
  `id` bigint(20) NOT NULL auto_increment,
  `VehicleNo` varchar(250) NOT NULL,
  `Date` varchar(250) NOT NULL,
  `Status` varchar(250) NOT NULL,
  `ParkingNo` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=16 ;

--
-- Dumping data for table `entrytb`
--

INSERT INTO `entrytb` (`id`, `VehicleNo`, `Date`, `Status`, `ParkingNo`) VALUES
(12, 'TN45AL5535', '11-Nov-2022', 'out', '1'),
(13, 'TN45AL5536', '11-Nov-2022', 'in', '2'),
(14, 'TN45AL5537', '11-Nov-2022', 'in', '3'),
(15, 'TN45AL5535', '11-Nov-2022', 'in', '1');

-- --------------------------------------------------------

--
-- Table structure for table `regtb`
--

CREATE TABLE `regtb` (
  `id` bigint(10) NOT NULL auto_increment,
  `Name` varchar(250) NOT NULL,
  `Mobile` varchar(250) NOT NULL,
  `Email` varchar(250) NOT NULL,
  `VehicleNo` varchar(50) NOT NULL,
  `UserName` varchar(250) NOT NULL,
  `Password` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `regtb`
--

INSERT INTO `regtb` (`id`, `Name`, `Mobile`, `Email`, `VehicleNo`, `UserName`, `Password`) VALUES
(1, 'san', '9486365535', 'sangeeth5535@gmail.com', 'TN45AL5535', 'san', 'san'),
(2, 'sangeeth', '9486365535', 'sangeeth5535@gmail.com', 'TN45AL5536', 'sangeeth', 'sangeeth'),
(3, 'rajiya', '09087556035', 'rajiya@gmail.com', 'TN45AL5537', 'rajiya', 'rajiya');
