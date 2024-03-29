#!/bin/bash 

echo "Stop all services in Ambari or kill them. In my case, Ambari damaged his database during downgrade and could not start. So I manually killed all the processes on all nodes"
killall -u hdfs
killall -u zookeeper
killall -u hbase
killall -u spark
killall -u spark2
echo "Run python script on all cluster nodes"
python /usr/lib/python2.6/site-packages/ambari_agent/HostCleanup.py --silent --skip=users

echo "Remove Hadoop packages on all nodes"
yum remove hive\* -y
yum remove oozie\* -y
yum remove pig\* -y
yum remove zookeeper\* -y
yum remove tez\* -y
yum remove hbase\* -y
yum remove ranger\* -y
yum remove knox\* -y
yum remove storm\* -y
yum remove accumulo\* -y
yum remove falcon\* -y
yum remove ambari-metrics-hadoop-sink  -y
yum remove smartsense-hst -y
yum remove slider_2_4_2_0_258 -y
yum remove ambari-metrics-monitor -y
yum remove spark2_2_5_3_0_37-yarn-shuffle -y
yum remove spark_2_5_3_0_37-yarn-shuffle -y
yum remove ambari-infra-solr-client -y

echo "Remove ambari-server (on ambari host) and ambari-agent (on all nodes)"
ambari-server stop      #not,ignore
ambari-agent stop
yum erase ambari-server #not,ignore
yum erase ambari-agent

echo "Remove repositories on all nodes"
rm -rf /etc/yum.repos.d/ambari.repo /etc/yum.repos.d/HDP*
yum clean all

echo "Remove log folders on all nodes"
rm -rf /var/log/ambari-agent
rm -rf /var/log/ambari-metrics-grafana
rm -rf /var/log/ambari-metrics-monitor
rm -rf /var/log/ambari-server/
rm -rf /var/log/falcon
rm -rf /var/log/flume
rm -rf /var/log/hadoop
rm -rf /var/log/hadoop-mapreduce
rm -rf /var/log/hadoop-yarn
rm -rf /var/log/hive
rm -rf /var/log/hive-hcatalog
rm -rf /var/log/hive2
rm -rf /var/log/hst
rm -rf /var/log/knox
rm -rf /var/log/oozie
rm -rf /var/log/solr
rm -rf /var/log/zookeeper

echo "Remove Hadoop folders including HDFS data on all nodes"
rm -rf /hadoop/*
rm -rf /hdfs/hadoop
rm -rf /hdfs/lost+found
rm -rf /hdfs/var
rm -rf /local/opt/hadoop
rm -rf /tmp/hadoop
rm -rf /usr/bin/hadoop
rm -rf /usr/hdp
rm -rf /var/hadoop
for i in {1..12}; do rm -rf /data$i/hadoop; done

echo "Remove config folders on all nodes"
rm -rf /etc/ambari-agent
rm -rf /etc/ambari-metrics-grafana
rm -rf /etc/ambari-server
rm -rf /etc/ams-hbase
rm -rf /etc/falcon
rm -rf /etc/flume
rm -rf /etc/hadoop
rm -rf /etc/hadoop-httpfs
rm -rf /etc/hbase
rm -rf /etc/hive 
rm -rf /etc/hive-hcatalog
rm -rf /etc/hive-webhcat
rm -rf /etc/hive2
rm -rf /etc/hst
rm -rf /etc/knox 
rm -rf /etc/livy
rm -rf /etc/mahout 
rm -rf /etc/oozie
rm -rf /etc/phoenix
rm -rf /etc/pig 
rm -rf /etc/ranger-admin
rm -rf /etc/ranger-usersync
rm -rf /etc/spark2
rm -rf /etc/tez
rm -rf /etc/tez_hive2
rm -rf /etc/zookeeper

echo "Remove PIDs on all nodes"
rm -rf /var/run/ambari-agent
rm -rf /var/run/ambari-metrics-grafana
rm -rf /var/run/ambari-server
rm -rf /var/run/falcon
rm -rf /var/run/flume
rm -rf /var/run/hadoop 
rm -rf /var/run/hadoop-mapreduce
rm -rf /var/run/hadoop-yarn
rm -rf /var/run/hbase
rm -rf /var/run/hive
rm -rf /var/run/hive-hcatalog
rm -rf /var/run/hive2
rm -rf /var/run/hst
rm -rf /var/run/knox
rm -rf /var/run/oozie 
rm -rf /var/run/webhcat
rm -rf /var/run/zookeeper

echo "Remove library folders on all nodes"
rm -rf /usr/lib/ambari-agent
rm -rf /usr/lib/ambari-infra-solr-client
rm -rf /usr/lib/ambari-metrics-hadoop-sink
rm -rf /usr/lib/ambari-metrics-kafka-sink
rm -rf /usr/lib/ambari-server-backups
rm -rf /usr/lib/ams-hbase
rm -rf /usr/lib/mysql
rm -rf /var/lib/ambari-agent
rm -rf /var/lib/ambari-metrics-grafana
rm -rf /var/lib/ambari-server
rm -rf /var/lib/flume
rm -rf /var/lib/hadoop-hdfs
rm -rf /var/lib/hadoop-mapreduce
rm -rf /var/lib/hadoop-yarn 
rm -rf /var/lib/hive2
rm -rf /var/lib/knox
rm -rf /var/lib/smartsense
rm -rf /var/lib/storm

echo "Clean folder /var/tmp/* on all nodes"
rm -rf /var/tmp/*

#Delete HST from cron on all nodes (no ignore)
#0 * * * * /usr/hdp/share/hst/bin/hst-scheduled-capture.sh sync
#0 2 * * 0 /usr/hdp/share/hst/bin/hst-scheduled-capture.sh
#Remove databases. I remove the instances of MySQL and Postgres so that Ambari installed and configured fresh databases.
#yum remove mysql mysql-server
#yum erase postgresql
#rm -rf /var/lib/pgsql
#rm -rf /var/lib/mysql

echo "Remove symlinks on all nodes. Especially check folders /usr/sbin and /usr/lib/python2.6/site-packages"
cd /usr/bin
rm -rf accumulo
rm -rf atlas-start
rm -rf atlas-stop
rm -rf beeline
rm -rf falcon
rm -rf flume-ng
rm -rf hbase
rm -rf hcat
rm -rf hdfs
rm -rf hive
rm -rf hiveserver2
rm -rf kafka
rm -rf mahout
rm -rf mapred
rm -rf oozie
rm -rf oozied.sh
rm -rf phoenix-psql
rm -rf phoenix-queryserver
rm -rf phoenix-sqlline
rm -rf phoenix-sqlline-thin
rm -rf pig
rm -rf python-wrap
rm -rf ranger-admin
rm -rf ranger-admin-start
rm -rf ranger-admin-stop
rm -rf ranger-kms
rm -rf ranger-usersync
rm -rf ranger-usersync-start
rm -rf ranger-usersync-stop
rm -rf slider
rm -rf sqoop
rm -rf sqoop-codegen
rm -rf sqoop-create-hive-table
rm -rf sqoop-eval
rm -rf sqoop-export
rm -rf sqoop-help
rm -rf sqoop-import
rm -rf sqoop-import-all-tables
rm -rf sqoop-job
rm -rf sqoop-list-databases
rm -rf sqoop-list-tables
rm -rf sqoop-merge
rm -rf sqoop-metastore
rm -rf sqoop-version
rm -rf storm
rm -rf storm-slider
rm -rf worker-lanucher
rm -rf yarn
rm -rf zookeeper-client
rm -rf zookeeper-server
rm -rf zookeeper-server-cleanup

echo "Remove service users on all nodes"
userdel -r accumulo
userdel -r ambari-qa
userdel -r ams
userdel -r falcon
userdel -r flume
userdel -r hbase
userdel -r hcat
userdel -r hdfs
userdel -r hive
userdel -r kafka
userdel -r knox
userdel -r mapred
userdel -r oozie
userdel -r ranger
userdel -r spark
userdel -r sqoop
userdel -r storm
userdel -r tez
userdel -r yarn
userdel -r zeppelin
userdel -r zookeeper

echo "Run find / -name ** on all nodes. You will definitely find several more files/folders. Remove them."
find / -name *ambari*
find / -name *accumulo*
find / -name *atlas*
find / -name *beeline*
find / -name *falcon*
find / -name *flume*
find / -name *hadoop*
find / -name *hbase*
find / -name *hcat*
find / -name *hdfs*
find / -name *hdp*
find / -name *hive*
find / -name *hiveserver2*
find / -name *kafka*
find / -name *mahout*
find / -name *mapred*
find / -name *oozie*
find / -name *phoenix*
find / -name *pig*
find / -name *ranger*
find / -name *slider*
find / -name *sqoop*
find / -name *storm*
find / -name *yarn*
find / -name *zookeeper*

#Reboot all nodes
#reboot
