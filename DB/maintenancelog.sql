-- MySQL dump 10.13  Distrib 8.0.29, for macos12 (arm64)
--
-- Host: localhost    Database: maintenancelog
-- ------------------------------------------------------
-- Server version	8.0.29

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `app_brush`
--

DROP TABLE IF EXISTS `app_brush`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `app_brush` (
  `id` int NOT NULL,
  `side` varchar(1) DEFAULT NULL,
  `setNum` int NOT NULL,
  `brushStyle` longtext NOT NULL,
  `siteCode` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_brush`
--

LOCK TABLES `app_brush` WRITE;
/*!40000 ALTER TABLE `app_brush` DISABLE KEYS */;
INSERT INTO `app_brush` VALUES (1,'D',1,'Wrap Brush',1),(2,'P',1,'Wrap Brush',1),(3,'D',2,'Wrap Brush',1),(4,'P',2,'Wrap Brush',1),(5,'D',1,'Side Washer',1),(6,'P',1,'Side Washer',1),(7,'D',1,'Rocker Brush',1),(8,'P',1,'Rocker Brush',1),(9,'D',2,'Rocker Brush',1),(10,'P',2,'Rocker Brush',1),(11,'',1,'Curtain',1),(12,'',2,'Curtain',1),(13,'',3,'Curtain',1),(14,'D',1,'Wrap Brush',2),(15,'P',1,'Wrap Brush',2),(16,'D',2,'Wrap Brush',2),(17,'P',2,'Wrap Brush',2),(18,'D',1,'Side Washer',2),(19,'P',1,'Side Washer',2),(20,'D',1,'Rocker Brush',2),(21,'P',1,'Rocker Brush',2),(22,'N',1,'Curtain',2),(23,'N',2,'Curtain',2),(24,'N',3,'Curtain',2);
/*!40000 ALTER TABLE `app_brush` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_brushcomponent`
--

DROP TABLE IF EXISTS `app_brushcomponent`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `app_brushcomponent` (
  `id` int NOT NULL,
  `brushID` int NOT NULL,
  `motor` date NOT NULL,
  `shaft` date NOT NULL,
  `bearings` date NOT NULL,
  `upperBearings` date NOT NULL,
  `cloth` date NOT NULL,
  `shocks` date NOT NULL,
  `siteCode` int NOT NULL,
  `bearingsDueDate` date NOT NULL,
  `clothDueDate` date NOT NULL,
  `motorDueDate` date NOT NULL,
  `shaftDueDate` date NOT NULL,
  `shocksDueDate` date NOT NULL,
  `upperBearingsDueDate` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_brushcomponent`
--

LOCK TABLES `app_brushcomponent` WRITE;
/*!40000 ALTER TABLE `app_brushcomponent` DISABLE KEYS */;
INSERT INTO `app_brushcomponent` VALUES (1,1,'2020-01-01','2022-07-10','2022-07-12','2019-01-29','2022-07-15','2022-07-15',1,'2023-01-15','2023-01-15','2023-01-15','2023-01-15','2023-01-15','2023-01-15'),(2,2,'2020-01-01','2022-07-10','2022-07-15','2018-05-29','2022-07-15','2022-07-15',1,'2023-01-15','2023-01-15','2023-01-15','2023-01-15','2023-01-15','2023-01-15'),(3,3,'2018-06-30','2022-07-10','2022-07-15','2019-01-29','2022-07-15','2022-07-15',1,'2023-01-15','2023-01-15','2023-01-15','2023-01-15','2023-01-15','2023-01-15'),(4,4,'2020-01-01','2022-07-10','2022-07-15','2018-09-26','2022-07-15','2022-07-15',1,'2023-01-15','2023-01-15','2023-01-15','2023-01-15','2023-01-15','2023-01-15'),(5,5,'2019-01-29','2022-07-10','2022-07-15','2018-11-29','2022-07-15','2022-07-15',1,'2023-01-15','2023-01-15','2023-01-15','2023-01-15','2023-01-15','2023-01-15'),(6,6,'2018-11-29','2022-07-10','2022-07-15','2018-05-25','2022-07-15','2022-07-15',1,'2023-01-15','2023-01-15','2023-01-15','2023-01-15','2023-01-15','2023-01-15'),(7,7,'2022-07-10','2022-07-10','2022-07-11','2022-07-28','2022-07-15','2022-07-15',1,'2023-01-15','2023-01-15','2023-01-15','2023-01-15','2023-01-15','2023-01-15'),(8,8,'2022-07-10','2022-07-10','2022-07-15','2022-07-28','2022-07-15','2022-07-15',1,'2023-01-15','2023-01-15','2023-01-15','2023-01-15','2023-01-15','2023-01-15'),(9,9,'2022-07-10','2022-07-10','2022-07-15','2022-07-15','2022-07-15','2022-07-15',1,'2023-01-15','2023-01-15','2023-01-15','2023-01-15','2023-01-15','2023-01-15'),(10,10,'2022-07-10','2022-07-10','2022-07-15','2022-07-15','2022-07-15','2022-07-15',1,'2023-01-15','2023-01-15','2023-01-15','2023-01-15','2023-01-15','2023-01-15'),(11,11,'2022-07-15','2022-07-10','2022-07-15','2022-07-15','2022-07-10','2022-07-15',1,'2023-01-15','2023-01-15','2023-01-15','2023-01-15','2023-01-15','2023-01-15'),(12,12,'2022-07-10','2022-07-10','2022-07-15','2022-07-15','2022-07-15','2022-07-15',1,'2023-01-15','2023-01-15','2023-01-15','2023-01-15','2023-01-15','2023-01-15'),(13,13,'2022-07-10','2022-07-10','2022-07-15','2022-07-15','2022-07-15','2022-07-15',1,'2023-01-15','2023-01-15','2023-01-15','2023-01-15','2023-01-15','2023-01-15'),(14,14,'2022-07-15','2022-07-15','2022-07-15','2022-07-15','2022-07-15','2022-07-15',2,'2023-01-15','2023-01-15','2023-01-15','2023-01-15','2023-01-15','2023-01-15'),(15,15,'2022-07-15','2022-07-15','2022-07-15','2022-07-15','2022-07-15','2022-07-15',2,'2023-01-15','2023-01-15','2023-01-15','2023-01-15','2023-01-15','2023-01-15'),(16,16,'2022-07-15','2022-07-15','2022-07-15','2022-07-15','2022-07-15','2022-07-15',2,'2023-01-15','2023-01-15','2023-01-15','2023-01-15','2023-01-15','2023-01-15'),(17,17,'2022-07-15','2022-07-15','2022-07-15','2022-07-15','2022-07-15','2022-07-15',2,'2023-01-15','2023-01-15','2023-01-15','2023-01-15','2023-01-15','2023-01-15'),(18,18,'2022-07-15','2022-07-15','2022-07-15','2022-07-15','2022-07-15','2022-07-15',2,'2023-01-15','2023-01-15','2023-01-15','2023-01-15','2023-01-15','2023-01-15'),(19,19,'2022-07-15','2022-07-15','2022-07-15','2022-07-15','2022-07-15','2022-07-15',2,'2023-01-15','2023-01-15','2023-01-15','2023-01-15','2023-01-15','2023-01-15'),(20,20,'2022-07-15','2022-07-15','2022-07-15','2022-07-15','2022-07-15','2022-07-15',2,'2023-01-15','2023-01-15','2023-01-15','2023-01-15','2023-01-15','2023-01-15'),(21,21,'2022-07-15','2022-07-15','2022-07-15','2022-07-15','2022-07-15','2022-07-15',2,'2023-01-15','2023-01-15','2023-01-15','2023-01-15','2023-01-15','2023-01-15'),(22,22,'2022-07-13','2022-07-15','2022-07-15','2022-07-15','2022-07-15','2022-07-15',2,'2023-01-15','2023-01-15','2023-01-15','2023-01-15','2023-01-15','2023-01-15'),(23,23,'2019-01-01','2022-07-15','2022-07-15','2022-07-15','2022-07-15','2022-07-15',2,'2023-01-15','2023-01-15','2023-01-15','2023-01-15','2023-01-15','2023-01-15'),(24,24,'2022-07-15','2022-07-15','2022-07-15','2022-07-15','2022-07-15','2022-07-15',2,'2023-01-15','2023-01-15','2023-01-15','2023-01-15','2023-01-15','2023-01-15');
/*!40000 ALTER TABLE `app_brushcomponent` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_employee`
--

DROP TABLE IF EXISTS `app_employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `app_employee` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `site` int NOT NULL,
  `user_id` int NOT NULL,
  `darkMode` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `app_employee_user_id_4491aba0_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_employee`
--

LOCK TABLES `app_employee` WRITE;
/*!40000 ALTER TABLE `app_employee` DISABLE KEYS */;
INSERT INTO `app_employee` VALUES (1,1,1,1),(2,1,14,0),(3,1,15,0),(4,1,16,0),(5,1,17,1),(6,1,18,0),(7,1,19,0),(8,1,20,0),(9,1,21,0),(10,1,22,0),(11,1,23,0),(12,1,24,0),(13,1,25,0),(14,1,26,1),(15,1,27,0);
/*!40000 ALTER TABLE `app_employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_hydraulichoses`
--

DROP TABLE IF EXISTS `app_hydraulichoses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `app_hydraulichoses` (
  `id` int NOT NULL,
  `brushID` int NOT NULL,
  `dateReplaced` date NOT NULL,
  `dueDate` date NOT NULL,
  `siteCode` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_hydraulichoses`
--

LOCK TABLES `app_hydraulichoses` WRITE;
/*!40000 ALTER TABLE `app_hydraulichoses` DISABLE KEYS */;
INSERT INTO `app_hydraulichoses` VALUES (1,1,'2022-08-08','2022-11-09',1),(2,1,'2022-08-09','2022-11-09',1),(3,2,'2022-08-09','2022-11-09',1),(4,2,'2022-08-09','2022-11-09',1),(5,3,'2022-08-09','2022-11-09',1),(6,3,'2022-08-09','2022-11-09',1),(7,4,'2022-08-09','2022-11-09',1),(8,4,'2022-08-09','2022-11-09',1),(9,5,'2022-08-09','2022-11-09',1),(10,5,'2022-08-09','2022-11-09',1),(11,6,'2022-08-09','2022-11-09',1),(12,6,'2022-08-09','2022-11-09',1),(13,7,'2022-08-09','2022-11-09',1),(14,7,'2022-08-09','2022-11-09',1),(15,8,'2022-08-09','2022-11-09',1),(16,8,'2022-08-09','2022-11-09',1),(17,9,'2022-08-09','2022-11-09',1),(18,9,'2022-08-09','2022-11-09',1),(19,10,'2022-08-09','2022-11-09',1),(20,10,'2022-08-09','2022-11-09',1),(21,14,'2022-08-09','2022-11-09',2),(22,14,'2022-08-09','2022-11-09',2),(23,15,'2022-08-09','2022-11-09',2),(24,15,'2022-08-09','2022-11-09',2),(25,16,'2022-08-09','2022-11-09',2),(26,16,'2022-08-09','2022-11-09',2),(27,17,'2022-08-09','2022-11-09',2),(28,17,'2022-08-09','2022-11-09',2),(29,18,'2022-08-09','2022-11-09',2),(30,18,'2022-08-09','2022-11-09',2),(31,19,'2022-08-09','2022-11-09',2),(32,19,'2022-08-09','2022-11-09',2),(33,20,'2022-08-09','2022-11-09',2),(34,20,'2022-08-09','2022-11-09',2),(35,21,'2022-08-09','2022-11-09',2),(36,21,'2022-08-09','2022-11-09',2);
/*!40000 ALTER TABLE `app_hydraulichoses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_inventory`
--

DROP TABLE IF EXISTS `app_inventory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `app_inventory` (
  `id` int NOT NULL,
  `partName` varchar(50) NOT NULL,
  `modelNumber` varchar(50) DEFAULT NULL,
  `quantity` int NOT NULL,
  `siteCode` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_inventory`
--

LOCK TABLES `app_inventory` WRITE;
/*!40000 ALTER TABLE `app_inventory` DISABLE KEYS */;
INSERT INTO `app_inventory` VALUES (1,'Motor-Wrap','103-1004-012',9,1),(2,'Motor-Side Brush','103-1004-012',10,1),(3,'Motor-Rocker Brush','103-1003-012',10,1),(4,'Motor-Curtain','103-1005-012',5,1),(5,'Motor-Blower',NULL,10,1),(6,'Motor-Conveyor',NULL,10,1),(7,'Heco',NULL,10,1);
/*!40000 ALTER TABLE `app_inventory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_maintenance`
--

DROP TABLE IF EXISTS `app_maintenance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `app_maintenance` (
  `id` int NOT NULL,
  `component` longtext NOT NULL,
  `dateReplaced` date NOT NULL,
  `dueDate` date NOT NULL,
  `notes` longtext NOT NULL,
  `siteCode` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_maintenance`
--

LOCK TABLES `app_maintenance` WRITE;
/*!40000 ALTER TABLE `app_maintenance` DISABLE KEYS */;
INSERT INTO `app_maintenance` VALUES (1,'Takeup Drum','2022-07-10','2023-01-15','hello\ntest\n\ntest2test3',1),(2,'Sprocket','2022-04-20','2022-10-20','\nThe sprocket needs to be checked soon.\n\nstarting to get damaged',1),(3,'Fork Cover','2022-07-10','2023-01-15','',1),(4,'Fork Cylinder','2022-07-11','2023-01-11','Enter notes here',1),(5,'Heco Drive','2022-07-10','2023-01-15','Enter notes here',1),(6,'Conveyor Hydraulic Motor','2022-07-10','2023-01-15','Enter notes here',1),(7,'Chain/Rollers','2022-07-10','2023-01-15','Enter notes here',1),(8,'Takeup Drum','2022-07-15','2023-01-15','Enter notes here',2),(9,'Sprocket','2022-07-15','2023-01-15','Enter notes here',2),(10,'Fork Cover','2022-07-15','2023-01-15','Enter notes here',2),(11,'Fork Cylinder','2022-07-15','2023-01-15','Enter notes here',2),(12,'Heco Drive','2022-07-15','2023-01-15','Enter notes here',2),(13,'Conveyor Hydraulic Motor','2022-07-15','2023-01-15','Enter notes here',2),(14,'Chain/Rollers','2022-07-15','2023-01-15','Enter notes here\ntest\n\n\ntest2\ntest3\ntest4\ntest5\ntest6\ntest7\n',2);
/*!40000 ALTER TABLE `app_maintenance` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add brush',7,'add_brush'),(26,'Can change brush',7,'change_brush'),(27,'Can delete brush',7,'delete_brush'),(28,'Can view brush',7,'view_brush'),(29,'Can add brush component',8,'add_brushcomponent'),(30,'Can change brush component',8,'change_brushcomponent'),(31,'Can delete brush component',8,'delete_brushcomponent'),(32,'Can view brush component',8,'view_brushcomponent'),(33,'Can add maintenance',9,'add_maintenance'),(34,'Can change maintenance',9,'change_maintenance'),(35,'Can delete maintenance',9,'delete_maintenance'),(36,'Can view maintenance',9,'view_maintenance'),(37,'Can add inventory',10,'add_inventory'),(38,'Can change inventory',10,'change_inventory'),(39,'Can delete inventory',10,'delete_inventory'),(40,'Can view inventory',10,'view_inventory'),(41,'Can add employee',11,'add_employee'),(42,'Can change employee',11,'change_employee'),(43,'Can delete employee',11,'delete_employee'),(44,'Can view employee',11,'view_employee'),(45,'Can add hydraulic hoses',12,'add_hydraulichoses'),(46,'Can change hydraulic hoses',12,'change_hydraulichoses'),(47,'Can delete hydraulic hoses',12,'delete_hydraulichoses'),(48,'Can view hydraulic hoses',12,'view_hydraulichoses');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$320000$HCibaSMsVcdAObMKaLasl0$koKzAb0sG7qi/YKi7IUFSl6V2HDojna6AiEqs+DFQL0=','2022-07-19 14:36:06.295975',0,'dfin','David','Finley','david@shitmail.com',0,1,'2022-07-08 15:51:36.282839'),(14,'pbkdf2_sha256$320000$6cjzgecPEhq2qwgwexFAh9$HguUOOKzUFSWq1cWzS2PQSYgPyCust5nkqeNb/U9fKE=',NULL,0,'test9','','','test9@mail.com',0,1,'2022-07-15 19:43:52.590071'),(15,'pbkdf2_sha256$320000$U3gKvUjPns5kZ8CFuLjfUZ$YNE3DyTx/jcBULlzT5XwRPPPiKiUz7XlpYiEXwU5z2U=','2022-07-15 19:51:07.584470',0,'matt','','','matt@shitmail.com',0,1,'2022-07-15 19:45:39.368679'),(16,'pbkdf2_sha256$320000$xqSVMo8vhZ6ibaaID5x5d7$Bd9DyT8uq8qG5H4SOjUi8Q133Df8AArZWdHMLFmmkUE=','2022-07-15 20:30:59.455653',0,'Dickball','','','Buttsauce@shitmail.com',0,1,'2022-07-15 20:20:24.933685'),(17,'pbkdf2_sha256$320000$rr8ASyr2vo2uXZ6MuErV9y$M8Xs4nSExrM7+XZrmXMm9pqR9uWQE/J6QNp3gHVTlLo=','2022-08-09 22:48:56.542073',0,'davidfinley','','','dfinley5656@gmail.com',0,1,'2022-08-08 16:44:59.176573'),(18,'pbkdf2_sha256$320000$At7LPRU8E49ixTihOuSOpV$4+H5ygsL5jYQl5iW7Awb+NUrO/oZ+x1nrWX59ezJJhQ=',NULL,0,'test','','','erin@test.com',0,1,'2022-08-09 01:59:55.981998'),(19,'pbkdf2_sha256$320000$8dSUoGWuqUwJWVLcoogBi6$VdHzUDG4ACRNyHm3OCZoRxf6tYTF56tot5snCrv2N5E=',NULL,0,'erin','','','erin@shitmail.com',0,1,'2022-08-09 02:02:57.131560'),(20,'pbkdf2_sha256$320000$SOhgSHrj8G9bMceKGAvf9E$8WbJliEmpHA7siLpl2O6rRjJKZC5FvN/II/5r3OQBdo=',NULL,0,'erin5','','','erin@shitmail.com',0,1,'2022-08-09 02:08:12.601257'),(21,'pbkdf2_sha256$320000$YPBTiQxwcHP3cVabeLuDTz$55RsuWKeB33RAbAywMUX3EYCdnD0iERVmIZQZrR15v4=',NULL,0,'copper','','','copper@test.com',0,1,'2022-08-09 02:12:56.367406'),(22,'pbkdf2_sha256$320000$wcSKYLBKmHm5rgOLv8q49q$w1AmS+4/MKcaT1HByECrQSjOMBvCL7ydCQ+Q6Ls6Xvs=',NULL,0,'copper2','','','copper2@test.com',0,1,'2022-08-09 02:14:42.940422'),(23,'pbkdf2_sha256$320000$HCY7VBobNo4CHeXCd2xInn$MHsT7SaPF1TALuGCjWo1hHf16wY54p2ngCJE5PS5Q9Q=',NULL,0,'copper3','','','copper3@test.com',0,1,'2022-08-09 02:15:46.123242'),(24,'pbkdf2_sha256$320000$ZE977nLHtSVKd3UfmCz3Ae$to/GvH+fbTvY/0g339kjyStj2fLLM+o8RcavFX/ux7Y=',NULL,0,'copper4','','','copper4@test.com',0,1,'2022-08-09 02:16:56.166933'),(25,'pbkdf2_sha256$320000$ysyswHNdxBF6cFsPhkvyAW$qdOr/F0PbZmFmW1IVZwXg1YBFP7rt3IZWq7F1XAOGV8=',NULL,0,'copper5','','','copper5@test.com',0,1,'2022-08-09 14:14:30.785780'),(26,'pbkdf2_sha256$320000$o3aPRASJuPlYQOfAQZniwx$3MFC53qVHkbR2dZI+NqMjXZmQtbaZVv6nTy9Bms/EOw=','2022-08-10 01:16:33.416475',0,'erinfwilson','Erin','Wilson','ewilson095@gmil.com',0,1,'2022-08-10 01:09:38.038196'),(27,'pbkdf2_sha256$320000$lK6EojwMFEHNz3EWEI4xYz$0497ytpUo46PwE43d7JoVtyOczKTjHdgyrnDTQQ8KwU=',NULL,0,'maxi','','','maxi@test.com',0,1,'2022-08-10 01:17:53.508616');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `brush`
--

DROP TABLE IF EXISTS `brush`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `brush` (
  `id` int NOT NULL AUTO_INCREMENT,
  `side` varchar(1) NOT NULL,
  `setNum` int NOT NULL,
  `brush_style` varchar(30) NOT NULL,
  `site_code` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `brush`
--

LOCK TABLES `brush` WRITE;
/*!40000 ALTER TABLE `brush` DISABLE KEYS */;
/*!40000 ALTER TABLE `brush` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(7,'app','brush'),(8,'app','brushcomponent'),(11,'app','employee'),(12,'app','hydraulichoses'),(10,'app','inventory'),(9,'app','maintenance'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2022-07-07 17:26:22.520855'),(2,'auth','0001_initial','2022-07-07 17:26:22.591453'),(3,'admin','0001_initial','2022-07-07 17:26:22.617613'),(4,'admin','0002_logentry_remove_auto_add','2022-07-07 17:26:22.620972'),(5,'admin','0003_logentry_add_action_flag_choices','2022-07-07 17:26:22.624262'),(6,'contenttypes','0002_remove_content_type_name','2022-07-07 17:26:22.639958'),(7,'auth','0002_alter_permission_name_max_length','2022-07-07 17:26:22.653003'),(8,'auth','0003_alter_user_email_max_length','2022-07-07 17:26:22.660673'),(9,'auth','0004_alter_user_username_opts','2022-07-07 17:26:22.664817'),(10,'auth','0005_alter_user_last_login_null','2022-07-07 17:26:22.674396'),(11,'auth','0006_require_contenttypes_0002','2022-07-07 17:26:22.675417'),(12,'auth','0007_alter_validators_add_error_messages','2022-07-07 17:26:22.679041'),(13,'auth','0008_alter_user_username_max_length','2022-07-07 17:26:22.690612'),(14,'auth','0009_alter_user_last_name_max_length','2022-07-07 17:26:22.701704'),(15,'auth','0010_alter_group_name_max_length','2022-07-07 17:26:22.707643'),(16,'auth','0011_update_proxy_permissions','2022-07-07 17:26:22.711126'),(17,'auth','0012_alter_user_first_name_max_length','2022-07-07 17:26:22.722884'),(18,'sessions','0001_initial','2022-07-07 17:26:22.728566'),(19,'app','0001_initial','2022-07-08 21:11:30.496864'),(20,'app','0002_alter_brushcomponent_bearings_and_more','2022-07-09 01:31:10.787417'),(21,'app','0003_alter_maintenance_notes','2022-07-09 02:35:42.096883'),(22,'app','0004_inventory','2022-07-12 20:02:42.346489'),(23,'app','0005_inventory_sitecode','2022-07-13 16:49:43.697432'),(24,'app','0006_employee','2022-07-13 17:00:43.056546'),(25,'app','0007_employee_darkmode','2022-07-14 03:08:38.270854'),(26,'app','0008_alter_employee_user','2022-07-14 15:12:58.691874'),(27,'app','0009_brushcomponent_bearingsreplace_and_more','2022-07-15 13:54:02.509557'),(28,'app','0010_rename_bearingsreplace_brushcomponent_bearingsduedate_and_more','2022-07-15 13:55:39.893089'),(29,'app','0011_hydraulichoses_alter_brushcomponent_bearings_and_more','2022-08-09 14:48:21.064031');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('jtrr0vb9s9f3283sdqbdat4mgn822pgo','.eJxVjrtuwyAUht-FtQnijmFs527dEXAOsRPLqAZPVd49tuShWf_b9_-RELc-hq3hGiYgnnBy-a-lmB-4HAbc43KrNNelr1OiR4SebqPfFXD-PLNvA2Ns4952SVrQUpScTCxuGLQFZaLQ2agsmCsSGVgoaHWWJgHHJJRCV5wsMYHZR9vU8WvnEM8v55uDU8Ncb3XrYY6thxV_N2x9JwomxJXZK3c_XHs-eK0oN5ZL88GYZ4w8X3aAUR0:1oDozu:IAO-cxnFzw2AghW_vjvl-yiYbge2WQDH7S2vp7jdGxs','2022-08-02 15:18:54.301856');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `MaintenanceDates`
--

DROP TABLE IF EXISTS `MaintenanceDates`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `MaintenanceDates` (
  `id` int DEFAULT NULL,
  `BrushID` int DEFAULT NULL,
  `motor` datetime DEFAULT NULL,
  `shaft` datetime DEFAULT NULL,
  `bearings` datetime DEFAULT NULL,
  `upperBearings` datetime DEFAULT NULL,
  `cloth` datetime DEFAULT NULL,
  `shocks` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `MaintenanceDates`
--

LOCK TABLES `MaintenanceDates` WRITE;
/*!40000 ALTER TABLE `MaintenanceDates` DISABLE KEYS */;
INSERT INTO `MaintenanceDates` VALUES (1,1,'2022-07-07 00:00:00','2022-07-07 00:00:00','2022-07-07 00:00:00','2019-01-29 00:00:00','2022-07-07 00:00:00','2022-07-07 00:00:00'),(2,2,'2022-07-07 00:00:00','2022-07-07 00:00:00','2022-07-07 00:00:00','2018-05-29 00:00:00','2022-07-07 00:00:00','2022-07-07 00:00:00'),(3,3,'2018-06-30 00:00:00','2022-07-07 00:00:00','2022-07-07 00:00:00','2019-01-29 00:00:00','2022-07-07 00:00:00','2022-07-07 00:00:00'),(4,4,'2022-07-07 00:00:00','2022-07-07 00:00:00','2022-07-07 00:00:00','2018-09-26 00:00:00','2022-07-07 00:00:00','2022-07-07 00:00:00'),(5,5,'2019-01-29 00:00:00','2022-07-07 00:00:00','2022-07-07 00:00:00','2018-11-29 00:00:00','2022-07-07 00:00:00','2022-07-07 00:00:00'),(6,6,'2018-11-29 00:00:00','2022-07-07 00:00:00','2022-07-07 00:00:00','2018-05-25 00:00:00','2022-07-07 00:00:00','2022-07-07 00:00:00'),(7,7,'2022-07-07 00:00:00','2022-07-07 00:00:00','2022-07-07 00:00:00','2022-07-07 00:00:00','2022-07-07 00:00:00','2022-07-07 00:00:00'),(8,8,'2022-07-07 00:00:00','2022-07-07 00:00:00','2022-07-07 00:00:00','2022-07-07 00:00:00','2022-07-07 00:00:00','2022-07-07 00:00:00'),(9,9,'2022-07-07 00:00:00','2022-07-07 00:00:00','2022-07-07 00:00:00','2022-07-07 00:00:00','2022-07-07 00:00:00','2022-07-07 00:00:00'),(10,10,'2022-07-07 00:00:00','2022-07-07 00:00:00','2022-07-07 00:00:00','2022-07-07 00:00:00','2022-07-07 00:00:00','2022-07-07 00:00:00'),(11,11,'2022-07-07 00:00:00','2022-07-07 00:00:00','2022-07-07 00:00:00','2022-07-07 00:00:00','2022-07-07 00:00:00','2022-07-07 00:00:00'),(12,12,'2022-07-07 00:00:00','2022-07-07 00:00:00','2022-07-07 00:00:00','2022-07-07 00:00:00','2022-07-07 00:00:00','2022-07-07 00:00:00'),(13,13,'2022-07-07 00:00:00','2022-07-07 00:00:00','2022-07-07 00:00:00','2022-07-07 00:00:00','2022-07-07 00:00:00','2022-07-07 00:00:00');
/*!40000 ALTER TABLE `MaintenanceDates` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-08-10  9:49:46
