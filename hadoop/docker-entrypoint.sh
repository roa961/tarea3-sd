#!/bin/bash
set -e
sudo service ssh start

if [ ! -d "/tmp/hadoop-hduser/dfs/name" ]; then
        $HADOOP_HOME/bin/hdfs namenode -format && echo "OK : HDFS namenode format operation finished successfully !"
fi

$HADOOP_HOME/sbin/start-dfs.sh

echo "YARNSTART = $YARNSTART"
if [[ -z $YARNSTART || $YARNSTART -ne 0 ]]; then
        echo "running start-yarn.sh"
        $HADOOP_HOME/sbin/start-yarn.sh
fi

$HADOOP_HOME/bin/hdfs dfs -mkdir -p /tmp
$HADOOP_HOME/bin/hdfs dfs -mkdir -p /users
$HADOOP_HOME/bin/hdfs dfs -mkdir -p /jars
$HADOOP_HOME/bin/hdfs dfs -chmod 777 /tmp
$HADOOP_HOME/bin/hdfs dfs -chmod 777 /users
$HADOOP_HOME/bin/hdfs dfs -chmod 777 /jars


$HADOOP_HOME/bin/hdfs dfsadmin -safemode leave
$HADOOP_HOME/bin/hdfs dfs -mkdir /user
$HADOOP_HOME/bin/hdfs dfs -mkdir /user/hduser
$HADOOP_HOME/bin/hdfs dfs -mkdir input	
$HADOOP_HOME/bin/hdfs dfs -chmod 777 /user
$HADOOP_HOME/bin/hdfs dfs -chmod 777 /user/hduser
$HADOOP_HOME/bin/hdfs dfs -chmod 777 input	

$HADOOP_HOME/bin/hdfs dfs -put /usr/local/bin/carpeta_1/*.txt input
$HADOOP_HOME/bin/hdfs dfs -put /usr/local/bin/carpeta_2/*.txt input
# keep the container running indefinitely
tail -f $HADOOP_HOME/logs/hadoop-*-namenode-*.log
