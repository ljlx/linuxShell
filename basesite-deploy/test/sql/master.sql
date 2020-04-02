CREATE TABLESPACE tbSpace1
ADD DATAFILE 'tbSpace1_1.dat'
USE LOGFILE GROUP logGroup1
EXTENT_SIZE =100M
INITIAL_SIZE = 3072M
AUTOEXTEND_SIZE = 100M
  --  INITIAL_SIZE 3072M
ENGINE INNODB;



SHOW MASTER LOGS;
SHOW MASTER STATUS ;
SHOW MASTER LOGS;

SELECT * FROM user;

RESET MASTER ;

SHOW TABLES ;



USE test;
CREATE TABLE testdata(
  sid INT(12) not null AUTO_INCREMENT,
  sname varchar(222),
  PRIMARY KEY (sid)
);


SELECT @@tx_isolation;

DELETE FROM testdata;

SELECT * FROM testdata;

ALTER TABLE testdata
  ADD column ssex varchar(2)
;

UPDATE testdata SET sname='zzzz';

UPDATE testdata SET sname='yyyy' WHERE sname='xxxx';

INSERT INTO testdata (sname,ssex) VALUES ('sss','1');
INSERT INTO testdata (sname,ssex) VALUES ('sss2','2');
INSERT INTO testdata (sname,ssex) VALUES ('sss3','3');
INSERT INTO testdata (sname,ssex) VALUES ('sss4','4');
INSERT INTO testdata (sname,ssex) VALUES ('sss4','4');
INSERT INTO testdata (sname,ssex) VALUES ('sss5','5');
INSERT INTO testdata (sname,ssex) VALUES ('sss6','6');

CREATE VIEW testdata_sex_man AS
  SELECT * FROM testdata WHERE testdata.ssex='1';

SELECT *
FROM testdata_sex_man;

SELECT * FROM testdata