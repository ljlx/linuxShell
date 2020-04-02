SELECT * FROM user FOR UPDATE ;

CREATE USER 'slave'@'%' IDENTIFIED BY 'slave';


CREATE DATABASE test;
GRANT ALL ON *.* TO 'root'@'%';

SELECT *
FROM servers;
SELECT *
FROM slave_master_info;
SELECT *
FROM slave_worker_info;
SELECT *
FROM slave_relay_log_info;


-- 配置slave连接master
STOP SLAVE ;

CHANGE MASTER TO MASTER_HOST='master.test.nas.lan',
  MASTER_PORT =5721,
  MASTER_USER ='master',
  MASTER_PASSWORD ='master',
  MASTER_LOG_FILE ='mysql-bin.000001',
  MASTER_LOG_POS =313;
 START SLAVE ;

SELECT t.* FROM
  (
)AS t


RESET SLAVE ;

