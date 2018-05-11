set datafile separator ','
set xlabel "Path"
set ylabel "Mbps"
set xrange [1:170]

plot '../parsed_data/iperf_bmx.csv' u 0:($3/1000000)  axes x1y1 w l t "Mbps"
