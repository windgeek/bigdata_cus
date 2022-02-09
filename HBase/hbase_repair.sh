#!/bin/bash
su - hbase <<EOF
hbase hbck -fixMeta -fixAssignments
hbase hbck -repair
hbase hbck -fixEmptyMetaCells
hbase hbck
EOF
