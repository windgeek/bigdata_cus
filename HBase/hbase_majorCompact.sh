#!/bin/bash

date  "+%Y-%m-%d %H:%M:%S"
echo '============================================='


su - hbase -c "hbase shell" << EOF 
        major_compact 'k_media:ntc_oss_small_file' 
EOF


echo '============================================='
date  "+%Y-%m-%d %H:%M:%S"

