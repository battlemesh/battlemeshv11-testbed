#!/bin/bash

. ../test_script/ip_list.sh
. ../test_script/functions.sh


for ip in ${IPv4_mgmt[@]}; do
    data_dir="../data/bmx_crash_test_$ip"
    echo -n "gathering data from $ip ..."
    if check_if_up $ip; then
        mkdir -p $data_dir
        echo "OK"
        scp -q -o ConnectTimeout=10 -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null root@$ip:/var/run/bmx7/json/netjson/network-routes.json  $data_dir
    else
        echo "node is unreachable"
    fi
done
