#!/bin/bash
#--------------------------------------------------
# File Name: start.sh
# Author:
# AuthorSite: https://www. .com/
# Created Time: 2018-11-02 下午5:29
#---------------------说明--------------------------
#  2类网部署
#---------------------------------------------------

#--thrift.configServer.hostname=豆豆的配置服务地址 \
#--thrift.configServer.port=豆豆的配置服务端口 \
#--dood.db.name=数据库名,用来保存同步错误信息 \
#--dood.db.host=数据库地址 \
#--dood.db.port=数据库端口 \
#--dood.db.user=数据库用户名 \
#--dood.db.passwd=数据库密码 \
#--ganshu.secretkey=由甘肃星火提供 \
#--ganshu.serviceid=由甘肃星火提供 \
#--ganshu.protocol=http甘肃星火提供的接口地址协议http/https \
#--ganshu.host=甘肃星火提供的接口地址,ip或者域名 \
#--ganshu.port=甘肃星火提供的接口端口 \
#--ganshu.dood.enterprise-id=豆豆企业id,需要用来插入组织机构用户 \
#--ganshu.dood.operator-id=豆豆操作人id,管理员id即可,需要用来插入组织机构用户
#上述的除了ganshu.protocol=http不要配置,其他都需要配置.
#配置完后,访问同步服务的url来同步组织机构和用户.
#全量同步组织机构: nohup curl http://localhost:8080/ganshu/sync/alldepartment &;tail -f nohup.out
#全量同步组织机构: nohup curl http://localhost:8080/ganshu/sync/alluser &;tail -f nohup.out
#95.1.2.201:80
#正式环境的
#serviceId: a888a536b70a49f4ae5df3349509b030
#secketkey: 7fb57f3f9ddc9338c7d1561fe6c0a2d5

#测试环境的
#serviceId: bef2679348c54a17bdeedb028d364b34
#secketkey: 4edbd543bc8f36683376ca80516f3c8a

#本同步程序提供http访问的端口
serverport=8080

# 甘肃提供的服务serviceID
ganshuserviceid='a888a536b70a49f4ae5df3349509b030'
#甘肃提供的服务密钥
ganshusecretkey='7fb57f3f9ddc9338c7d1561fe6c0a2d5'

#甘肃提供的服务ip
ganshuhost=20.30.2.11
#甘肃提供的服务端口
ganshuport=10080


# 豆豆的服务地址
thriftconfigServerhostname=127.0.0.1

#豆豆配置中心服务端口
thriftconfigServerport=11200

# 管理员 21256832672
# 系统管理员21265121277
operatorId=21256832672

#---------BEGIN--增量同步定时查询-------------------
# 增量更新同步程序的访问地址
ganshuUpdate_enable=true
ganshuUpdate_host=20.30.2.11
ganshuUpdate_port=10077

##查询偏移页码
ganshuPageNo=0

##查询页码大小
ganshuPageSize=200

##同步查询定时延迟时间 单位秒
ganshuInitialDelay=60

##同步查询 间隔时间 单位秒
ganshuPeriod=120

 #---------END----同步定时查询-------------------

function start(){
exejar=$(/bin/ls dood-joint-ganshu*exec.jar)
nohup java -jar ${exejar} \
--ganshu.page-no=${ganshuPageNo} \
--ganshu.page-size=${ganshuPageSize} \
--ganshu.initial-delay=${ganshuInitialDelay} \
--ganshu.period=${ganshuPeriod} \
--spring.profiles.active=pro \
--thrift.configServer.hostname=${thriftconfigServerhostname} \
--thrift.configServer.port=${thriftconfigServerport} \
--spring.kafka.consumer.bootstrap-servers=${ganshu_kafka_ip}:${ganshu_kafka_port} \
--dood.debug.bjhd.save=false \
--ganshu.serviceidname=serviceID \
--ganshu.secretkeyname=secretKey \
--ganshu.secretkey=${ganshusecretkey} \
--ganshu.serviceid=${ganshuserviceid} \
--ganshu.protocol=http \
--ganshu.host=${ganshuhost} \
--ganshu.port=${ganshuport} \
--ganshu.sync.page-size=100 \
--ganshu.dood.enterprise-id=1267 \
--ganshu.dood.operator-id=${operatorId} \
--ganshu.dood.personal-status=1 \
--ganshu.update-sync.hostname=${ganshuUpdate_host} \
--ganshu.update-sync.port=${ganshuUpdate_port} \
--ganshu.update-sync.enable=${ganshuUpdate_enable} \
--logging.file=logs/dood-ganshu-sync.log &
}

function stop(){
doodSyncPid=$(ps aux|grep dood-joint-ganshu|grep -v grep|awk '{print $2}' |xargs)
if [[ -n ${doodSyncPid} ]]; then
    echo "kill ${doodSyncPid}"
    echo "停止豆豆同步服务:${doodSyncPid}"
    kill -9 ${doodSyncPid}
fi

}

function log(){
    tail -50f ./logs/dood-ganshu-sync.log
}
case $1 in
start)
    start
   ;;
stop)
    stop
   ;;
restart)
    stop
    start
    sleep 3
    log
    ;;
syncdept)
    #全量同步组织机构: nohup curl http://localhost:8080/ganshu/sync/alluser &;tail -f nohup.out
    nohup curl http://localhost:${serverport}/ganshu/sync/alldepartment > syncdept.log 2>&1 &
    log
    ;;
syncuser)
    #全量同步组织机构: nohup curl http://localhost:8080/ganshu/sync/alldepartment &;tail -f nohup.out
    nohup curl http://localhost:${serverport}/ganshu/sync/alluser > syncuser.log 2>&1 &
    log
    ;;
syncupdate)
    nohup curl http://localhost:${serverport}/ganshu/sync/update > syncuser.log 2>&1 &
    log
    ;;
log)
    log
    ;;
*)
    start
    sleep 3
    log
   ;;
esac
