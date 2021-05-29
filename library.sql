-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               5.7.17-log - MySQL Community Server (GPL)
-- Server OS:                    Win64
-- HeidiSQL Version:             11.2.0.6213
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for library
CREATE DATABASE IF NOT EXISTS `library` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `library`;

-- Dumping structure for table library.book
CREATE TABLE IF NOT EXISTS `book` (
  `ISBN` varchar(50) NOT NULL,
  `Title` varchar(100) NOT NULL,
  `Author` varchar(100) NOT NULL,
  `Publisher` varchar(100) DEFAULT NULL,
  `NumOfCopies` int(6) unsigned NOT NULL,
  `LatencyFinePerDay` decimal(20,6) unsigned NOT NULL,
  PRIMARY KEY (`ISBN`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.

-- Dumping structure for table library.borrowing
CREATE TABLE IF NOT EXISTS `borrowing` (
  `BorrowID` varchar(50) NOT NULL,
  `BookISBN` varchar(50) NOT NULL,
  `MemID` varchar(50) NOT NULL,
  `BorrowingDate` date NOT NULL,
  PRIMARY KEY (`BorrowID`),
  KEY `BorrowBookISBN` (`BookISBN`),
  KEY `BorrowMemID` (`MemID`),
  CONSTRAINT `BorrowBookISBN` FOREIGN KEY (`BookISBN`) REFERENCES `book` (`ISBN`),
  CONSTRAINT `BorrowMemID` FOREIGN KEY (`MemID`) REFERENCES `member` (`MemID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.

-- Dumping structure for table library.branch
CREATE TABLE IF NOT EXISTS `branch` (
  `BranchID` varchar(50) NOT NULL,
  `Address` varchar(100) NOT NULL,
  PRIMARY KEY (`BranchID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.

-- Dumping structure for table library.employee
CREATE TABLE IF NOT EXISTS `employee` (
  `EmpID` varchar(50) NOT NULL,
  `Name` varchar(100) NOT NULL,
  `Salary` decimal(20,6) NOT NULL,
  `Email` varchar(100) NOT NULL,
  `PhoneNum` varchar(50) NOT NULL,
  `BranchID` varchar(50) NOT NULL,
  PRIMARY KEY (`EmpID`),
  KEY `EmpBranchID` (`BranchID`),
  CONSTRAINT `EmpBranchID` FOREIGN KEY (`BranchID`) REFERENCES `branch` (`BranchID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.

-- Dumping structure for table library.member
CREATE TABLE IF NOT EXISTS `member` (
  `MemID` varchar(50) NOT NULL,
  `Name` varchar(100) NOT NULL,
  `PhoneNum` varchar(11) NOT NULL,
  `Email` varchar(100) NOT NULL,
  `RegDate` date NOT NULL,
  `BranchID` varchar(50) NOT NULL,
  PRIMARY KEY (`MemID`),
  KEY `MemBranchID` (`BranchID`),
  CONSTRAINT `MemBranchID` FOREIGN KEY (`BranchID`) REFERENCES `branch` (`BranchID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.

-- Dumping structure for table library.returning
CREATE TABLE IF NOT EXISTS `returning` (
  `ReturnID` varchar(50) NOT NULL,
  `BookISBN` varchar(50) NOT NULL,
  `MemID` varchar(50) NOT NULL,
  `ReturningDate` date NOT NULL,
  PRIMARY KEY (`ReturnID`),
  KEY `RetrunMemID` (`MemID`),
  KEY `ReturnBookISBN` (`BookISBN`),
  CONSTRAINT `ReturnBookISBN` FOREIGN KEY (`BookISBN`) REFERENCES `book` (`ISBN`),
  CONSTRAINT `ReturnMemID` FOREIGN KEY (`MemID`) REFERENCES `member` (`MemID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
