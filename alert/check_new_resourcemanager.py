#!/usr/bin/python2.7

import  urllib2
import  json
import  sys


rmnodes = ['192.168.xx.xx','192.168.xx.xx']

num_rmnode=166
offset=2
rmnode_num=166
STATE_OK=0
STATE_WARNING=1
STATE_CRITICAL=2
STATE_UNKNOWN=3

#################get cluster status

rmnode_con = {}
rmnode_page_error = ''
rmnode_status = {}

for c in rmnodes:
    url_rmnode = 'http://%s:8088/ws/v1/cluster/info'%c
#    print url_rmnode

    try:
        rmnode_con['%s'%c] = urllib2.urlopen(url_rmnode).read()
    except:
        rmnode_page_error += '%s '%c


if rmnode_page_error:
    for c in rmnodes:
        if c not in rmnode_page_error:
            rmnode_page_error += '(%s is OK)'%c

    print 'CRITICAL! Can not get %s information.'%rmnode_page_error
    sys.exit(STATE_CRITICAL)

for cc in rmnode_con:
    cc_xml = json.loads(rmnode_con[cc])
    rmnode_status[cc] = cc_xml['clusterInfo']['haState']

#print rmnode_status
for i in rmnode_status:
#    print rmnode_status[i]
    if rmnode_status[i] == "ACTIVE":
         active = i
 #        print active
    elif rmnode_status[i] == "STANDBY":
         standby = i
  #       print standby

#################get nmnode status
    
url_nmnode = 'http://%s:8088/ws/v1/cluster/nodes'%active
#print url_nmnode

try:
    html_nmnode = urllib2.urlopen(url_nmnode).read()
except:
    print 'CRITICAL! Can not get nmnode information from %s.'%active
    sys.exit(STATE_CRITICAL)
    
html_nmnode_con = json.loads(html_nmnode)
nodes = html_nmnode_con['nodes']['node']

node_running = []
node_dead = []
node_deco = []
node_unknow = []

for node in nodes:
    if node['state'] == 'RUNNING':
        node_running.append(node['nodeHostName'])
    elif node['state'] == 'DECOMMISSIONED':
        node_deco.append(node['nodeHostName'])  
    elif node['state'] == 'DEAD':
        node_dead.append(node['nodeHostName'])
    else:
        node_unknow.append(node['nodeHostName'])

running_num = len(node_running)
deco_nodes = ','.join(node_deco)
dead_nodes = ','.join(node_dead)
unknow_nodes = ','.join(node_unknow)

#print running_num,deco_nodes,dead_nodes,unknow_nodes


if not deco_nodes:
    deco_nodes = '-'

if not dead_nodes:
    dead_nodes = '-'

if not unknow_nodes:
    unknow_nodes = '-'

#################result
    
node_active = '%s'%active
node_standby = '%s'%standby
#print node_active

active_status = rmnode_status[node_active]
standby_status = rmnode_status[node_standby]
#print active_status

if  running_num == rmnode_num and active_status == 'ACTIVE' and standby_status == 'STANDBY':    
    print "OK!%s/active; %s/standy <> %s/%s nodes running <> decommissioned_nodes are %s <> dead_nodes are %s <> lost_nodes are %s"%(node_active,node_standby,running_num,rmnode_num,deco_nodes,dead_nodes,unknow_nodes)
    sys.exit(STATE_OK)

elif rmnode_num - running_num <= offset and active_status == 'ACTIVE' and standby_status == 'STANDBY':
    print "WARNING!%s/active; %s/standy <> %s/%s nodes running <> decommissioned_nodes are %s <> dead_nodes are %s <> lost_nodes are %s"%(node_active,node_standby,running_num,rmnode_num,deco_nodes,dead_nodes,unknow_nodes)
    sys.exit(STATE_WARNING)

else:
    print "CRITICAL!%s/active; %s/standy <> %s/%s nodes running <> decommissioned_nodes are %s <> dead_nodes are %s <> lost_nodes are %s"%(node_active,node_standby,running_num,rmnode_num,deco_nodes,dead_nodes,unknow_nodes)
    sys.exit(STATE_CRITICAL)



