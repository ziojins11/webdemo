--
-- Table structure for table `upload_images`
--

use web_demo;

DROP TABLE IF EXISTS `upload_images`;

CREATE TABLE `upload_images` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) DEFAULT '',
  `filename` varchar(255) DEFAULT '',
  `timeline` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;



LOCK TABLES `upload_images` WRITE;

INSERT INTO `upload_images` VALUES (1,'Jay Jin','clouds1.jpg','2023-07-31 04:21:11'),(2,'Jay Jin','clouds2.jpg','2023-07-31 04:21:15'),(3,'Jay Jin','clouds3.jpg','2023-07-31 04:21:20'),(4,'Jay Jin','clouds4.jpg','2023-07-31 04:21:25'),(5,'Jay Jin','clouds5.jpg','2023-07-31 04:24:26'),(6,'Jay Jin','clouds6.jpg','2023-07-31 04:24:30');

UNLOCK TABLES;

