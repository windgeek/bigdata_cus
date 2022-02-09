#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by wind on 2019-12-03

import os
esAlert = os.popen('curl -s http://$HOSTNAME:9200/_cat/health?v')
resultProcess = esAlert.read()
esStatus = resultProcess.split()[17]
esAlert.close()
if esStatus == "green":
    print(0)
else:
    print(1)
