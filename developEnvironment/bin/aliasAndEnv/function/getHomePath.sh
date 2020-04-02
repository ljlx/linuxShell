#!/usr/bin/bash
function _getHomePath(){
curuser=$(whoami);
    if [[ ! -z "${curuser}" && "${curuser}" == "root" ]]; then
        authDir="/root/"
    else
        authDir="/home/${curuser}/"
    fi
    echo ${authDir}
    return $?;
}
