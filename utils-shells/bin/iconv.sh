#!/bin/bash
cd /home/hanxu/ideaProject/jx_yc/脚本/脚本1.1/业务库/

rm -rf ./test/iconv_tmp
mkdir -p ./test/iconv_tmp
cp ./*.sql ./test/
cd ./test/
for item in $(ls *.sql)
do
    echo ${item}
    fileEncode=$(file -i ${item} | awk -F = '{print $2}')
    if [[ ! ${fileEncode} -eq 'UTF-8' ]]; then
        $(which iconv) -f GBK -t UTF-8 ${item} -o ./iconv_tmp/${item}
        else
        cp ${item} ./iconv_tmp/${item}
    fi

done;