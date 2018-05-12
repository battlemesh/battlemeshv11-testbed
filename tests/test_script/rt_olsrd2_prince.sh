while [ 1 ];do
	time=`date +%s`
	echo Dumping at $time
	mkdir -p /tmp/olsrd2-routes_prince/
  routes=`echo /netjsoninfo filter route ipv4_0 | nc 127.0.0.1 2009`  
	echo $routes > /tmp/olsrd2-routes_prince/$time
	sleep 1
done;
