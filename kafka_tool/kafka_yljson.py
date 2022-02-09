#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by wind on 2021/5/10

import subprocess
import random
import json

def cmdout(cmd):
    try:
        out_text = subprocess.check_output(cmd, shell=True).decode('utf-8')
        out_text = int(out_text)
    except subprocess.CalledProcessError as e:
        out_text = e.output.decode('utf-8')
        code = e.returncode
    return out_text

def ge_json():
    l, t = [], []
    for i in range(0, 100):
        cmd = "./bin/kafka-topics.sh --describe --zookeeper 192.168.146.70:2181/kafka_new --topic __consumer_offsets | grep -w {} | awk '{{print $6}}'".format(
            i)
        print(cmdout(cmd))
        l1 = l.append(cmdout(cmd))
        t_json = {
            "topic": "__consumer_offsets",
            "partition": i,
            "replicas": l1
        }
        t.append(t_json)
    d = {"version": 1, "partitions": t}
    print(d)


def gen_json():
    t = []
    # luse = []
    with open('./ge.txt', 'r') as f:
        for line in f:
            l = []
            node = [145222, 145223, 145224, 145225, 145226, 145227, 145216, 145217, 145218, 145221, 145222, 145223, 145224, 145225, 145226, 145227, 145216, 145217, 145218, 145221, 145222, 145223, 145224, 145225, 145226, 145227, 145216, 145217, 145218, 145221, 145222, 145223, 145224, 145225, 145226, 145227, 145216, 145217, 145218, 145221, 145222, 145223, 145224, 145225, 145226, 145227, 145216, 145217, 145218, 145221, 145222, 145223, 145224, 145225, 145226, 145227, 145216, 145217, 145218, 145221, 145222, 145223, 145224, 145225, 145226, 145227, 145216, 145217, 145218, 145221, 145222, 145223, 145224, 145225, 145226, 145227, 145216, 145217, 145218, 145221, 145222, 145223, 145224, 145225, 145226, 145227, 145216, 145217, 145218, 145221, 145222, 145223, 145224, 145225, 145226, 145227, 145216, 145217, 145218, 145221]
            nodes = list(set(node))
            new = [145198, 145199, 145228, 145229]
            nodes.extend(new)
            a = line.split()
            b = int(a[1].strip())
            c = int(a[3].strip())
            print(c)
            nodes.remove(c)
            print(nodes)
            r = random.sample(nodes, 2)
            print(r)
            l.append(c)
            l.extend(r)
            # luse.append(c)
            t_json = {
                "topic": "__consumer_offsets",
                "partition": b,
                "replicas": l
            }
            t.append(t_json)
            d = {"version": 1, "partitions": t}
        # print(luse)
        print(json.dumps(d))

if __name__ == '__main__':
    gen_json()
