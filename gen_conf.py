#!/env/python3
import os

controller = 2
nodes_n = 30
with open("config-wdr/network.template", "r") as f_temp:
    template = f_temp.read()
    with open("config-wdr/olsrd2.template", "r") as f_olsr:
        olsr2_template = f_olsr.read()
        with open("config-wdr/bmx7.template", "r") as f_bmx7:
            bmx7_template = f_bmx7.read()
            for i in range(1, nodes_n + 1):
                mgmt_ip = "192.168.254.%d" % (i)
                lan_ip = "10.1.%d.1" % (i)
                radio_ip = "10.0.%d.1" % (i)
                hna = "10.1.%d.0/24" % (i)
                ip6 = "fc00:%d::1/128" % (i)
                ip6_net = "fc00:%d::/64" % (i)
                print(hna)
                if not os.path.exists("config-wdr/" + mgmt_ip):
                    os.makedirs("config-wdr/" + mgmt_ip)
                if(i == controller):
                    # special case for controller node
                    os.system("cp config-wdr/controller/* config-wdr/%s/" % (mgmt_ip))
                else:
                    os.system("cp config-wdr/dhcp config-wdr/%s/dhcp" % (mgmt_ip))
                    os.system("cp config-wdr/wireless config-wdr/%s/wireless" % (mgmt_ip))
                    with open("config-wdr/%s/olsrd2" % (mgmt_ip), "w") as f:
                        config = olsr2_template.format(hna)
                        f.write(config)
                    with open("config-wdr/%s/bmx7" % (mgmt_ip), "w") as f:
                        config = bmx7_template.format(ip6_net, lan_ip + "/24", hna)
                        f.write(config)
                    with open("config-wdr/%s/network" % (mgmt_ip), "w") as f:
                        config = template.format(radio_ip, ip6, lan_ip, mgmt_ip)
                        f.write(config)
