while [ 1 ];do
	time=`date +%s`
	echo Dumping at $time
	mkdir -p /tmp/bmx7-routes/
	cp /var/run/bmx7/json/netjson/network-routes.json /tmp/bmx7-routes/$time
	sleep 1
done;
