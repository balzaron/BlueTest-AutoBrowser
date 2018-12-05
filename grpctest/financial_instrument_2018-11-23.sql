# ************************************************************
# Sequel Pro SQL dump
# Version 4541
#
# http://www.sequelpro.com/
# https://github.com/sequelpro/sequelpro
#
# Host: 127.0.0.1 (MySQL 5.7.23-log)
# Database: financial_instrument
# Generation Time: 2018-11-23 03:37:08 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table DB_VERSION
# ------------------------------------------------------------

DROP TABLE IF EXISTS `DB_VERSION`;

CREATE TABLE `DB_VERSION` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `schema` varchar(45) DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `version` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `DB_VERSION` WRITE;
/*!40000 ALTER TABLE `DB_VERSION` DISABLE KEYS */;

INSERT INTO `DB_VERSION` (`id`, `schema`, `update_time`, `version`)
VALUES
	(2,'financial_instrument','2018-11-22 02:23:22',1);

/*!40000 ALTER TABLE `DB_VERSION` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table MIOTECH_ASSET_ALIAS
# ------------------------------------------------------------

DROP TABLE IF EXISTS `MIOTECH_ASSET_ALIAS`;

CREATE TABLE `MIOTECH_ASSET_ALIAS` (
  `asset_id` bigint(11) NOT NULL,
  `asset_alias` varchar(1000) DEFAULT NULL,
  `insert_time` bigint(20) NOT NULL,
  `user_id` varchar(2000) NOT NULL DEFAULT '',
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `MIOTECH_ASSET_ALIAS` WRITE;
/*!40000 ALTER TABLE `MIOTECH_ASSET_ALIAS` DISABLE KEYS */;

INSERT INTO `MIOTECH_ASSET_ALIAS` (`asset_id`, `asset_alias`, `insert_time`, `user_id`, `id`)
VALUES
	(1,'testAssetAlias',11111,'MioTech',1);

/*!40000 ALTER TABLE `MIOTECH_ASSET_ALIAS` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table MIOTECH_ASSET_FILE
# ------------------------------------------------------------

DROP TABLE IF EXISTS `MIOTECH_ASSET_FILE`;

CREATE TABLE `MIOTECH_ASSET_FILE` (
  `id` bigint(11) NOT NULL AUTO_INCREMENT,
  `asset_id` bigint(11) NOT NULL,
  `file_id` bigint(20) NOT NULL,
  `insert_time` bigint(20) NOT NULL,
  `user_id` varchar(2000) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `MIOTECH_ASSET_FILE` WRITE;
/*!40000 ALTER TABLE `MIOTECH_ASSET_FILE` DISABLE KEYS */;

INSERT INTO `MIOTECH_ASSET_FILE` (`id`, `asset_id`, `file_id`, `insert_time`, `user_id`)
VALUES
	(1,1,6666,1542940769281,'MioTech'),
	(309,20735,6666,1542883829249,'Silverhorn'),
	(310,20735,6666,1542940769281,'Silverhorn');

/*!40000 ALTER TABLE `MIOTECH_ASSET_FILE` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table MIOTECH_ASSET_TAG
# ------------------------------------------------------------

DROP TABLE IF EXISTS `MIOTECH_ASSET_TAG`;

CREATE TABLE `MIOTECH_ASSET_TAG` (
  `asset_tag_id` bigint(11) NOT NULL AUTO_INCREMENT,
  `asset_tag_category_id` bigint(11) NOT NULL,
  `asset_tag_name` varchar(1000) NOT NULL,
  `asset_tag_type_id` bigint(11) NOT NULL,
  `asset_tag_minimun_value` varchar(200) DEFAULT NULL,
  `asset_tag_maximum_value` varchar(200) DEFAULT NULL,
  `editable` int(11) NOT NULL DEFAULT '1',
  PRIMARY KEY (`asset_tag_id`),
  KEY `FK_ASSET_TAG_TO_ASSET_TAG_TYPE_idx` (`asset_tag_type_id`),
  KEY `FK_ASSET_TAG_TO_ASSET_TAG_CATEGORY_idx` (`asset_tag_category_id`),
  CONSTRAINT `FK_ASSET_TAG_TO_ASSET_TAG_CATEGORY` FOREIGN KEY (`asset_tag_category_id`) REFERENCES `MIOTECH_ASSET_TAG_CATEGORY` (`asset_tag_category_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `FK_ASSET_TAG_TO_ASSET_TAG_TYPE` FOREIGN KEY (`asset_tag_type_id`) REFERENCES `MIOTECH_ASSET_TAG_TYPE` (`asset_tag_type_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `MIOTECH_ASSET_TAG` WRITE;
/*!40000 ALTER TABLE `MIOTECH_ASSET_TAG` DISABLE KEYS */;

INSERT INTO `MIOTECH_ASSET_TAG` (`asset_tag_id`, `asset_tag_category_id`, `asset_tag_name`, `asset_tag_type_id`, `asset_tag_minimun_value`, `asset_tag_maximum_value`, `editable`)
VALUES
	(1,1,'testAssetTagName',1,'0','10',1),
	(2,1,'testAssetTagName',1,'0','10',0);

/*!40000 ALTER TABLE `MIOTECH_ASSET_TAG` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table MIOTECH_ASSET_TAG_CATEGORY
# ------------------------------------------------------------

DROP TABLE IF EXISTS `MIOTECH_ASSET_TAG_CATEGORY`;

CREATE TABLE `MIOTECH_ASSET_TAG_CATEGORY` (
  `asset_tag_category_id` bigint(11) NOT NULL AUTO_INCREMENT,
  `asset_tag_category_name` varchar(1000) NOT NULL,
  `name_editable` int(11) NOT NULL DEFAULT '1',
  `content_editable` int(11) NOT NULL DEFAULT '1',
  `user_id` varchar(200) NOT NULL DEFAULT '',
  PRIMARY KEY (`asset_tag_category_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `MIOTECH_ASSET_TAG_CATEGORY` WRITE;
/*!40000 ALTER TABLE `MIOTECH_ASSET_TAG_CATEGORY` DISABLE KEYS */;

INSERT INTO `MIOTECH_ASSET_TAG_CATEGORY` (`asset_tag_category_id`, `asset_tag_category_name`, `name_editable`, `content_editable`, `user_id`)
VALUES
	(1,'TestTagCategoryName',1,1,'MioTech'),
	(2,'TestTagCategoryName',1,0,'MioTech'),
	(3,'TestTagCategoryName',0,0,'MioTech'),
	(4,'TestTagCategoryName',1,0,'MioTech'),
	(506,'Test',1,1,'Silverhorn');

/*!40000 ALTER TABLE `MIOTECH_ASSET_TAG_CATEGORY` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table MIOTECH_ASSET_TAG_CHOICE
# ------------------------------------------------------------

DROP TABLE IF EXISTS `MIOTECH_ASSET_TAG_CHOICE`;

CREATE TABLE `MIOTECH_ASSET_TAG_CHOICE` (
  `asset_tag_choice_id` bigint(11) NOT NULL AUTO_INCREMENT,
  `asset_tag_id` bigint(11) NOT NULL,
  `asset_tag_choice_name` varchar(4000) NOT NULL,
  PRIMARY KEY (`asset_tag_choice_id`),
  KEY `FK_ASSET_TAG_CHOICE_TO_ASSET_TAG_idx` (`asset_tag_id`),
  CONSTRAINT `FK_ASSET_TAG_CHOICE_TO_ASSET_TAG` FOREIGN KEY (`asset_tag_id`) REFERENCES `MIOTECH_ASSET_TAG` (`asset_tag_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `MIOTECH_ASSET_TAG_CHOICE` WRITE;
/*!40000 ALTER TABLE `MIOTECH_ASSET_TAG_CHOICE` DISABLE KEYS */;

INSERT INTO `MIOTECH_ASSET_TAG_CHOICE` (`asset_tag_choice_id`, `asset_tag_id`, `asset_tag_choice_name`)
VALUES
	(1,1,'testTagChoiceName');

/*!40000 ALTER TABLE `MIOTECH_ASSET_TAG_CHOICE` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table MIOTECH_ASSET_TAG_RECORD
# ------------------------------------------------------------

DROP TABLE IF EXISTS `MIOTECH_ASSET_TAG_RECORD`;

CREATE TABLE `MIOTECH_ASSET_TAG_RECORD` (
  `id` bigint(11) unsigned NOT NULL AUTO_INCREMENT,
  `asset_id` bigint(11) NOT NULL,
  `asset_tag_id` bigint(11) NOT NULL,
  `asset_tag_value` varchar(20) DEFAULT NULL,
  `insert_time` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `MIOTECH_ASSET_TAG_RECORD` WRITE;
/*!40000 ALTER TABLE `MIOTECH_ASSET_TAG_RECORD` DISABLE KEYS */;

INSERT INTO `MIOTECH_ASSET_TAG_RECORD` (`id`, `asset_id`, `asset_tag_id`, `asset_tag_value`, `insert_time`)
VALUES
	(1,1,1,'testAssetTagValue',1111);

/*!40000 ALTER TABLE `MIOTECH_ASSET_TAG_RECORD` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table MIOTECH_ASSET_TAG_RELATION
# ------------------------------------------------------------

DROP TABLE IF EXISTS `MIOTECH_ASSET_TAG_RELATION`;

CREATE TABLE `MIOTECH_ASSET_TAG_RELATION` (
  `asset_tag_relation_id` bigint(11) NOT NULL AUTO_INCREMENT,
  `asset_id` bigint(11) NOT NULL,
  `asset_tag_id` bigint(11) NOT NULL,
  `asset_tag_choice_id` bigint(11) DEFAULT NULL,
  `asset_tag_input_content` blob,
  `asset_tag_scenario_selected` int(11) DEFAULT NULL,
  `asset_tag_scenario_income` double DEFAULT NULL,
  `asset_tag_scenario_return_expect` double DEFAULT NULL,
  PRIMARY KEY (`asset_tag_relation_id`),
  KEY `FK_ASSET_TAG_RELATION_TO_ASSET_TAG_idx` (`asset_tag_id`),
  KEY `FK_ASSET_TAG_RELATION_TO_ASSET_TAG_CHOICE_idx` (`asset_tag_choice_id`),
  KEY `INDEX_ASSET_ID` (`asset_id`),
  CONSTRAINT `FK_ASSET_TAG_RELATION_TO_ASSET_TAG` FOREIGN KEY (`asset_tag_id`) REFERENCES `MIOTECH_ASSET_TAG` (`asset_tag_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `FK_ASSET_TAG_RELATION_TO_ASSET_TAG_CHOICE` FOREIGN KEY (`asset_tag_choice_id`) REFERENCES `MIOTECH_ASSET_TAG_CHOICE` (`asset_tag_choice_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `MIOTECH_ASSET_TAG_RELATION` WRITE;
/*!40000 ALTER TABLE `MIOTECH_ASSET_TAG_RELATION` DISABLE KEYS */;

INSERT INTO `MIOTECH_ASSET_TAG_RELATION` (`asset_tag_relation_id`, `asset_id`, `asset_tag_id`, `asset_tag_choice_id`, `asset_tag_input_content`, `asset_tag_scenario_selected`, `asset_tag_scenario_income`, `asset_tag_scenario_return_expect`)
VALUES
	(1,1,1,1,X'746573744173736574546167496E707574436F6E74656E74',1,1,1);

/*!40000 ALTER TABLE `MIOTECH_ASSET_TAG_RELATION` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table MIOTECH_ASSET_TAG_TYPE
# ------------------------------------------------------------

DROP TABLE IF EXISTS `MIOTECH_ASSET_TAG_TYPE`;

CREATE TABLE `MIOTECH_ASSET_TAG_TYPE` (
  `asset_tag_type_id` bigint(11) NOT NULL AUTO_INCREMENT,
  `asset_tag_type_name` varchar(200) NOT NULL,
  `user_id` varchar(200) NOT NULL DEFAULT '',
  PRIMARY KEY (`asset_tag_type_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `MIOTECH_ASSET_TAG_TYPE` WRITE;
/*!40000 ALTER TABLE `MIOTECH_ASSET_TAG_TYPE` DISABLE KEYS */;

INSERT INTO `MIOTECH_ASSET_TAG_TYPE` (`asset_tag_type_id`, `asset_tag_type_name`, `user_id`)
VALUES
	(1,'testAssetTagTypeName','MioTech');

/*!40000 ALTER TABLE `MIOTECH_ASSET_TAG_TYPE` ENABLE KEYS */;
UNLOCK TABLES;


/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
