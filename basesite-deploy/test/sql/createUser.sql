SELECT * FROM user FOR UPDATE ;

DELETE FROM user WHERE user NOT LIKE 'root';


-- http://www.jb51.net/article/31850.htm
-- 创建用户
CREATE USER  'master'@'%' IDENTIFIED BY 'master';
GRANT REPLICATION SLAVE ON *.* TO 'master'@'%';


-- 普通授权
GRANT ALL ON test.* TO 'master'@'%';

-- 删除用户
DROP USER 'master'@'%';

SELECT *
FROM user;
-- dba授权
#GRANT privileges ON test.* TO 'master'@'%' WITH GRANT option


CREATE DATABASE test;
GRANT ALL ON test.* TO 'root'@'%';
GRANT ALL ON test.* TO 'master'@'%';


CREATE DATABASE test2;
GRANT ALL ON test2.* TO 'root'@'%';
USE test;
CREATE TABLE testdata(
  sid INT(12) not null AUTO_INCREMENT,
  sname varchar(222),
  PRIMARY KEY (sid)
);

ALTER TABLE testdata
  ADD column ssex varchar(2)
;

SHOW BINLOG EVENTS ;

DROP DATABASE test2;