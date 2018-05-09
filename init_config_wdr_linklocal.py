#!/env/python3
import os
import sys

interface = "%eth0"
with open(sys.argv[1]) as f:
    ip_list = f.read().split('\n')

print ip_list
for i in range(16, 41):
    mgmt_ip = "192.168.254.%d" % (i)
    ll_ip = ip_list[i-16]
    os.system("scp -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null config-wdr/%s/* root@[%s]:/etc/config/" % (mgmt_ip, ll_ip))
    #print("scp -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null config-wdr/%s/network root@%s:/etc/config/" % (mgmt_ip, ll_ip))
