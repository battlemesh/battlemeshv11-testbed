#! /bin/bash

cat $1 | while read -r line
do
    ip="$line"
    echo $ip
    mkdir -p ../data/bmx_crash/bmx_crash_test_$ip
    echo|scp -o ConnectTimeout=20 -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null root@[$ip]:/tmp/bmx7-routes/* ../data/bmx_crash/bmx_crash_test_$ip/
done
