# perform an iperf towards a node, save the result in a file in /tmp 
source ip_list.sh
usage() { echo "$0 usage:" && grep " .)\ #" $0; exit 0; }
[ $# -eq 0 ] && usage


while getopts ":c:dr" arg; do
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
    h | *) # Display help.
      usage
      exit 0
      ;;
  esac
done


if [ $RND ]; then
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


IPERFOUT="/tmp/iperftest-iperf-"`hostname`"-$DEST.csv"
if [ $DELETE ];
then 
    rm $IPERFOUT
fi 



#iperf -f M -y C -t 10 -e -V -c $DEST | tail -n 2 >> $IPERFOUT
iperf -f M -y C -t 10 -e -c $DEST | tail -n 2 >> $IPERFOUT
