set datafile separator ','
set xlabel "Path"
set ylabel "bps"
plot '../parsed_data/iperf_alltogether.csv' u 0:3 w l  t "bps"
