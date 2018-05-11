set datafile separator ','
set yrange [-1:100]
set xlabel "Path"
set ylabel "bps"
plot '../parsed_data/iperf.csv' u 0:3  axes x1y1 w l t "bps"
