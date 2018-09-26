#!/bin/bash

notify=/usr/bin/notify-send

$notify "准备关机了。";

eventRootDir=/home/$(whoami)/autoshells
eventShellDir=$eventRootDir/shell.d


function stopall(){
	if [ -d ${eventShellDir} ];then

		for item in `ls ${eventShellDir}`;do
#        resu=1;
        itemfile="${eventShellDir}/${item}";
#        echo ${itemfile};
#		resu=$(${itemfile});
#        resu=$(mkdir asd);
        bash "${itemfile}";
        $notify "shutdownExec ${item},code:${?}";
		done



	fi

}

stopall;


