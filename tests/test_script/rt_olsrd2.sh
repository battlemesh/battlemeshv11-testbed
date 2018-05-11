while [ 1 ];do
	time=`date +%s`
	echo Dumping at $time
	mkdir -p /tmp/olsrd2-routes/
  routes=`echo \"/netjsoninfo filter route ipv4_0\"`  
	echo $routes > /tmp/olsrd2-routes/$time
	sleep 1
done;
