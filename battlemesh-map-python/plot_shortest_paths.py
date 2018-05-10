#!/usr/bin/python

import networkx as nx
import sys
from collections import defaultdict
import matplotlib.pyplot as plt


if len(sys.argv) < 2:
    topo_file = "/tmp/graph.graphml"
else:
    topo_file = sys.argv[1]

g = nx.read_graphml(topo_file)

#for edge in g.edges(data=True):
#    weight = 1/edge[2]['weight']
#    g.edge[edge[0]][edge[1]]['weight'] = weight

path_weight = defaultdict(dict)
path_bw = defaultdict(dict)
path_dist = defaultdict(dict)
for n in g.nodes():
    paths = nx.dijkstra_predecessor_and_distance(g, n, weight='cost')[1]
    for d, c in paths.items():
        path_weight[n][d] = c
    paths = nx.single_source_dijkstra_path(g, n, weight='cost')
    for d, p in paths.items():
        if d == n:
            continue
        path_dist[n][d] = len(p)-1
        path_bandwidth = []
        ph = p[0]
        for nh in p[1:]:
            print g.edge[ph]
            link_cost = g.edge[ph][nh]['weight']
            ph = nh
            path_bandwidth.append(link_cost)
        path_bw[n][d] = min(path_bandwidth)


endpoints = []
for s in path_dist:
    for d in path_dist[s]:
        endpoints.append([(s, d), path_dist[s][d]])

w = []
di = []
b = []
labels = []
for (ep, d) in sorted(endpoints, key=lambda x: x[1]):
    print ep[0] + ":" + ep[1], d, path_weight[ep[0]][ep[1]], path_bw[ep[0]][ep[1]] 
    labels.append(ep[0] + ":" + ep[1])
    w.append(path_weight[ep[0]][ep[1]])
    di.append(d)
    b.append(path_bw[ep[0]][ep[1]])

x = range(len(w))
fig, ax1 = plt.subplots()
p_h = ax1.plot(x, di, 'r', label="hopcount",)
ax1.set_xlabel('path')
ax1.set_ylabel('hop count')
ax2 = ax1.twinx()
p_b = ax2.plot(x, b, 'b' ,label="Bandwidth")
ax2.set_ylabel('Mbps')
#ax1.plot(x, w, label="OLSR weight")
ax1.legend(p_h + p_b, [l.get_label() for l in p_h + p_b ], loc=1)
plt.title("Shortest paths length and bandwidth")
plt.show()
