#!/bin/bash
# perform an iperf towards a node, save the result in a file in /tmp 
source ip_list.sh
source functions.sh

usage() { echo "$0 usage:" && grep " .)\ #" $0; exit 0; }
[ $# -eq 0 ] && usage

hostname=`ip -o addr show dev wlan1|grep inet\ | awk '{print $4}' | sed -e s@/[0-9]*@/32@ | awk -F '/' '{print $1}'`
if [ -z $hostname ]; then 
    hostaname=`hostname`
fi


PING=''
DELETE=''
RND=''

while getopts ":c:drp" arg; do
  case $arg in
    c) # Specify destination.
      DEST=${OPTARG}
      ;;
    d) # delete previous output file
	  DELETE=1
      ;;
    r) # pick a random destination
	  RND=1
      ;;
    p) # do ping instead of iperf
	  PING=1
      ;;
    h | *) # Display help.
      usage
      exit 0
      ;;
  esac
done


if [ -n "$RND" ]; then
    DEST_START=$(($RANDOM%${#IPv4[@]}))
    DEST=${IPv4[$DEST_START]}
    for i in `seq 1 ${#IPv4[@]}`; do
        echo "pinging $DEST"
        if check_if_up $DEST; then
            break;
        else
            DEST_ID=$((($i+$DEST_START)%${#IPv4[@]}))
            DEST=${IPv4[$DEST_ID]}
        fi;
    done
fi

if [ -n "$PING" ]; then
    PINGOUT="/tmp/pingtest-ping-$hostname-$DEST.csv"
    if [ -n "$DELETE" ];
    then 
        rm -f $PINGOUT
    fi 
    ping -c 3 -q $DEST | tail -n 1 >> $PINGOUT
else 
    IPERFOUT="/tmp/iperftest-iperf-$hostname-$DEST.csv"
    if [ -n "$DELETE" ];
    then 
        rm -f $IPERFOUT
    fi 
    iperf -f M -y C -t 10 -e -c $DEST | tail -n 2 >> $IPERFOUT
fi 


#iperf -f M -y C -t 10 -e -V -c $DEST | tail -n 2 >> $IPERFOUT
