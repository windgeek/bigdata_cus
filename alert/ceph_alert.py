#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by wind on 2019-12-03

import os
CephAlert = os.popen('ceph -s')
resultProcess = CephAlert.read()
CephStatus = resultProcess.split()[4]
CephAlert.close()
if CephStatus == 'HEALTH_OK':
    print(0)
else:
    print(1)
