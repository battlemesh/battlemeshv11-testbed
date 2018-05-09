#!/env/python3
import os
with open("config-wdr/network.template", "r") as f_temp:
    template = f_temp.read()
    for i in range(12, 21):
        mgmt_ip = "192.168.254.%d" % (i)
        lan_ip = "10.1.%d.1" % (i)
        radio_ip = "10.0.%d.1" % (i)
        print(mgmt_ip)
        if not os.path.exists("config-wdr/" + mgmt_ip):
            os.makedirs("config-wdr/" + mgmt_ip)
        os.system("cp config-wdr/dhcp config-wdr/%s/dhcp" % (mgmt_ip))
        os.system("cp config-wdr/olsrd2 config-wdr/%s/olsrd2" % (mgmt_ip))
        os.system("cp config-wdr/wireless config-wdr/%s/wireless" % (mgmt_ip))


        with open("config-wdr/%s/network" % (mgmt_ip), "w") as f:
            config = template.format(lan_ip, radio_ip, mgmt_ip)
            f.write(config)
            
    
