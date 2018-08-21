#!/bin/bash
baseDir=/home/hanxu/ideaProject/chaozou/ggfw
#baseDir=$(pwd);
packageWar=(commons pbs ebus bag)
targetDir=~/Desktop/

package(){

    for item in ${packageWar[@]}
    do
        cd $baseDir/$item/ && mvn clean package install -Dmaven.test.skip=true && cd ../ || cd ../
    done
    return 0;
}

mvtar(){
find $baseDir -type f  -name "*.war" | xargs -I {} mv {} ./target
return $?
}

yasuo(){
echo "yasuo:start>>"
	local backDir=$targetDir/targetBackup/
	tar -zcvf target.tar.gz ./target
	echo "yasuo:end<<";
	local datename=$(date "+%m-%d-%H%M%S")
if [ ! -d $backDir ];then
	mkdir $backDir
fi
	echo "yasuo:back old tar.>>";
	mv $targetDir/target*.tar.gz $backDir
	echo "yasuo:back old tar success <<";
	local tarname=target"$datename".tar.gz

	cp target.tar.gz $targetDir/$tarname
	echo "yasuo: copy target.tar.gz to $tarname success";
}
deltarget(){
if [ -f $baseDir/target.tar.gz ]; then
	rm -rf $baseDir/target.tar.gz
fi
if [ -d $baseDir/target ]; then
	rm -rf $baseDir/target/*.war
	else
	mkdir target
fi

}
all(){
    startTime=$(date +%s)
    deltarget;
    package;
    mvtar;
    yasuo;
    deltarget;
    endTime=$(date +%s)
    echo "总耗时: $(( $endTime - $startTime )) 秒"
}

case $* in
all)
   time all;
;;
package)
    package;
   ;;
   mv)
	   mvtar;
   ;;
tar)
	yasuo;	
    ;;
delwar)
    deltarget;
    ;;
*)

	 time all;

	;;
esac
