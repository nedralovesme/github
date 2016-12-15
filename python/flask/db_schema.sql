DROP TABLE IF EXISTS `student`;
CREATE TABLE `student` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` TEXT NULL,
  `mdate` DATETIME NULL,
  `cdate` DATETIME NULL,
  `deleted` TINYINT NULL DEFAULT 0,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1;

insert into student(`name`) values ('Janice');
insert into student(`name`) values ('Bill');
