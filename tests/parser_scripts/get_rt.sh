#!/bin/bash

. ../test_script/ip_list.sh
. ../test_script/functions.sh
$name=$1

for ip in ${IPv4_mgmt[@]}; do
    data_dir="../data/$name/crash_test_$ip"
    echo -n "gathering data from $ip ..."
    if check_if_up $ip; then
        mkdir -p $data_dir
        echo "OK"
        scp -q -o ConnectTimeout=10 -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null root@$ip:/tmp/olsrd2-routes_prince/* $data_dir
        # scp -q -o ConnectTimeout=10 -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null root@$ip:/tmp/olsrd2-routes/* $data_dir
        # scp -q -o ConnectTimeout=10 -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null root@$ip:/tmp/bmx7-routes/* $data_dir
    else
        echo "node is unreachable"
    fi
done
