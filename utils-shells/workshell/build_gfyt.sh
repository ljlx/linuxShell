#!/bin/bash
#--------------------------------------------------
# File Name: ${NAME}
# Author: hanxu
# AuthorSite: https://www.thesunboy.com/
# Created Time: 2018-11-02 下午5:28
#---------------------说明--------------------------
#  
#---------------------------------------------------


jarname="dood-joint-ganshu"
splitDir="dir"
splitSize="2m"
buildDir="./xbuild"
buildContextPath=${buildDir}
projectDir=$(pwd)
splitSuffix="_split"
splitmd5file="splitFile.md5sum"

function mvnp(){
mvn clean package
}



function package(){
mkdir -p ${buildContextPath}/buildScript
local ljarname="${jarname}*exec.jar"
cp ./target/classes/buildScript/* ${buildContextPath}/buildScript/
cp ./target/${ljarname} ${buildContextPath}/
cd ${buildContextPath}
echo "进入目录 => $(pwd)"
mv ./buildScript/*.sh ./
sauth.sh
realjarname=$(ls ${ljarname})
nowdatea=$(date "+%Y-%m-%d-%H%M%S")
tarname="${jarname}-${nowdatea}"
md5sum ./${realjarname} > ${realjarname}.md5sum
tar -zcvf "${tarname}.tar.gz" ./*
md5sum ${tarname}.tar.gz > ${tarname}.tar.gz.md5sum
echo "离开目录 => $(pwd)"
cd ../
}

function gettarName(){
    local tarname="$(ls ${jarname}*.tar.gz)"
    echo ${tarname}
}

function clean(){
    echo "清理构建目录[${buildContextPath}]..."
    rm -rf ${buildContextPath}
    echo "清理构建目录完成,ExitCode:$?."
}

function _getsplitar(){
    echo ${jarname}.tar.gz.${splitDir}
}

function splittar(){
    cd ${buildContextPath}
    local tarname=$(gettarName)
    local dirname=$(_getsplitar)
    local dirpath="$(pwd)/${dirname}/"
    echo "开始切割压缩包[ ${tarname} ] >>> ${dirpath}"
    if [[ -d ${dirpath} ]]; then
        echo "正在删除=> ${dirpath}"
        rm -rf ${dirpath}
        echo "正在重建=> ${dirpath}"
    fi
    mkdir ${dirpath}
    _genMd5File ${tarname} "${dirpath}/${tarname}.md5sum"
    cd ${dirpath}
    echo "重建完成,正在分割文件..."
    split -d -u -b ${splitSize} --additional-suffix=${splitSuffix} ../${tarname} "${tarname}_"
    local sfilenum=$(/bin/ls ${dirpath} |wc |awk '{print $1}')
    local sfilesize=$(/usr/bin/du -sh |awk '{print $1}')

    echo "分割完成,exitCode[$?],分割文件数量:${sfilenum},分割后文件总字节大小:${sfilesize}"
    echo "正在计算生成文件的md5校验值$(pwd),使用后缀分隔符:${splitSuffix}"
    for item in $(/bin/ls *${splitSuffix}*)
    do
        _genMd5File ${item} ${splitmd5file}
    done
    echo "计算生成分割文件的md5校验值完毕."
    _genMerageSh ./
    cd ../

}
#参数1. 需要被计算md5值的文件名, 参数2:md5文件路径名
function _genMd5File(){
    md5sum $1 >> $2
}

function _genMerageSh(){

mergeShFile="$1/merge.sh"

if [[ -f ${mergeShFile} ]]; then
    rm -rf ${mergeShFile}
fi


echo 'function _checkMd5File(){' >> ${mergeShFile}
echo '    local checkfile=$1' >> ${mergeShFile}
echo '    echo "正在校验生成分割文件的md5校验值..."' >> ${mergeShFile}
echo '    checkResult=$(md5sum --quiet -c ${checkfile})' >> ${mergeShFile}
echo '    exitcode=$?' >> ${mergeShFile}
echo '    if [[ ${exitcode} != "0" ]]; then' >> ${mergeShFile}
echo '        echo "${checkResult} "' >> ${mergeShFile}
echo '        echo "md5校验不匹配."' >> ${mergeShFile}
echo '        return ${exitcode}' >> ${mergeShFile}
echo '    fi' >> ${mergeShFile}
echo '    echo "完成校验生成分割文件的md5校验值..."' >> ${mergeShFile}
echo '}' >> ${mergeShFile}
echo '' >> ${mergeShFile}
echo 'function _mergeTarFile(){' >> ${mergeShFile}
echo '    _checkMd5File splitFile.md5sum' >> ${mergeShFile}
echo '    checkResult=$?' >> ${mergeShFile}
echo '#    TODO suffix这里生成需要由build的变量定义.暂时写死' >> ${mergeShFile}
echo '    local splitSuffix="_split"' >> ${mergeShFile}
echo '    if [[ ${checkResult} != "0" ]]; then' >> ${mergeShFile}
echo '        exit ${exitcode}' >> ${mergeShFile}
echo '    fi' >> ${mergeShFile}
echo "    local ltarname=$(ls |head -1|awk -F "_00" '{print $1}')" >> ${mergeShFile}
echo '    echo "正在合并分割压缩包${ltarname}"' >> ${mergeShFile}
echo -e '    cat ${ltarname}*${splitSuffix} >> ${ltarname}' >> ${mergeShFile}
echo '    echo "正在合并分割压缩包${ltarname},完成.exitCode[$?]"' >> ${mergeShFile}
echo '    _checkMd5File ${ltarname}.md5sum' >> ${mergeShFile}
echo '}' >> ${mergeShFile}
echo '' >> ${mergeShFile}
echo 'function _clearTarFile(){' >> ${mergeShFile}
echo '    local ltarname=$(ls |head -1|awk -F "_00" "{print $1}")' >> ${mergeShFile}
echo '    if [[ -f ${ltarname} ]]; then' >> ${mergeShFile}
echo '        echo "正在删除旧文件[${ltarname}].."' >> ${mergeShFile}
echo '        rm -rf ${ltarname}' >> ${mergeShFile}
echo '        echo "完成删除旧文件! exitCode: $?,"' >> ${mergeShFile}
echo '    fi' >> ${mergeShFile}
echo '}' >> ${mergeShFile}
echo '' >> ${mergeShFile}
echo '_mergeTarFile' >> ${mergeShFile}
chmod +x ${mergeShFile}
}

# ----↓↓↓↓↓----start----↓↓↓↓↓----该方法需要通过列编辑的方式,进行echo生成, 这是待生成源码----↓↓↓↓↓----start----↓↓↓↓↓----

function _checkMd5File(){
    local checkfile=$1
    echo "正在校验生成分割文件的md5校验值..."
    checkResult=$(md5sum --quiet -c ${checkfile})
    exitcode=$?
    if [[ ${exitcode} != "0" ]]; then
        echo "${checkResult} "
        echo "md5校验不匹配."
        return ${exitcode}
    fi
    echo "完成校验生成分割文件的md5校验值..."
}

function _mergeTarFile(){
    _checkMd5File splitFile.md5sum
    checkResult=$?
#    TODO suffix这里生成需要由build的变量定义.暂时写死
    local splitSuffix="_split"
    if [[ ${checkResult} != "0" ]]; then
        exit ${exitcode}
    fi
    local ltarname=$(ls |head -1|awk -F "_00" '{print $1}')
    echo "正在合并分割压缩包${ltarname}"
    cat ${ltarname}*${splitSuffix} >> ${ltarname}
    echo "正在合并分割压缩包${ltarname},完成.exitCode[$?]"
    _checkMd5File ${ltarname}.md5sum
}

function _clearTarFile(){
    local ltarname=$(ls |head -1|awk -F "_00" "{print $1}")
    if [[ -f ${ltarname} ]]; then
        echo "正在删除旧文件[${ltarname}].."
        rm -rf ${ltarname}
        echo "完成删除旧文件! exitCode: $?,"
    fi
}


# ----↑↑↑↑↑----end------↑↑↑↑↑----该方法需要通过列编辑的方式,进行echo生成----↑↑↑↑↑----end------↑↑↑↑↑----





function init(){
     if [[ ! -d ${buildDir} ]]; then
         mkdir ${buildDir}
     fi
     buildContextPath=$(cd ${buildDir} && pwd)
}
case $1 in
debug)
    genresu=$(_genMerageSh .)
    echo $genresu
   ;;
mvnp)
init
mvnp
   ;;
package)
init
package
   ;;
split)
init
splittar
   ;;
merge)
init
mergeTar
   ;;
clean)
init
clean
   ;;
    debug)
    init
    debug
    ;;
*)
    init
    clean
    mvnp
    package
;;

esac
