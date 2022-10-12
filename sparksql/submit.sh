#!/usr/bin/env bash

spark-submit \
--master yarn-client \
--queue online \
--executor-memory 4G \
--num-executors 2 \
--executor-cores 2 \
--conf spark.default.parallelism=200 \
sparksql.py
