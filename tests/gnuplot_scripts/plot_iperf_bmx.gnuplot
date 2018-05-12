set terminal png
set output "../graphs/iperf_results_bmx.png"
set key autotitle columnhead

set datafile separator ','
set xlabel "Path"
set ylabel "Mbps"
set xrange [0:180]

plot '../parsed_data/iperf_bmx.csv' u 0:($3/1000000)  axes x1y1 w l t "BMXv7"
