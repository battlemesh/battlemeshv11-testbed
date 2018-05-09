# perform an iperf towards a node, save the result in a file in /tmp 
source ip_list.sh
usage() { echo "$0 usage:" && grep " .)\ #" $0; exit 0; }
[ $# -eq 0 ] && usage

while getopts ":c:nr" arg; do
  case $arg in
    c) # Specify destination.
      DEST=${OPTARG}
      ;;
    n) # delete previous output file
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

IPERFOUT="/tmp/iperftest-iperf-"`hostname`"-$DEST.csv"
if [ $DELETE ];
then 
    rm $IPERFOUT
fi 

if [ $RND ];
then 
    DEST_ID=$(($RANDOM%${#IPv4[@]}))
    DEST=${IPv4[$DEST_ID]}
fi



#iperf -f M -y C -t 10 -e -V -c $DEST | tail -n 2 >> $IPERFOUT
iperf -f M -y C -t 10 -e -c $DEST | tail -n 2 >> $IPERFOUT
