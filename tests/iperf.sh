# perform an iperf towards a node, save the result in a file in /tmp 

usage() { echo "$0 usage:" && grep " .)\ #" $0; exit 0; }
[ $# -eq 0 ] && usage
while getopts ":c:n" arg; do
  case $arg in
    c) # Specify destination.
      DEST=${OPTARG}
      ;;
    n) 
	  DELETE=1
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


iperf -f M -y C -t 10 -e -V -c $DEST | tail -n 2 >> $IPERFOUT
