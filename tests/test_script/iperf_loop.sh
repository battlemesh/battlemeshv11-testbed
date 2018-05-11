#!/bin/bash
# rm /tmp/ping*
# rm /tmp/iperf*
source ip_list.sh
source functions.sh


# while [ 1 ]; do
#   
#   # ./iperf.sh -r -6
#   # sleep 1
# 
#   
# done
for i in `seq 1 ${#IPv6[@]}`; do
  DEST_START=0
  DEST=${IPv6[$DEST_ID]}
  if check_if_up $DEST; then
    ./iperf.sh -6 -c $DEST
  fi;
  DEST_ID=$((($i+$DEST_START)%${#IPv6[@]}))
  DEST=${IPv6[$DEST_ID]}
done
