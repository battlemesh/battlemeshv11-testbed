#!/bin/bash

loss=$(echo $@ | awk -F '%' '{print $1}' | awk '{print $NF}')
rtt_min=$(echo $@ | awk -F '/' '{print $4}' | cut -d "=" -f 2 | tr -d '[:space:]')
rtt_avg=$(echo $@ | awk -F '/' '{print $5}')
rtt_max=$(echo $@ | awk -F '/' '{print $6}')
echo $loss,$rtt_min,$rtt_avg,$rtt_max
