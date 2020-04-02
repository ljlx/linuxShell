
# jira 管理平台 建库初始化脚本。


-- create db and user
CREATE DATABASE jiraMaster;
CREATE USER 'jiraAdmin'@'%' IDENTIFIED BY 'jiraAdmin';

-- do grant
-- dba to admin
GRANT ALL ON jiraMaster.* TO 'jiraAdmin'@'%';
GRANT ALL ON jiraMaster.* TO 'root'@'%';


SHOW ENGINES ;
USE jiraMaster;
SHOW TABLE STATUS ;


CREATE TABLE JQUARTZ_JOB_LISTENERS (
  JOB_NAME     VARCHAR(200) NOT NULL,
  JOB_GROUP    VARCHAR(200) NOT NULL,
  JOB_LISTENER VARCHAR(200) NOT NULL,
  CONSTRAINT PK_JQUARTZ_JOB_LISTENERS PRIMARY KEY (JOB_NAME, JOB_GROUP, JOB_LISTENER)
);

