#!/usr/bin/ bash
pwd
. ../aliasAndEnv/bash_env/maven.env.sh
maven=/media/hanxu/e/Maven/MavenBin
maven_resp=${maven}/../repository
mavenHome=${M2_HOME}
respHome=${M2_RESP}
echo "maven环境变量${mavenHome}"
echo "仓库环境变量,${respHome}"
echo "仓库变量,${maven_resp}"
mkdir /home/hanxu/.m2
ln -s ${maven} ${mavenHome}
ln -s ${maven_resp} ${respHome}