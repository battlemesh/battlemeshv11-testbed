#!/bin/sh
if="eth0"
cat $1 | while read -r line
do
    ip="$line"%$if
    ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null root@$ip 'ash -s'< scripts/reload_network
    echo "runned $2 on $ip"
done
