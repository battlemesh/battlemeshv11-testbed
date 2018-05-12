#!/bin/python3
import json
import os
from netdiff import NetJsonParser
import networkx as nx
import time

destination = "192.168.254.3"

data = os.popen('echo "/netjsoninfo filter graph ipv4_0" | nc %s 2009' % (destination)).read()
json = json.loads(data)
graph = NetJsonParser(data=data).graph.to_undirected()
graph2 = nx.Graph()
networks = []

for link in graph.edges(data=True):
    if link[2]["type"] not in ["node", "local"]:
        networks.append(link[1])
for net in networks:
    graph.remove_node(net)    
cp = nx.articulation_points(graph)
cent = nx.betweenness_centrality(graph, endpoints=True, weight='cost')
for x in list(cp):
    del(cent[x])
sorted(cent, key=cent.__getitem__)

print(cent)

node = list(cent.keys())[0]
node_ip = node[3:]
print("%s: killing node: %s with centrality %f" % (time.time(), node_ip, cent[node]))

os.system('ssh root@%s "killall olsrd2 && killall exe"' % (node_ip))
