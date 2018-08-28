#!/usr/bin/env python
#coding:utf-8
#
#
author = "__keke__"

__declare__ = """
3/26:跟新数据库备份
3/28:eid唯一 云环境适配 保存密码等
3/30:修复一些输出问题
4/01:快照功能 
4/04:添加自动以证书文件路径以及crt文件路径位置
4/08:新加云环境内网下载安装包地址
4/25:liandoudou中country，选择语言
"""

__version__ = "1.1.15"

__all__ = [
    "arguments",
]

import os as _os
import sys as _sys
import time as _time
import logging as _logging
import platform as _platform
import urllib2 as _urllib2
import urllib as _urllib
import zipfile as _zipfile
import readline as _readline
import atexit as _atexit
import subprocess as _subprocess
import socket as _socket
import tarfile as _tarfile


import json
import re
from commands import getstatusoutput as getcmd


# 需要适配minic和channel
def tar(pakname='linkdood-server.tar.gz') :
    t = _tarfile.open(pakname)
    t.extract('data/linkdood/tools/rpm/python/python-argparse-1.2.1-2.1.el6.noarch.rpm','/')
    getcmd('/bin/rpm -i --nodeps --force /data/linkdood/tools/rpm/python/python-argparse-1.2.1-2.1.el6.noarch.rpm')
    t.close()

#0327
try :
    import argparse as _argparse
except :
    getcmd("/usr/bin/yum install -y python-argparse")
    try :
        import argparse as _argparse
    except :
        tar()
        import argparse as _argparse





# 初始化系统参数
class _init_system_property(object):
    def __init__(self):
        self.sys_init_parameter = {
            # 需要适配minic和标准版本
            "/var/spool/cron/root":[
                "#联网同步时间\n20 * * * * /usr/sbin/ntpdate cn.pool.ntp.org &> /dev/null\n",
                "#定期删除日志\n1 4 * * * /bin/find /data/linkdood/logs -name '*.log*' -type f -mtime +5 | xargs rm -f\n",
                "#服务自动启\n*/10 * * * * /usr/bin/python /usr/bin/linkd auto\n",
                "#切割nginx日志\n1 0 * * * /data/linkdood/im/bin/chut_nginx_log.sh\n",
                "#数据库备份\n1 3 * * * /usr/bin/python /data/linkdood/im/bin/backupdb.py &> /dev/null\n",
                #"#自动更新下载\n1 2 * * * /usr/bin/python /data/linkdood/im/bin/down_update.py &> /dev/null\n",
                #"#获取服务状态\n*/1 * * * * /data/linkdood/im/bin/callget.sh &> /dev/null\n",
                "#数据库和服务备份\n5 3 * * * /bin/bash /data/linkdood/im/bin/service_backup_3.0.sh &> /dev/null\n",
                ],
            "/etc/rc.d/rc.local":[
                "/data/linkdood/im/bin/vall\n",
                ],
            "/etc/hosts":[
                ],
            "/etc/sysctl.conf":[
                "net.ipv4.tcp_timestamps = 0\n",    # 防范伪造的sequence号码
                "net.ipv4.tcp_max_orphans = 3276800\n", # 抵御那些简单的DoS攻击
                "net.core.somaxconn = 32768\n",    # 同时发起并发TCP连接数
                "net.ipv4.tcp_tw_reuse = 1\n",     # 允许将TIME-WAIT 重新用于新的TCP连接
                "net.ipv4.tcp_tw_recycle = 1\n",   # 开启TCP连接中TIME-WAIT 的快速回收
                "net.ipv4.tcp_keepalive_time = 600\n",
                "net.ipv4.tcp_max_syn_backlog = 65535\n",
                "net.ipv4.tcp_max_tw_buckets = 5000\n", # 允许TIME-WAIT套接字数量的最大值
                "net.ipv4.ip_local_port_range = 10000 65535\n",
                ],
            "/etc/security/limits.conf":[
                "* soft nofile 999999\n",
                "* hard nofile 999999\n",
                ],
            "/etc/profile":[
                "ulimit -c 999999\n",
                ],
            "/etc/sysconfig/iptables":[
                "*filter\n",
                ":INPUT ACCEPT [0:0]\n",
                ":FORWARD ACCEPT [0:0]\n",
                ":OUTPUT ACCEPT [0:0]\n",
                "-A INPUT -p tcp -m state --state RELATED,ESTABLISHED -j ACCEPT\n",
                "-A INPUT -p tcp -m multiport --dports 22,80,443,4021,4022,10022,10080 -m state --state NEW,ESTABLISHED -j ACCEPT\n",
                "-A INPUT -p udp -j ACCEPT\n",
                "-A INPUT -p icmp -j ACCEPT\n",
                "-A INPUT -i lo -j ACCEPT\n",
                "-A INPUT -j DROP\n",
                "-A FORWARD -j DROP\n",
                "-A OUTPUT -p tcp -m state --state RELATED,ESTABLISHED -j ACCEPT\n",
                "-A OUTPUT -p tcp -m multiport --dports 22,80,443,465,2195,10022,10051 -m state --state NEW,ESTABLISHED -j ACCEPT\n",
                "-A OUTPUT -o lo -j ACCEPT\n",
                "-A OUTPUT -p icmp -j ACCEPT\n",
                "-A OUTPUT -p udp -j ACCEPT\n",
                "-A OUTPUT -j DROP\n",
                "COMMIT\n",
                ],
            "/etc/fstab":[ # 0328
                ],
        }

        hostname = _os.popen("hostname").read()
        self.sys_init_parameter["/etc/hosts"].append("127.0.0.1 %s"%hostname)
        
    # 移除之前的crontab配置
    def _remove_crontab(self,*names):
        for name in names:
            if name in self.sys_init_parameter:
                if not _os.path.isfile(name):
                    return True

                with open(name) as f:
                    content = f.readlines()

                for line in self.sys_init_parameter.get(name):
                    for l in line.split('\n'):
                        if l+'\n' in content :
                            content.remove(l+'\n')
                content = ''.join(content)
                with open(name,'w') as f:
                    f.write(content)

    def add_parameter(self,*names):
        for name in names:
            if name in self.sys_init_parameter:
                if name == '/etc/sysconfig/iptables':
                    self._add_write(name,self.sys_init_parameter[name],'w+')
                else:
                    self._add_write(name,self.sys_init_parameter[name])
            else :
                pass


    def _add_write(self,srcfile,datalist,pattern='a+'):
        try :
            with open(srcfile,pattern) as f:
                for row in datalist:
                    if row not in f:
                        f.write(row)
                    continue
        except IOError , e :
                pass


class vlogger(object):
    def __init__(self,logpath="/tmp/",logname="linkdood_info.log"):      # 修改日志文件路径     
        if not _os.path.isdir(logpath):
            _os.makedirs(logpath)
        self.logfile = logpath + logname

    # 记录日志
    def record(self,messages,level='debug'):
        logger = _logging.getLogger()
        if not logger.handlers:
            logger.setLevel(_logging.DEBUG)
            w_log = _logging.FileHandler(self.logfile)
            formatter = _logging.Formatter('%(asctime)s - %(name)s - %(levelname)s : %(message)s')
            w_log.setFormatter(formatter)
            logger.addHandler(w_log)

        if level == "info" :
            logger.info(messages)
        elif level == "debug":
            logger.debug(messages)
        elif level == "warn":
            logger.warning(messages)
        elif level == "error":
            logger.error(messages)
        else :
            logger.debug(messages)

    # 输出到屏幕并记录
    def echo(self,messages,color='white',backgroud=False,raw=False):
        '''
        messages = The output text info
        color = The color of the messages
        background = Show blackground color but dno't show color of the messages
        raw = "raw_input" output return value

        '''
        backgroud = '4' if backgroud else '3'

        color_dict = {'red':'1','green':'2','yellow':'3','blue':'4','purple':'5','sblue':'6'}
        if color in color_dict :
            msgs =  '\033[%s%sm%s\033[0m' %(backgroud,color_dict.get(color),messages)
        else :
            msgs = messages

        if raw :
            v = raw_input(msgs).strip()
        else :
            print(msgs)
            v = None
        if color == "red":
            self.record(messages,'error')
        elif color == "yellow":
            self.record(messages,'warn')
        else:
            self.record(messages,'info')

        return v

    # 执行linux命令 并记录
    def excmd(self,cmd):
        result,output = getcmd(cmd)
        if result :
            self.record('{0} result--> {1}'.format(cmd,output),'error')
            return result,output
        else :
            self.record('{0} result--> {1}'.format(cmd,output),'info')
            return result,output


class create_conf(object):
    def __init__(self,
        eurl=None,
        name=None,
        elogo=None,
        serverversion=None,
        #eid="1267",  # 2018/03/27 所有服务统一eid
        eid=None,  # 2018/03/27 所有服务统一eid
        country='cn',
        inip='127.0.0.1',
        outip='127.0.0.1',
        domain='linkdood.cn',
        admininitpw='123456',
        adminemail='vrv@vrv.com',
        adminphone='13666666666',
        interflow='0',
        configIp='127.0.0.1',
        preUrl='http://127.0.0.1:5000',
        lname='消息',
        conf_path = "/data/linkdood/im/conf/",
        conf_name = "liandoudou.conf"
        ):
        #super(create_conf,self).__init__()

        self.conf_file = conf_path + conf_name
        if not _os.path.isdir(conf_path):
            _os.makedirs(conf_path)

        # This is global configuration file of Linkdood
        self.conf = {
            "admininitpw":admininitpw,      # 初始密码
            "adminemail":adminemail,        # 初始邮箱
            "adminphone":adminphone,        # 初始手机
            "vdnsurl":"vdns.linkdood.cn",   #
            "interflow":interflow,          # 是否启用ag
            "status":"0",
            "remark":"",
            "vdnsport":"443",
            "mark":"vrv",
            "name":name,                    # 初始组件根节点
            "elogo":elogo,
            "eid":eid,
            "image":"",
            "lname":lname,                  # 客户端首页显示
            "eurl":eurl,
            "domain":domain,
            "serverversion":serverversion,
            "reportuser":"0",
            "inip":inip,
            "outip":outip,
            "registrable":"1",
            "ios": "1.0.0",
            "android":"1.0.0",
            "pc":"1.0.0",
            "pclogin":"1",
            "ioslogin":"1",
            "andlogin":"1",
            "configIp":configIp,
            "configPort":"8999",
            "isRegisteInNetwork":"true",
            "personMsgRetainDays":"7",
            "groupMsgRetainDays":"7",
            "isFilterBadWord":"false",
            "update":"22:00-24:00",
            "character":"8",
            "included":["1","4"],
            "phone":"1",
            "service":"1",  # 多服务开启
            "creategroup":"1",
            "tools":"1",    # 工具是否隐藏
            # 需要适配分割minic和chaneel
            #"private":"1", ##渠道版注释 2018年3月9日12:42:58
            "plan":"1",
            "activity":"1",
            "attention":"1",  # 关注是否显示
            "alertphone":[],
            "addr":[],
            "serverMessageContentMode":"1",
            "iospushmsgip":"iospushmsg.linkdood.cn",
            "iospushmsgPort":"2195",
            "smsaddr":"https://sms.linkdood.cn/msgpush",
            "TimeForDown":"259200",
            "dataFrom":"cn",
            "isCodecEnabled":"false",   # 数据库加密
            "redbag":"0",
            "offline":"0",
            "uploaduserinfo":"0",
            "isPwdStrength":"0",
            "preUrl":"http://127.0.0.1:5000",        # 预登录地址
            "indexImage":"",
            "apptitle":"",
            "logoImage":"",
            "customize":["doodlogin","emaillogin"],
            "entExtends":[],
            "loginPageImage":"",
            "isDoodOrCustom":"1",
            "isPhoneLogin":"1",
            "loginPageLogo":"",
            "menuLogo":"",
            "toplogo":"",
            "toptext":"登录",
            "badWordConfig":"2",
            "iosExtendPackPath":"",
            "iosExtendPackVersion":"",
            "andExtendPackVersion":"",
            "andExtendPackPath":"",
            "audit":"linkdood@A01",  # 审计管理员密码
            "secadmin":"S01@linkdood", # 保密管理员密码
            "country":"cn", #初始化语言
            #"isRoaming":"0",#2018年3月9日12:41:54 渠道版注释
            "entTitle":"信源豆豆管理中心",
            "entLable":"信源豆豆管理中心",
            "welcomeLable":"信源豆豆管理中心",
            "secTitle":"信源豆豆安全中心",
            "secLable":"信源豆豆安全中心",
            "titleIcon":"",
            "xinTitle":"信源豆豆公众服务平台",
            "xinLable":"信源豆豆公众服务平台",
            "xinLogo":"",
            "indexTitle":"信源豆豆官网",
            "doodName":"豆豆号",
            "diyIconName":"工作台",
            "diyIconStyle":"0",
            "onlineType":["all","ios","android"],
            "isIntranet":"true",
            "isupdate":"0", # 是否可以升级服务端
            "updateStatus":"0",
            "isIntranet":"false",
            "smsAlerts":"0",
            "smsAlertsTime":"1",
            "smsAlertsOption":"0",
            "isOpenIosApns":"0",
            "isLoginSmsValidate":"1",
            "onewayBuddy":"0",
            "mailaddr":"http://127.0.0.1:5002",
            "databaseId":"mysql",
            "freezeAfterDays":"180",
            "callbackAfterHours":"1",
            "sysAdminpw":"sys1234567",
            "sysAdminphone":"00862016080901",
            "sysAdminemail":"sysAdmin@qq.com",
            "permissionSwitch":"open",# 渠道版默认开启
            "preSendTime":"5",
            "dbconfigAddr":"ip=127.0.0.1&port=3306&DB=IM_DBCONFIG&user=root&pwd=knilVrvim0228%)",
            "configAddr":"ip=127.0.0.1&port=3306&DB=IM_CONFIG&user=root&pwd=knilVrvim0228%)",
            "voiceMeeting":{"needMasterControl":"true","appCertificate":"fc691b7b87224d3bba1f0340bbf6ce71","appID":"a4fdf852e3ba495ea598f3f0100bf8e4"}, #17/11/1
            "countryCode":"zh_cn", #17/11/1
            "renameRules":[],   #17/10/20
            #"isAutoRename":"1", #2018年3月9日12:41:54 渠道版注释
            "dmark":"pro",  #17/11/09 # minic:0l java:pro
            "isStaffLevel":"0", #17/11/21
            "isInvitingCode":"1", # 17/12/25
            "dbcfgAddr":"tcp://127.0.0.1:3306/IM_DBCONFIG?user=root&password=knilVrvim0228%)", #mini 数据库连接地址
            "isInvitingCode":"1",                                                              #mini 
            "addrAomestic":"%s:10660"%outip,  # turnserver 18/01/29
            "addrAbroad":"%s:10660"%outip,    # avroad turnserver 18/01/29
            "serverLimitFlow":"0",            # 是否限制流量服务器 18/03/26
            }

    # 生成豆豆配置文件
    def create_ldd(self):
        with open(self.conf_file,"w") as f :
            json.dump(self.conf,f,ensure_ascii=False,sort_keys=True,indent=4)
        return True


class deploy_linkdood(vlogger,_init_system_property):
    def __init__(self,
        main=None,    # 主线版本
        detail='ins',       # 版本明细
        eid = None,         
        password = None, 
        offline = False,    # 是否离线安装
        address = False,    # 内网IP
        eurl = None,        # 外网IP 或者域名
        ischecksystem = False, # 是否跳过系统检测
        show_versions = False,
        show_enterprise_info = False,
        download = 'http://www.linkdood.cn/download/',  # 安装包下载地址
        cloud=None, #0327
        savepwd=None, #0327
        snapshoot=None, #0327 创建快照
        start_server=None, #0401 不启动服务
        rollback=None, # 0401 快照回滚
        auth_url=False,
        crt_url=None
        ):
        #super(deploy_linkdood,self).__init__()
        vlogger.__init__(self)
        _init_system_property.__init__(self)


        self._cloud_url = {
        'aliyun':'http://172.17.105.207/download/', # 阿里云华北2C区
        'aws':'http://172.31.52.247/download/', # aws 美国东部 弗吉尼亚北部
        'tencent':'http://10.105.247.116/download/', # 腾讯上海一区
        }
        # 暂时只支持主线版本下载
        if cloud in self._cloud_url.keys():
            if self._ck_url(self._cloud_url.get(cloud)+main) :
                download = self._cloud_url.get(cloud)
            
        # 安装包下载地址
        if detail == 'ins' :
            self._download_url = '{0}{1}'.format(download,main)
        else :
            self._download_url = '{0}{1}_{2}'.format(download,main,detail)

        self._download_url_changed = self._download_url+"/changed.json"


        self._cred = None  # 本地证书
        if main == 'minic' :
            self._standar_pak = 'linkdood-minic.tar.gz'   # 安装包名称
        else :
            self._standar_pak = 'linkdood-server.tar.gz'   # 安装包名称

        self._pwd = _os.getcwd() + _os.sep # 当前路径
        self._isCheckSysInfo = ischecksystem
        self._offline = offline

        # channel 默认的eid
        if main == 'standard' and not eid and not password :
            self._eid = 'standard'
            self._password = '3421791441'
        else :
            self._eid = eid
            self._password = password

        self._main_type = main
        self._showVersions = show_versions
        self._showEnterpriseInfo = show_enterprise_info
        self._eurl = eurl
        self._cloud = cloud # 0327 适配云镜像
        self._savepwd = savepwd # 0327 适配云镜像
        self._snapshoot = snapshoot # 0401 快照
        self._start_server = start_server # 0401 不启动服务
        self._rollback = rollback # 0401 快照回滚
        self._auth_url = auth_url
        self._crt_url = crt_url

        self._urls = {
            'getip':'http://getip.linkdood.cn',          # 获取外网ip地址
            'www':'http://www.linkdood.cn',               # 证书校验地址
            'sms':'https://sms.linkdood.cn',              # 短信通道地址
        }

        # 企业信息
        self.enterprise_info = {}
        # 系统初始化信息
        self.sysinfo = {
            'user':None,        # 0 root 
            'sysname':None,     # system name
            'sysversion':None,  # system version
            'meminfo':None,     # memory info
            'partition':[],   # dick size
            'cpuinfo':None,     # cpu info
            'outip':None,       # outer ip
            'inip':None,        # inside ip
           }

        # 需要适配minic和标准版本
        self._proc_info = {
            'mysql':[3306,],
            'redis':[6379,],
            'zookeeper':[2181,],
            'kafka':[9092,],
            'elasticsearch':[9200,9300,],
            'turnserver':[10660,10661,],
            'fdfs_trackerd':[22122,],
            'fdfs_storaged':[23000,],
            'prelogin':[5000,],
            'upload':[9089,],
            'ap':[4031,4032,4071,],
            'badword':[4100,],
            'apnsAgentConfig':[44444],
            'go-mail':[5002,],
            'nginx':[80,443,4021,],
            'tomcat-webapp':[3801,3802,],
            'tomcat-app':[11008,11009],
            'server-config':[8999,],
            }

        country = raw_input("Please select language Chinese or English, input cn or en(default:cn):").strip()
        if country:
            self.enterprise_info['country'] = country

        if address :
            # ip校验
            self.sysinfo["inip"] = address
            self.enterprise_info['inip'] = address
        else :
            self._choice_inner_ip()


        self._get_system_info()
        self.record(self.sysinfo)


    def _ck_url(self,url):
        try :
            u = _urllib2.urlopen(url,timeout=2)
            if u.code == 200 :
                self.record('使用内网url下载安装包')
                return True
            else:
                self.record('本地IP错误使用官网地址%s'%u.code,'warn')
                return False
        except :
            self.record('本地IP错误使用官网地址','warn')
            return False
        
    # 创建磁盘分区
    def _fdisk(self,disk):
        cmds = ["n\n","p\n","1\n","\n","+8G\n","n\n","p\n","2\n","\n","\n","t\n","1\n","82\n","w\n"]

        s,o = self.excmd('/bin/ls %s'%disk)
        if int(s) :
            self.echo('找不到数据库盘')
            return False

        pipe = _subprocess.Popen("/sbin/fdisk %s"%disk,shell=True,stdin=_subprocess.PIPE,stdout=_subprocess.PIPE,stderr=_subprocess.PIPE)
        for cmd in cmds :
            pipe.stdin.write(cmd)
        pipe.communicate()
        
        if not _os.path.isdir('/data') :
            _os.mkdir('/data')

        self.excmd('/sbin/mkfs.ext4 %s2'%disk)
        self.excmd('/bin/mount %s2 /data'%disk)
        self.excmd('/sbin/mkswap %s1'%disk)
        self.excmd('/sbin/swapon %s1'%disk)
        _,dataid = self.excmd("/sbin/blkid %s2|awk '{print $2}'"%disk)
        _,swapid = self.excmd("/sbin/blkid %s1|awk '{print $2}'"%disk)
        
        self.sys_init_parameter.get('/etc/fstab').append("%s    /data                       ext4    defaults        1 1\n"%dataid)
        self.sys_init_parameter.get('/etc/fstab').append("%s    swap                        swap    defaults        0 0\n"%swapid)
        self.add_parameter('/etc/fstab')
        return True
    

    # 0327
    def _cloud_base(self,cloud):
        if cloud in ("aliyun","tencent"):
            disk = "/dev/vdb"
            if not self._fdisk(disk) :
                pass
            return True
        elif cloud == 'aws':
            disk = "/dev/xvdb"
            if not self._fdisk(disk) :
                pass
            return True
        elif cloud == 'baidu':
            disk = "/dev/vdb"
            self.excmd('/bin/umount /mnt')
            self.excmd("/bin/sed -i '/^\/dev\/vdb/d' /etc/fstab")
            if not self._fdisk(disk) :
                pass
            return True
        else :
            return True
            
    def _stop_linkdood(self):
        self.excmd('/usr/bin/linkd all fstop')

    def _start_linkdood(self):
        self.excmd('/usr/bin/linkd all start')
        
    # 备份或删除之前的服务
    def remove_linkdood(self):
        result = self.echo('\n检查到您之前安装过此服务 是否进行备份并重新安装[yes/no]:',raw=1).strip()
        if result in ("yes","y","Y","YES"):
            self._remove_crontab("/var/spool/cron/root")
            self._stop_linkdood()
            self.excmd('/usr/bin/killall -9 java')
            self.excmd('/bin/mv /data/linkdood/ /data/linkdood_`date +"%Y%m%d%H%M"`')
            _time.sleep(3)
            return True
        else :
            return False
 

    def _ck_proc(self):
        flag = 1
        for p in self._proc_info :
            for port in self._proc_info.get(p) :
                s = _socket.socket()
                try :
                    s.connect(('127.0.0.1',int(port)))
                    s.close()
                    self.echo('提示:%-15s:%5s 端口被占用 请检查您系统环境'%(p,port),'red')
                    flag = 0
                except :
                    pass

        if _os.path.isfile('/data/linkdood/im/conf/liandoudou.conf') :
            flag = 2
        return flag

    # 检查是否有进程占用
    def _check_proc(self):
        flag = self._ck_proc()

        if flag == 1 :
            self._remove_crontab("/var/spool/cron/root")
            return True
        elif flag == 2 :
            if self.remove_linkdood() :
                flag = self._ck_proc()
                if flag != 1 :
                    self.echo('有一些无法处理的程序 您可以常识手动清理这些程序后 再次安装')
                    return False
                return True
            else :
                return False
        else :
            return False


    # 过滤内网ip
    def _choice_inner_ip(self):
        _,ip = getcmd("/sbin/ifconfig | awk '/.*inet addr/{print $2}'")
        iplist = [ i.strip('addr:') for i in ip.split('\n') if i not in ("addr:127.0.0.1","addr:192.168.42.1","addr:172.17.42.1")]
        if not self.sysinfo.get("inip"):
            self.sysinfo["inip"] = iplist[0]
            self.enterprise_info['inip'] = iplist[0]
        return

    def _get_url(self,url):
        if  self._eurl :
            return True
        eurl = self.echo('\n请输入您的外网IP或者域名 默认为[%s] : '%url ,raw=1).strip()
        self._eurl = eurl if eurl else url
        return True


    # 获取系统基本信息
    def _get_system_info(self):
    
        self.sysinfo['user'] = _os.geteuid()
        self.sysinfo['sysname'] = _platform.linux_distribution()[0]
        self.sysinfo['sysversion'] = _platform.linux_distribution()[1]

        _,m = self.excmd("/bin/grep MemTotal /proc/meminfo | awk '{print $2}'")
        self.sysinfo['meminfo'] = int(m) // 1000 // 1000

        _,d = self.excmd("/bin/df -Ph | awk '$NF~/data$|\/$|home$/{print $NF,$2}'")
        self.sysinfo['partition'] = [ tuple(i.split()) for i in d.split('\n') ]

        _,c = self.excmd("/bin/grep 'processor' /proc/cpuinfo | wc -l")
        self.sysinfo['cpuinfo'] = int(c)

        try:
            outip = _urllib2.urlopen(self._urls.get('getip'),timeout=2).read().rstrip('\n')
            self.sysinfo['outip'] = outip
        except Exception as e:
            self.sysinfo["outip"] = self.sysinfo["inip"]
        return

    # 检测操作系统是否符合标准
    def check_system(self):
        flag = 0 # 0 ok 
        if self.sysinfo.get('user') != 0 :
            self.echo('User        : %s' %self.sysinfo.get('user'),'red')
            flag = 1
        if self.sysinfo.get('sysname') == 'CentOS' and '7.0' > self.sysinfo.get('sysversion') > '6.5' :
            pass
        else :
            self.echo('Sysname     : %s_%s' %(self.sysinfo.get('sysname'),self.sysinfo.get('sysversion')),'yellow')
            flag = 1
        #if self.sysinfo.get('meminfo') < 16 :
        min_men = 3 if self._main_type == 'minic' else 16

        if self.sysinfo.get('meminfo') < min_men :
            self.echo('Memory info : %s' %self.sysinfo.get('meminfo'),'red')
            flag = 1

        #if self.sysinfo.get('cpuinfo') < 4 :
        if self.sysinfo.get('cpuinfo') < 2 :
            self.echo('CPU info    : %s' %self.sysinfo.get('cpuinfo'),'yellow')
            flag = 1

        urls = {} if self._offline else self._urls
        for url in urls :
            try :
                u = _urllib2.urlopen(self._urls.get(url),timeout=2)
                if u.code == 200 :
                    pass
                else:
                    self.echo('URL Status [%s]: %s' %(url,u.code),'red')
                    flag = 1
            except :
                self.echo('URL Status [%s]: Timeout' %self._urls.get(url),'red')
                flag = 1
        
        if not self._check_proc() : flag = 1

        if self._isCheckSysInfo : flag = 0


        if flag :
            return False
        else :
            return True



    def _ck_offline(self):
        verinfo = "package.json"

        files = _os.listdir(self._pwd)
        cred = [ i for i in files if i.endswith('gz') and i != self._standar_pak ]

        if len(cred) < 1 :   
            return False,"Not found license file : %s"%cred
        self._cred = cred[0]
        for f in (self._cred,self._standar_pak,verinfo):
            if not _os.path.isfile(f) :
                return False,"Not found file : %s"%f

        with open(verinfo) as f : self.enterprise_info['serverversion'] = json.load(f).get('version').rstrip('V')

        return True,''


    def is_offline(self):
        s,v = self._ck_offline()        
        if s :
            self._offline = True
            if not self._get_auth_info(self._pwd+self._cred):
                return False
            return True

        if not self._offline :
            return True
        else :
            self.echo(v,'red')
            return False

    # 联网认证并下载安装包
    def authentication(self):
        if self._offline :
            return True

        eid = None
        password = None

        if self._auth_url :
           url = self._auth_url
        elif self._eid or self._password :
            eid = self._eid
            password = self._password
        else :
            while not eid:
                eid = self.echo('Input your EID:',raw=1)
            while not password:
                password = self.echo('Input your Password:',raw=1)

        if not self._auth_url :
            # 校验证书地址
            auth_url = "%s/server-linkdood/server/eadVerify" %self._urls.get('www','http://www.linkdood.cn')
            urlcode = _urllib.urlencode({"verify":password, "token":eid, "type":"authentication"})
            content = _urllib.urlopen(auth_url,urlcode).read()
            auth_info = json.loads(content)
            if auth_info.get("status") != "successGetFile" :    # validation ead and code
                self.echo('EAD or PASSWORD error,Sorry.','red')
                return False
            # 下载证书
            url = auth_info.get('gz')

        self._cred = url.split('/')[-1]
    
        if not self._get_ver(url,self._cred) :
            return False
 
        # 读取企业信息
        if not self._get_auth_info(self._pwd+self._cred):
            return False

        # 获取版本列表
        try :
            data = _urllib2.urlopen(self._download_url_changed,timeout=2).read()
            ver_list = json.loads(data)
            vers = [i for i in ver_list.get('ls')]
            vers.append(ver_list.get('release'))
            if self._showVersions :
                self.echo("Version list:")
                for v in vers :
                    self.echo(v)

                ver = self.echo('Input version [default : %s] : '%ver_list.get('release') ,raw=1)

                if ver == '':
                    ver = ver_list.get('release')

                if ver in vers :
                    self.enterprise_info['serverversion'] = ver.strip('V')
                else:
                    self.echo("Not found such version in the version list",'red')
                    return Falsea
            else :
                self.enterprise_info['serverversion'] = ver_list.get('release').strip('V')
                
        except BaseException as e :
            print e
            return False

        down_pak = "{0}/V{1}/{2}".format(self._download_url,self.enterprise_info['serverversion'],self._standar_pak)

        if self._cloud :
            self._get_ver(down_pak,self._standar_pak)
        else :
            if not self._wget_ver(down_pak) :
                self.echo('下载安装包失败','red')
                return False

        return True

    # 解析企业证书信息
    def _get_auth_info(self,zipname):



        #jsonfile = self._cred.rstrip('gz') + 'json'
        z = _zipfile.ZipFile(zipname)

        for i in z.namelist() : 
            if i.endswith('json') :
                jsonfile = i

        info = z.read(jsonfile)
        info = json.loads(info)

    
        if not self._cloud :
            if self._eid == 'standard':
                self._get_url(self.sysinfo.get("inip"))
            else :
                self._get_url(info.get('domainName'))

        try :
            if self._eurl :
                if re.match('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$',self._eurl) :
                    self.enterprise_info['eurl'] = self._eurl
                    self.enterprise_info['outip'] = self._eurl
                    self.enterprise_info["domain"] = self._eurl
                else :
                    self.enterprise_info['eurl'] = self._eurl
                    self.enterprise_info['outip'] = info.get('outerNet')
            else :
                self.enterprise_info['eurl'] = info.get('domainName')
                self.enterprise_info['outip'] = info.get('outerNet') 


            self.enterprise_info['eid'] = info.get('enterpriseId') # 0328 eid统一
            self.enterprise_info['elogo'] = info.get('token')
            self.enterprise_info['name'] = info.get('name')
            self.enterprise_info['admininitpw'] = info.get('adpw')
            self.enterprise_info['adminemail'] = info.get('email')
            self.enterprise_info['adminphone'] = info.get('cellPhone')
        except :
            self.echo('证书格式不正确','red')
            return False

        # 是否可以修改企业信息
        if not self._showEnterpriseInfo :
            return True

        while True :
            for k,v in self.enterprise_info.items() :
                self.echo('%-12s : %-10s' %(k,v),'blue')

            #yne = self.echo('Are you sure you want to continue install (yes[CONTINUE]|no[EXIT]|edit[CUSTOMIZATION]) : ',raw=1)
            yne = self.echo('请确认您的企业信息 输入(yes[继续]|no[退出]|edit[编辑]) : ',raw=1)
            if yne in ('y','Y','yes'):
                break
            elif yne in ('n','N','no'):
                return False
            elif yne in ('e','edit'):
                args = self.echo("请输入您要编辑的值 [格式eid=**,eurl=vrv.linkdood.cn:10080]: ",raw=1)
                args = args.split(',')
                for p in args:
                    try :
                        n,a = p.split('=')
                    except :
                        self.echo('没有匹配的值 : %s'%p,'yellow')
                        break

                    if self.enterprise_info.get(n):
                        if n == "eurl":
                            self.enterprise_info[n] = a
                            if re.match('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$',a) :
                                self.enterprise_info["domain"] = a.split(':')[0]
                            elif re.match('.*linkdood.cn',a) :
                                self.enterprise_info["domain"] = 'linkdood.cn'
                            else :
                                self.enterprise_info["domain"] = a.split(':')[0]
                        else :
                            self.enterprise_info[n] = a
                    else :
                        self.echo('No such number: %s'%n,'yellow')
            elif yne == '' :
                break
            else :
                continue
        return True



    def vzip(self,zipname,dest,pwd=None):
        if not _zipfile.is_zipfile(zipname):
            self.echo("This is not compressed file of %s" %zipname,'red')
            return False
        z = _zipfile.ZipFile(zipname)
        z.extractall(dest)
        return True


    # 解压tar包
    def tar_pak(self):
        self.echo('unzip packages...')
        pak = self._pwd+self._standar_pak
        self.excmd('tar xf %s -C  /'%pak)
        cred = self._pwd+self._cred
        self.vzip(cred,'/data/linkdood/im/conf/')
        if self._crt_url :
            self._get_ver(self._crt_url,'/data/linkdood/im/conf/crt.conf')
        

    # 调用wget下班
    def _wget_ver(self,url,dest=None):
        wget = '/usr/bin/wget -t 5 -c %s' %url
        result = _subprocess.call(wget,shell=True)
        if int(result) :
            return False
        return True

    # 下载文件
    def _get_ver(self,url,dest):
        u = _urllib.urlopen(url)
        if int(u.code) == 200 :
            _urllib.urlretrieve(url,filename=dest)
        else :
            self.echo('%s --> %s'%(url,u.code),'red')
            return False
        return True



    def base(self):
        services = ["NetworkManager","acpid","atd","auditd","bluetooth","cpuspeed","cups","mdmonitor","rpcbind","rpcgssd"]
        for s in services :
            self.excmd('/sbin/service %s stop'%s)
            self.excmd('/sbin/chkconfig %s off'%s)

        self.excmd("/usr/sbin/setenforce 0")
        self.excmd("/bin/sed -i 's/SELINUX=enforcing/SELINUX=disabled/' /etc/selinux/config")
        self.excmd("/sbin/sysctl -p")
        self.excmd("ulimit -HSn 999999")
        self.excmd("ulimit -c 999999")
        self.excmd("/usr/sbin/ntpdate cn.pool.ntp.org")
        self.excmd("\cp -r /data/linkdood/tools/root/* /")
        self.excmd("/bin/ln -sv /data/linkdood/im/vrv/python36/bin/python3 /usr/bin/")
        
        #self.excmd("\cp /data/linkdood/im/minic/minidood/servconfig.json /data/linkdood/im/conf/") # minic 开启

    def ins_rpm(self):
        self.excmd("/bin/rpm -ivh --force --nodeps  /data/linkdood/tools/rpm/*/*")
        return

    def ins_mysql(self):
        self.excmd("/bin/bash /data/linkdood/im/vrv/mysql/initmysql.sh")
        return

    def init_db(self):

        self.excmd("unzip -o /data/linkdood/im/IMServer/sqlzipfile/database.zip -d /data/linkdood/tools/jsondb")

        _sys.path.append('/data/linkdood/tools/init_db')
        import main
        #pwds = main.main(['name','-p','/data/linkdood/im/minic/jsondb','-f','install'])
        #pwds = main.main(['name','-p','/data/linkdood/tools/jsondb','-f','install'])
        self._adminpwd = main.main(['name','-p','/data/linkdood/tools/jsondb','-f','install'])
        #self._adminpwd = pwds.get('admin')

        if self._savepwd :
            with open('/tmp/info.json',"w") as f :
                json.dump(pwds,f,ensure_ascii=False,sort_keys=True,indent=4)

        return True

    def init_servers(self):
        # turnserver configuration
        self.excmd("/bin/echo 'external-ip=%s/%s' >> /data/linkdood/im/vrv/turnserver/etc/turnserver.conf" %(self.sysinfo["outip"],self.sysinfo["inip"]))
        # fdfs 配置
        for f in ('client.conf','mod_fastdfs.conf','storage.conf') :
            self.excmd("""sed -i s@^tracker_server=.*@tracker_server=%s:22122@g /etc/fdfs/%s """ %(self.sysinfo['inip'],f))
        # prelogin 配置
        #conf = "/data/linkdood/im/minic/prelogin/apinfo.json"
        conf = "/data/linkdood/im/vrv/prelogin/apinfo.json"
        eurl = self.enterprise_info['eurl']
        inip = self.sysinfo['inip']
        logo = self.enterprise_info['elogo']
        self.excmd("""/bin/sed -i 's@\("ImageHost"\).*\(,\)@\\1 : "http://%s"\\2@g' %s""" %(eurl,conf))
        self.excmd("""/bin/sed -i 's@\("LocalDownURL"\).*\(,\)@\\1 : "http://%s/predownload/"\\2@g' %s""" %(eurl,conf))
        self.excmd("""/bin/sed -i '1,20s@\("UpURL"\).*\(,\)@\\1 : "http://%s"\\2@g' %s""" %(eurl,conf))
        self.excmd("""/bin/sed -i '20,150s@\("UpURL"\).*\(,\)@\\1 : ["http://%s"]\\2@g' %s""" %(eurl,conf))
        self.excmd("""/bin/sed -i '1,20s@\("DownURL"\).*\(,\)@\\1 : "http://%s"\\2@g' %s""" %(eurl,conf))
        self.excmd("""/bin/sed -i '20,150s@\("DownURL"\).*\(]\)@\\1 : ["http://%s"\\2@g' %s""" %(eurl,conf))
        self.excmd("""/bin/sed -i 's@\("OutterIP"\).*\(,\)@\\1 : "%s"\\2@g' %s""" %(eurl.split(":")[0],conf))
        self.excmd("""/bin/sed -i 's@\("InnerIP"\).*\(,\)@\\1 : "%s"\\2@g' %s"""%(inip,conf))
        self.excmd("""/bin/sed -i 's@\("ServerName"\).*\(,\)@\\1 : "%s"\\2@g' %s"""%(logo,conf))
        self.excmd("""/bin/sed -i 's@\("Online"\).*\(,\)@\"Online\":"0"\,@g' %s"""%conf)

        # nginx 配置
        ngxcnf = "/data/linkdood/im/vrv/nginx/conf/conf.d/"
        for i in "ngx_443.conf","ngx_80.conf","ngx_ap.conf" :
            self.excmd("/bin/sed -i 's@\(server_name\).*@\\1 %s;@g' %s%s" %(self.enterprise_info['eurl'].split(':')[0],ngxcnf,i))
            self.excmd("/bin/sed -i 's@\(ssl_certificate \).*@\\1  /data/linkdood/im/conf/%s.crt;@g' %s%s" %(self.enterprise_info['elogo'],ngxcnf,i))
            self.excmd("/bin/sed -i 's@\(ssl_certificate_key \).*@\\1  /data/linkdood/im/conf/%s.key;@g' %s%s" %(self.enterprise_info['elogo'],ngxcnf,i))
        
        #self.excmd("mv /data/linkdood/im/vrv/html /data/linkdood/im/vrv/nginx/")



    def endgame(self):
        self.echo('\n')
        # 0330
        self.echo("""
                      _____              _____    
                     / ___ \ ___   ___  / __  \  
                    / /  / / __ `/ __ `/ /  / /
                   / /__/ / /_/ / /_/ / /__/ /""",'sblue')
        self.echo("""         _________/______/ \___/ \___/___  _/ 
       /_    _   __      ____   __    \  \/
      / /   (_) /  \    / /| ` / /    /      
     / /   __  / /\ \  / / | |/ /    /            """,'purple')
        self.echo("""    / /___/ / / /  \ \/ /  | |\ \   /
   /_____/_/ /_/    \__/   |_| \_\ /
   \__    ________________________/
      \  /
       \/
        """,'blue')
        print """
     < http://%s >  
     User:admin Password:%s    
     """ %(self.enterprise_info['eurl'],self._adminpwd)
        

    def start_services(self):
        self.excmd("/bin/echo 1 > /proc/sys/vm/drop_caches")
        if self._snapshoot :
            self.excmd("/sbin/service mysqld stop")
            now_time = _time.strftime('%Y%m%d%H%M')
            self.excmd('/bin/cp -R /data/linkdood /data/linkdood_%s'%now_time)

        if not self._start_server :
            _subprocess.call('/data/linkdood/im/bin/vall1')
            #_subprocess.call('/data/linkdood/im/bin/vall',shell=True)
        self.excmd("/sbin/service iptables restart")


    def _rollback_linkdood(self):
        link_list = _os.listdir('/data/')
        link_list = [ i for i in link_list if re.match('^linkdood_[0-9]',i)]
        link_list.sort()
        for k,v in enumerate(link_list) :
            print k,v

        while True :
            try :
                link_id = self.echo('请选择要恢复的版本ID:',raw=1)
                pak_name = link_list[int(link_id)]
                break
            except Exception as e :
                self.echo('请输入合法的ID','red')
        
        self._remove_crontab("/var/spool/cron/root")
        self._stop_linkdood()
        self.excmd('/bin/mv /data/linkdood/ /data/linkdood_`date +"%Y%m%d%H%M"`')
        self.excmd('/bin/mv /data/%s /data/linkdood'%pak_name)
        self._start_linkdood()
        self.add_parameter('/var/spool/cron/root')
        self.echo('快照已恢复至%s,请检查服务.'%pak_name)
        return True
    


######################################
# 系统参数
######################################
def _arguments():
    '''
    args
        main 主版本类型
        type 第二版本类型
        ver  类型版本号
        address ip地址
        s    是否启动服务
    '''
    parser = _argparse.ArgumentParser(
        description="version: %s"%__version__ # 描述信息
        )
    parser.add_argument(
        "-m",
        "--main",
        default="standard", 
        #default="minic", 
        #default="channel", 
        choices=["channel","confid","minic","standard"], 
        help="自定义安装的类型 ") 
    parser.add_argument(
        "-d",
        "--detail",
        default="ins", 
        choices=["ins","pub","dev"], 
        help="自定义安装的类型明细")  
    parser.add_argument(
        "--show-versions",
        action="store_true",
        help="自定义安装版本")   # 帮助
    parser.add_argument(
        "--show-enterprise-info",
        action="store_true",
        help="自定义企业信息")   # 帮助

    parser.add_argument(
        "-e",
        "--eid",
        default=None, 
        help="安装企业EAD") 

    parser.add_argument(
        "-p",
        "--password",
        default=None, 
        help="安装口令") 

    parser.add_argument(
        "-o",
        "--offline",
        action="store_true",
        help="离线安装模式")
    parser.add_argument(
        "-i",
        "--address",
        default=False, 
        help="自定义内网IP") 
    parser.add_argument(
        "--eurl",
        default=None, 
        help="自定义外网IP或者域名") 
    # 0402
    parser.add_argument(
        "--auth-url",
        default=False,
        help="自定义授权文件下载地址")
    # 0402
    parser.add_argument(
        "--crt-url",
        default=None,
        help="自定义conf.crt下载地址")
    # 3/27
    parser.add_argument(
        "-c",
        "--cloud",
        default=None, 
        choices=["aliyun","aws","tencent","baidu"],
        help="适配云服务器")
    # 03/27
    parser.add_argument(
        "-s",
        "--savepwd",
        action="store_true",
        help="是否保存管理员密码")

    parser.add_argument(
        "--snapshoot",
        action="store_true",
        help="创建快照")

    parser.add_argument(
        "--rollback",
        action="store_true",
        help="恢复快照")

    parser.add_argument(
        "--start-server",
        action="store_true",
        help="安装后不启动服务")

    parser.add_argument(
        "--ischecksystem",
        action="store_true",
        help="跳过系统检测")
    
    args = parser.parse_args()
    return args.__dict__
 

def main(args):

    d = deploy_linkdood(**args)

    if d._rollback :
        d._rollback_linkdood()
        return True

    # 0327 适配云
    if not d._cloud_base(d._cloud):
        return False


    # 检查操作系统是否符合要求
    if not d.check_system() :
        d.record('操作系统不符合要求')
        return False


    if not d.is_offline():
        d.record('缺少离线安装包文件')
        return False

    if not d.authentication() :
        d.record('认证不通过')
        return False


    # 初始化liandoudou.conf
    c = create_conf(**d.enterprise_info)
    d.record(c.conf)
    c.create_ldd()

    d.tar_pak() 
    
    d.add_parameter('/etc/rc.d/rc.local','/etc/hosts','/etc/sysctl.conf','/etc/security/limits.conf','/etc/profile','/etc/sysconfig/iptables')

    d.base()
    d.ins_rpm()
    d.ins_mysql()
    d.init_db()
    d.init_servers()
    d.start_services()
    d.add_parameter('/var/spool/cron/root')
    d.endgame()
    d.record('True')



# 自动换行历史记录
def _tab():
    _readline.parse_and_bind('tab: complete')
    histfile = _os.path.join(_os.environ['HOME'], '.pythonhistory')
    try:
        _readline.read_history_file(histfile)
    except IOError:
        pass
    _atexit.register(_readline.write_history_file, histfile)


   
if __name__ == "__main__":
    reload(_sys)
    log = vlogger()
    _sys.setdefaultencoding("utf-8")
    _tab()
    try :
        main(_arguments())
    except Exception as e : # 0327
        log.echo('\n程序异常\n%s'%e,'red')
        log.record('False','error')
    except KeyboardInterrupt as e:
        log.echo('\n您使用Ctrl + C 取消了安装','yellow')
