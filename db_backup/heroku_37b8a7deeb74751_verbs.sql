CREATE DATABASE  IF NOT EXISTS `heroku_37b8a7deeb74751` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `heroku_37b8a7deeb74751`;
-- MySQL dump 10.13  Distrib 5.6.17, for Win32 (x86)
--
-- Host: us-cdbr-iron-east-01.cleardb.net    Database: heroku_37b8a7deeb74751
-- ------------------------------------------------------
-- Server version	5.5.40-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `verbs`
--

DROP TABLE IF EXISTS `verbs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `verbs` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `word` varchar(255) DEFAULT NULL,
  `pos` varchar(255) DEFAULT NULL,
  `trans` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1062 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `verbs`
--

LOCK TABLES `verbs` WRITE;
/*!40000 ALTER TABLE `verbs` DISABLE KEYS */;
INSERT INTO `verbs` VALUES (1,'annihilated','verb','yes'),(11,'appropriated','verb','yes'),(21,'ate','verb','no'),(31,'ate','verb','yes'),(41,'blasted','verb','yes'),(51,'blinked','verb','no'),(61,'bubbled up','verb','no'),(71,'burped','verb','no'),(81,'buzzed','verb','no'),(91,'charged','verb','no'),(101,'charged','verb','yes'),(111,'composed','verb','yes'),(121,'contained','verb','yes'),(131,'cried','verb','no'),(141,'cycled','verb','no'),(151,'damned','verb','yes'),(161,'decayed','verb','no'),(171,'destroyed','verb','yes'),(181,'detected','verb','yes'),(191,'died','verb','no'),(201,'disapproved','verb','no'),(211,'disliked','verb','yes'),(221,'ducked','verb','no'),(231,'eschewed','verb','yes'),(241,'excited','verb','yes'),(251,'exercised','verb','no'),(261,'exorcised','verb','yes'),(271,'fell','verb','no'),(281,'flashed','verb','yes'),(291,'flashed','verb','no'),(301,'flew','verb','no'),(311,'flew','verb','yes'),(321,'Force choked','verb','yes'),(331,'frittered away','verb','yes'),(341,'gave','verb','yes'),(351,'gave up','verb','no'),(361,'gave up','verb','yes'),(371,'gazed upon','verb','yes'),(381,'grabbed','verb','yes'),(391,'greased','verb','yes'),(401,'griped','verb','no'),(411,'hummed','verb','no'),(421,'hunted','verb','yes'),(431,'impressed','verb','yes'),(441,'injected','verb','yes'),(451,'interrupted','verb','yes'),(461,'jogged','verb','no'),(471,'jumped','verb','no'),(481,'jumped over','verb','yes'),(491,'kicked','verb','yes'),(501,'killed','verb','yes'),(511,'laughed','verb','no'),(521,'launched','verb','yes'),(531,'levelled','verb','yes'),(541,'liked','verb','yes'),(551,'melted','verb','no'),(561,'moved','verb','yes'),(571,'needed','verb','yes'),(581,'obeyed','verb','yes'),(591,'offended','verb','yes'),(601,'painted','verb','yes'),(611,'picked up','verb','yes'),(621,'poked','verb','yes'),(631,'polished','verb','yes'),(641,'poured','verb','yes'),(651,'presented','verb','yes'),(661,'pumped','verb','yes'),(671,'punched','verb','yes'),(681,'pushed','verb','yes'),(691,'refused','verb','no'),(701,'revived','verb','yes'),(711,'ruined','verb','yes'),(721,'satisfied','verb','yes'),(731,'scanned','verb','yes'),(741,'scattered','verb','yes'),(751,'scolded','verb','yes'),(761,'shot','verb','yes'),(771,'slapped','verb','yes'),(781,'sliced','verb','yes'),(791,'sneezed','verb','no'),(801,'snored','verb','no'),(811,'sparked','verb','yes'),(821,'spat','verb','no'),(831,'sprayed','verb','yes'),(841,'sprouted','verb','yes'),(851,'squealed','verb','no'),(861,'stabbed','verb','yes'),(871,'stamped out','verb','yes'),(881,'stepped on','verb','yes'),(891,'supplied','verb','yes'),(901,'tapped','verb','yes'),(911,'terrified','verb','yes'),(921,'threw','verb','yes'),(931,'took','verb','yes'),(941,'towed','verb','yes'),(951,'tripped','verb','no'),(961,'tripped','verb','yes'),(971,'trotted','verb','no'),(981,'tugged','verb','yes'),(991,'tumbled','verb','no'),(1001,'vanished','verb','no'),(1011,'wandered','verb','no'),(1021,'wobbled','verb','no'),(1031,'woke up','verb','no'),(1041,'wondered','verb','no'),(1051,'wrestled','verb','yes'),(1061,'wriggled','verb','no');
/*!40000 ALTER TABLE `verbs` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2014-11-14 22:35:36
