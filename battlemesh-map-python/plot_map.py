#! /usr/bin/python

import networkx as nx
import matplotlib.pyplot as plt
import netdiff
import sys
import json
import os
import re


def parse_bitrate(btr):
    number = float(re.findall("^[0-9]*\.?[0-9]*", btr)[0])
    scale = re.findall("Mbit|Kbit|bit|Gbit", btr)[0]
    if scale == "Kbit":
        number = number/1000
    elif scale == "bit":
        number = number/1000000
    elif scale == "Gbit":
        number = number*1000
    return number


def plot_line(n1, n2, left_id, right_id, cost=0, def_lw=5):
    x = [n1['x'], n2['x']]
    y = [n1['y'], n2['y']]
    if left_id not in plotted_nodes:
        plotted_nodes.add(left_id)
    if right_id not in plotted_nodes:
        plotted_nodes.add(right_id)
    if left_id+right_id not in plotted_links:
        if cost:
            lw = def_lw*cost/200 + 2
            #ax.text((x[0]+x[1])/2, (y[0]+y[1])/2, cost, fontsize=15)
        plotted_links.add(left_id+right_id)
        ax.text(x[1], y[1], right_id, fontsize=15)
        ax.text(x[0], y[0], left_id, fontsize=15)
        ax.plot(x, y, linewidth=lw, color='firebrick')


max_y = 370
max_x = 617
topo_file = "/tmp/map.json"
if len(sys.argv) > 2:
    topo_file = sys.argv[2]
else:
    os.system('echo "/netjsoninfo filter graph ipv4_0" | nc %s  2009  > '%(sys.argv[1])
              + topo_file)

plotted_nodes = set()
plotted_links = set()
def_width = 2

position_map = {}

position_map["10.0.7.1"] = {'x': 118, 'y': 232}
position_map["10.0.5.1"] = {'x': 157, 'y': 264}
position_map["10.0.4.1"] = {'x': 250, 'y': 86}
position_map["10.0.6.1"] = {'x': 258, 'y': 138}
position_map["10.0.2.2"] = {'x': 145, 'y': 114}
position_map["10.0.2.1"] = {'x': 145, 'y': 114}
position_map["10.0.8.1"] ={'x': 110, 'y': 160} 
position_map["10.0.1.1"] = {'x': 198, 'y': 115}
position_map["10.0.3.1"] = {'x': 119, 'y': 48}
position_map["10.0.13.1"] = {'x': 325, 'y': 84}
position_map["10.0.14.1"] = {'x': 59, 'y': 228}
position_map["10.0.15.1"] = {'x': 231, 'y': 38}
position_map["10.0.18.1"] = {'x': 50, 'y': 60}
position_map["10.0.23.1"] = {'x': 300, 'y': 210}


img = plt.imread("map.png")
fig, ax = plt.subplots()
try:
    ng = netdiff.NetJsonParser(file=topo_file)
    g = ng.graph
except netdiff.exceptions.ParserError:
    # TODO: remove NetworkCollection tag when the netjson is a collection of networks
    exit

new_g = nx.Graph()

for link in g.edges(data=True):
    if link[2]["type"] not in ["node", "local"]:
        continue
    #linklocal_left = g.node[link[0]]["router_addr"]
    #linklocal_right = g.node[link[1]]["router_addr"]
    #print(linklocal_left in position_map, linklocal_right in position_map, linklocal_left, linklocal_right)
    ip_left = link[0][3:]
    ip_right = link[1][3:]
    if ip_left in position_map and ip_right in position_map:
        try:
            cost = link[2]['in_text']
            olsr_cost = link[2]['in_cost']
        except Exception:
            pass
        cost = parse_bitrate(cost)
        new_g.add_edge(ip_left, ip_right, weight=cost, cost=olsr_cost)
        left = position_map[ip_left]
        right = position_map[ip_right]
        left_id = ip_left.split(".")[2]
        right_id = ip_right.split(".")[2]
        plot_line(left, right, left_id, right_id, cost=cost)
ax.imshow(img)
plt.savefig("/tmp/map.png")
plt.show()
nx.write_graphml(new_g, "/tmp/graph.graphml")
