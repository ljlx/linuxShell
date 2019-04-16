#!/bin/bash
####################################################
#
# File Name: killALL.sh
# Author: hx940929
# AuthorSite: https://www.thesunboy.com/
# Created Time: 2018年01月10日 星期三 20时51分11秒
###-----------------说明-------------------------###
#                                                   
####################################################
pname=$1
signal=$2
if [[ -z ${signal} ]]; then
    signal=15;

fi
#grep -v $0 过滤自身脚本.

pid=$(ps aux | grep $pname | grep -v grep |grep -v $0| awk '{print $2}' | xargs);

echo "使用kill -${signal} 来杀死。${pid}";
/bin/ps -p ${pid}
for item in ${pid[@]}; do
#    readarray -t pidlist
#    echo $(/bin/ps -p ${item})
    isright=1
    while true; do
        read -p "是否结束进程[${item}]? default:Y (Y/N): " isdelete
        if [[ ${isdelete} == "y" || ${isdelete} == "Y" ]]; then
            echo "结束进程(kill -${signal} $item)"
            kill -${signal} ${item}
            break
        elif [[ ${isdelete} == "n" || ${isdelete} == "N" ]]; then
#            echo "跳过进程:${item}"
            break
        else
            # 非法输入
            echo "确认结束请按Y(y) ,否则N(n)"
    fi
    done
done

#xargs
#kill -${signal} ${pid}






function setconf() {
    local i=1

    for element in "$@"
    do
        IFS=':', read -ra array <<< "$element"
        if [[ "${array[0]}" = "infile" ]]; then
            local input=${array[1]}
            continue
        elif [[ "${array[0]}" = "outfile" ]]; then
            local output=${array[1]}
            continue
        fi
        para[$i]="-e s#${array[0]}#${array[1]}#g "
        para+=${para[$i]}
        i=$(($i + 1))
    done
    if [[ -n "$output" ]]; then
        cp $output ${output}.org
        sed $para $input > $output
    else
        echo "ss"
        echo $array
#        cp $input ${input}.org
#        sed -i $para $input
    fi

    read -p "asdfasdf" asdf
    echo $asdf
}

