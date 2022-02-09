#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by wind on 12/18/20


from pyspark import SparkConf, SparkContext
from pyspark.sql import HiveContext


def spark_query(sparksql):
        conf = SparkConf().setMaster("yarn-client").setAppName("My App").set("user.name", "dp")
        sc = SparkContext(conf = conf)
        hive_context = HiveContext(sc)
        # hive_context.sql('select * from td_warehouse.advertiser_cvt').show()
        hive_context.sql(sparksql).show


if __name__ == '__main__':
        spark_query("msck repair table dairy_ftp.yy_user")

