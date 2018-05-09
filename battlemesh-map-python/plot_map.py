#! /usr/bin/python

import networkx as nx
import matplotlib.pyplot as plt
import netdiff
import sys
import json

max_y = 370
max_x = 617


def plot_line(n1, n2, cost=0):
    x = [n1['x'], n2['x']]
    y = [n1['y'], n2['y']]
    print(x, y)
    if not cost:
        cost = 2
    ax.plot(x, y, linewidth=cost, color='firebrick')

position_map = {}

#3600
#position_map["fe80::ea94:f6ff:fef3:10ee"] = {'x':, 'y':}
#position_map["fe80::ea94:f6ff:fef2:f4ce"] = {'x':, 'y':}
#position_map["fe80::ea94:f6ff:fef3:1100"] = {'x':, 'y':}
#position_map["fe80::ea94:f6ff:fef3:114e"] = {'x':, 'y':}
#position_map["fe80::ea94:f6ff:fef3:fe9"] = {'x':, 'y':}
#position_map["fe80::ea94:f6ff:fef3:1145"] = {'x':, 'y':}
#position_map["fe80::ea94:f6ff:fef3:10f7"] = {'x':, 'y':}
#position_map["fe80::16cc:20ff:fe5e:c8ac"] = {'x':, 'y':}
position_map["fe80::16cc:20ff:fe5e:c88c"] = {'x': 118, 'y': 232}
position_map["fe80::16cc:20ff:fe5e:c7c3"] = {'x': 157, 'y': 264}
position_map["fe80::16cc:20ff:fe5e:c781"] = {'x': 250, 'y': 86}
position_map["fe80::16cc:20ff:fe5e:c802"] = {'x': 258, 'y': 138}

position_map["10.0.7.1"] = {'x': 118, 'y': 232}
position_map["10.0.5.1"] = {'x': 157, 'y': 264}
position_map["10.0.4.1"] = {'x': 250, 'y': 86}
position_map["10.0.6.1"] = {'x': 258, 'y': 138}
#4300
position_map["fe80::6670:2ff:fe3e:9d5f "] = {'x': 151, 'y': 209}
position_map["fe80::12fe:edff:fee5:f0c8"] = {'x': 145, 'y': 114}
position_map["fe80::12fe:edff:fee5:eef2"] = {'x': 198, 'y': 115}
position_map["fe80::12fe:edff:fee6:ad8 "] = {'x': 119, 'y': 48}
position_map["fe80::12fe:edff:fee6:ade "] = {'x': 325, 'y': 84}
position_map["fe80::a2f3:c1ff:fe74:83ce"] = {'x': 59,  'y': 228}
position_map["fe80::a2f3:c1ff:fe74:83cd"] = {'x': 231, 'y': 38}

position_map["10.0.2.1"] = {'x': 151, 'y': 209}
position_map["10.0..1"] = {'x': 145, 'y': 114}
position_map["10.0.1.1"] = {'x': 198, 'y': 115}
position_map["10.0.3.1"] = {'x': 119, 'y': 48}
position_map["10.0.13.1"] = {'x': 325, 'y': 84}
position_map["10.0.14.1"] = {'x': 59, 'y': 228}
position_map["10.0.15.1"] = {'x': 231, 'y': 38}
#position_map["fe80::12fe:edff:fee5:f0c8"] = {'x':151, 'y':209}
#position_map["fe80::12fe:edff:fee5:f0c8"] = {'x':151, 'y':209}
#position_map["fe80::12fe:edff:fee5:f0c6"] = {'x':, 'y':}
#position_map["fe80::12fe:edff:fee6:add"] = {'x':, 'y':}


img = plt.imread("map.png")
fig, ax = plt.subplots()
try:
    g = netdiff.NetJsonParser(file=sys.argv[1]).graph
except netdiff.exceptions.ParserError:
    # TODO: remove NetworkCollection tag when the netjson is a collection of networks
    exit

for link in g.edges(data=True):
    linklocal_left = g.node[link[0]]["router_addr"]
    linklocal_right = g.node[link[1]]["router_addr"]
    #print(linklocal_left in position_map, linklocal_right in position_map, linklocal_left, linklocal_right)
    if linklocal_left in position_map and linklocal_right in position_map:
        left = position_map[linklocal_left]
        right = position_map[linklocal_right]
        plot_line(left, right)
ax.imshow(img)
plt.show()
