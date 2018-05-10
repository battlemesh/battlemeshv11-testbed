#! /bin/bash

. ip_list.sh

for ip in ${IPv4}; do
    echo "Getting the RT from node $ip "
    echo "/netjsoninfo routes" | nc $ip 2009 > ../test_data/${ip}.json
done
