#/bin/bash

baseDir='/media/ubuntu/2ee8572e-22d5-4eee-b098-ba447ddcb6bd/timeshift/';
choseDir='snapshots-boot/2018-07-17_13-29-53/';
workDir='/media/ubuntu/1cc8a442-917f-4a38-8b4c-05d254395772';
dtarget=(bin boot etc lib lib32 lib64 opt run sbin srv usr var);

delete(){
	for item in ${dtarget[@]}
	do
		rm -rf ${workDir}/${item}/
	done

}

copy(){
	for item in ${dtarget[@]}
	do
		cp -R ${baseDir}${choseDir}localhost/${item} ${workDir}/
	done

}

tar(){
	cd ${workDir}/
	for item in ${dtarget[@]}
	do
	#	cp -R ${baseDir}${choseDir}localhost/${item} ${workDir}/
	echo "tar >> ${workDir}/${item}"
	
	/bin/tar -zxvf ${workDir}/${item}.tar.gz  
	echo "tar finish ${item}>> $?"
	done

}

case $* in
delete)
	delete;
;;
copy)
	copy;
;;
tar)
	tar;
;;



esac
