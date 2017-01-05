-- LOAD DATA LOCAL INFILE 'file.csv' INTO TABLE t1 
-- FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n'  
-- (@col1,@col2,@col3,@col4) set name=@col4,id=@col2 ;
-- 
drop table if exists t1;
CREATE TABLE `t1` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `year` varchar(45) DEFAULT NULL,
  `team` varchar(45) DEFAULT NULL,
  `owner` varchar(45) DEFAULT NULL,
  `pf` varchar(45) DEFAULT NULL,
  `wins` varchar(45) DEFAULT NULL,
  `col6` varchar(45) DEFAULT NULL,
  `col7` varchar(45) DEFAULT NULL,
  `col8` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=128 DEFAULT CHARSET=utf8;


LOAD DATA LOCAL INFILE '/Users/damianobrien/Downloads/TDMPFFL Historical/Win_Loss-Table 1.csv'
 INTO TABLE t1 
FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 LINES
(@col1,@col2,@col3,@col4,@col5) 
set owner=@col4,team=@col2,year=@col1,wins=@col5,pf=@col3;

select * from t1;
