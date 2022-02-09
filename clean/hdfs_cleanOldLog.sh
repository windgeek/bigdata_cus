#!/bin/sh
source /etc/profile
find /var/log/hadoop/hdfs -mtime +180 -type f -exec rm -rf {}  \;
