#!/bin/bash
#--------------------------------------------------
# File Name: ${FILE_NAME}
# Author: hanxu
# AuthorSite: https://www.thesunboy.com/
# Created Time: 2018-07-02 下午4:04
#---------------------说明--------------------------
#  创建可用的win7镜像
#---------------------------------------------------
#创建新的vm 虚拟机
osname="twin7";
osfolder="/home/hanxu/test/";
#内存大小（Mb）
osmemory=1024;
#显存大小 mb
osGraphicMem=256;
#os_vdi="/home/hanxu/.virtualbox/virtualmachines/vdi.d/win732.vdi";
os_vdi="/home/hanxu/test/copyofwin7/copyofwin7.vdi";
#删除虚拟机
#VBoxManage createvm --name ${osname} --remove

function _existvm(){
#    local listvms=VBoxManage list vms | awk '{print $1}' | xargs;
#    for item in ${listvms[@]};
#    do
#        echo item
#    done
    return 0;
}

function _rmvm(){
    VBoxManage unregistervm ${osname} --delete
    return $?;

};

function _initvm(){
    VBoxManage createvm --name ${osname} --ostype=Windows7 --register --basefolder ${osfolder}
#    >Virtual machine 'test' is created and registered.
#    >UUID: 9c855d61-f2ab-4fb5-a899-c6803fbb2110
#    >Settings file: '/home/hanxu/test/test/test.vbox'

    VBoxManage modifyvm ${osname} --cpus 1\
 --memory ${osmemory}\
 --vram ${osGraphicMem}\
 --acpi on \
 --ioapic on\
 --apic on;
    return 0;
};

function _addHddController(){
    #添加磁盘控制器
    VBoxManage storagectl ${osname} --name "sata1" \
    --add sata \
    --portcount 4 \
    --hostiocache on;
    return 0;
};

function _addHdd(){
    #添加虚拟磁盘
   VBoxManage storageattach ${osname} --storagectl "sata1" --port 0 --device 0\
    --type hdd\
    --medium ${os_vdi};
    #添加虚拟磁盘vdi文件

    return 0;
}

function _setNetwork(){

    #桥接网卡
    VBoxManage modifyvm ${osname} --nic1 bridged \
    --bridgeadapter1 enp3s0

}

function _listVms(){
    shift;
    listVms="vms";
    isrun=$1;
    if [[ ! -z ${isrun} && ${isrun} -eq "run"  ]];then
        listVms="runningvms";
    fi

    VBoxManage list ${listVms} | awk '{print $1 }';
};

function _getvmIp(){
    VBoxManage guestproperty enumerate ${osname} | grep "Net.*V4.*IP" | awk -F ':' '{print $3}' ;
};
function _getname(){
    shift;
    vmname=$1;
    if [[ -z ${vmname} ]];then
        vmname='test';
    fi
    echo ${vmname};
    return 0;
};

case $1 in
  initvm)
         osname=$(_getname ${@});
        _initvm;
        _addHddController;
        _addHdd;
        _setNetwork;
  ;;
  start)
    echo "starting...";
    osname=$(_getname ${@});
    VBoxManage startvm ${osname} --type headless
    echo "start ['${osname}'] successful"
  ;;
  stop)
    echo "stoping...:${@}";
    osname=$(_getname ${@});
    VBoxManage controlvm ${osname} savestate
  ;;
  rmvm)
  osname=$(_getname ${@});
    echo "deleteing vm ${osname} ...."
    _rmvm;
    echo "deleteing vm ${osname} !"
  ;;
  getip)
  osname=$(_getname ${@});
  _getvmIp;
  ;;
  list)
  echo $(_listVms $@);
  ;;


esac


#断电关机
#hanxu@hx-mint ~/test $ VBoxManage controlvm twin7 poweroff
#0%...10%...20%...30%...40%...50%...60%...70%...80%...90%...100%
#休眠关机
#hanxu@hx-mint ~/test $ VBoxManage controlvm twin7 savestate
#0%...10%...20%...30%...40%...50%...60%...70%...80%...90%...100%
#开机
#VBoxManage startvm twin7
