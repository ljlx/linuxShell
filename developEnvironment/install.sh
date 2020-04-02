#!/bin/bash
####################################################
#
# File Name: addPub.sh
# Author: hx940929
# AuthorSite: https://www.thesunboy.com/
# Created Time: 2018年02月04日 星期日 23时10分42秒
###-----------------说明-------------------------###
#  安装开发环境脚本,主要是根据参数执行其下所有 或者指定的脚本,并且创建一个良好的执行环境 供子脚本执行
####################################################

#注册自定义函数运行环境
function regFunction(){
    if [ -z ${PUB_FACTION} ]; then
        PUB_FACTION="./bin/aliasAndEnv/function"
    fi
        for v in $(ls ${PUB_FACTION}/*.sh)
        do
            echo "init:"$v
            source $v;
        done;
        echo $(_getCurrentDir)
}

function _initenv(){
    regFunction;
}


isAutoSudo=true
svnurl="svn://mysvn.thesunboy.com:8443/releaseServer/shellScript"
#TODO  随意写的, 可能有以下问题: cp 权限问题,如果调用install.sh 的方法是使用的(bash | . ) 等方式 如何保证正确拷贝bin路径问题
function ss(){
isSudo=
if [[ ! -n "${curUser}" && "${curUser}" -eq 'root' ]]; then
        isSudo=
    else
        isSudo='sudo'
fi
#export my

export myshell_BaseDir=/usr/pubShells/developEnvironment
#/bin/aliasAndEnv
${isSudo} touch /usr/asdfasdfsf.test
if [ ! -d ${myshell_BaseDir} ]; then
    ${isSudo} mkdir -p ${myshell_BaseDir}
    issuc=$?
    if [ ${issuc} = '1' ]; then
       ${isSudo}  cp ./bin ${myshell_BaseDir}
    fi

fi
};
#判断当前用户及其操作的目录 是否需要申请使用sudo才能操作, 以及需要一个总开关
function issudo(){
    curUser=$(whoami)
    if [[ ${isAutoSudo} -eq 'true' ]]; then

          if [[ ! -n "${curUser}" && "${curUser}" -eq 'root' ]]; then
            echo ''
           else
            echo 'sudo'
          fi

    fi

    return $?;
};



#这个步骤不应该在这里做的.应该是提供一个sh文件 进行自动下载整个安装脚本进行wget这个安装包进行安装的
function checkoutFromSVN()
{
   #测试svn是否安装
   local issvn=$(which svn)

   if [[ ${issvn} != 0 ]]; then
       exit 1;
   fi 
}


#ln -s ${myshell_BaseDir}/setup.sh /etc/profile.d/myshellSetup.sh
function install()
{
    _initenv;
    realpath_parent=$(cd "$(dirname ..)"; pwd);
    echo "初始化路径:${realpath_parent}";
    echo "当前执行shell路径(0,install):$(_getCurrentDir)"

    for initsh in `ls ${realpath_parent}/bin`
    do
        local shpath=${realpath_parent}/bin/${initsh}/install.sh

        echo "当前检查路径:${shpath},$(_checkPermission ${shpath} r w x)"

        if [[ -x ${shpath} ]]; then
            echo "正在初始化脚本[${initsh}]:${shpath}"
            source ${shpath} install
            echo "初始化完成[${initsh}],结果:${?}"
        fi
    done


    return $?;
};


function uninstall()
{

    return $?;
};

case $1 in
 install)
    install;
    exit $?
   ;;
 uninstall)

    exit $?
   ;;
    *)
        echo '使用帮助:  install.sh (install | uninstall)'
        exit $?
    ;;
esac

ss=$(issudo)
echo $?;
