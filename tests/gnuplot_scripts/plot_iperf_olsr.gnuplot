set terminal png
set output "../graphs/iperf_results_olsr.png"
set key autotitle columnhead
load "plot_iperf.gnuplot"

reset
set terminal png
set output "../graphs/iperf_results_alltogether_olsr.png"
set key autotitle columnhead
load "plot_iperf_alltogether.gnuplot"


