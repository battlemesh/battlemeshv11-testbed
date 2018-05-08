#! /usr/bin/python

import networkx as nx
import matplotlib.pyplot as plt

max_y = 370
max_x = 617

def plot_line(n1, n2):
    x = [n1['x'], n2['x']]
    y = [n1['y'], n2['y']]
    ax.plot(x , y , linewidth=2, color='firebrick')

position_map = {}
#3600
#position_map["fe80::ea94:f6ff:fef3:10ee"] = {'x':, 'y':}
#position_map["fe80::ea94:f6ff:fef2:f4ce"] = {'x':, 'y':}
#position_map["fe80::ea94:f6ff:fef3:1100"] = {'x':, 'y':}
#position_map["fe80::ea94:f6ff:fef3:114e"] = {'x':, 'y':}
#position_map["fe80::ea94:f6ff:fef3:fe9"] = {'x':, 'y':}
#position_map["fe80::ea94:f6ff:fef3:1145"] = {'x':, 'y':}
#position_map["fe80::ea94:f6ff:fef3:10f7"] = {'x':, 'y':}
position_map["fe80::16cc:20ff:fe5e:c88b"] = {'x':118, 'y':232}
position_map["fe80::16cc:20ff:fe5e:c7c2"] = {'x':157, 'y':264}
#position_map["fe80::16cc:20ff:fe5e:c8ac"] = {'x':, 'y':}
position_map["fe80::16cc:20ff:fe5e:c780"] = {'x':250, 'y':86}
position_map["fe80::16cc:20ff:fe5e:c801"] = {'x':258, 'y':138}
#4300
position_map["fe80::6670:2ff:fe3e:9d5f"] = {'x':145, 'y':114}
position_map["fe80::12fe:edff:fee5:eef1"] = {'x':198, 'y':115}
#position_map["fe80::12fe:edff:fee6:add"] = {'x':, 'y':}
position_map["fe80::12fe:edff:fee6:ad7"] = {'x':119, 'y':48}
position_map["fe80::12fe:edff:fee5:f0c6"] = {'x':151, 'y':209}
#position_map["fe80::12fe:edff:fee5:f0c6"] = {'x':, 'y':}
position_map["fe80::12fe:edff:fee6:adc"] = {'x':325, 'y':84}
position_map["fe80::a2f3:c1ff:fe74:83cc"] = {'x':59, 'y':228}
position_map["fe80::a2f3:c1ff:fe74:83cd"] = {'x':231, 'y':38}


img = plt.imread("map.png")
fig, ax = plt.subplots()
ax.imshow(img)
for i in position_map.values():
    for k in position_map.values():
        plot_line(i, k)
plt.show()
