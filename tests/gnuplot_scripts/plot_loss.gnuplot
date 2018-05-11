set datafile separator ','
set yrange [-1:100]
set xlabel "Path"
set ylabel "loss"
set y2tics
set y2label "RTT delay (ms)"
plot '../parsed_data/ping.csv' u 0:3  axes x1y1 w l t "RTT loss", '' u 0:4  axes x1y2 w l t "RTT delay"
