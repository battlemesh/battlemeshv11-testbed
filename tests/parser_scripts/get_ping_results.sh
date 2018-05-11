#!/bin/bash

. ../test_script/ip_list.sh
. ../test_script/functions.sh


for ip in ${IPv4_mgmt[@]}; do
    data_dir="../data/iperf_test_$ip"
    echo -n "gathering data from $ip ..."
    if check_if_up $ip; then
        mkdir -p $data_dir
        echo "OK"
        scp -q -o ConnectTimeout=10 -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null root@$ip:/tmp/iperf*csv  $data_dir
        scp -q -o ConnectTimeout=10 -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null root@$ip:/tmp/ping*csv  $data_dir
    else
        echo "node is unreachable"
    fi
done
