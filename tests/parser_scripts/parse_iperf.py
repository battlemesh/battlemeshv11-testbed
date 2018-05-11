#!/usr/bin/env python2
import glob
from collections import defaultdict
import sys
import numpy as np
import tempfile
import argparse
import os

def compute_percentiles_iperf(ff):
        f = open(ff)
        bitrate_list = []
        transferred_list = []
        data = defaultdict(dict)
        s = ""
        for d in f.readlines():
            data = d.split(",")
            s = data[1]
            d = data[3]
            bitrate_list.append(float(data[-1][:-1]))
            transferred_list.append(float(data[7]))
        if not s:
            return
        print s, ",", d, ",", np.percentile(bitrate_list, 50), ",",\
              np.percentile(bitrate_list, 10), ",",\
              np.percentile(bitrate_list,90), ",",\
              np.percentile(transferred_list, 50)

def compute_percentiles_ping(ff):
        f = open(ff)
        loss_percentage = []
        avg_rtt = []
        data = defaultdict(dict)
        s = ""
        for d in f.readlines():
            data = d.split(",")
            s = data[0]
            d = data[1]
            loss_percentage.append(float(data[2]))
            avg_rtt.append(float(data[4].strip("ms")))
        if not s:
            return
        print s, ",", d, ",", np.percentile(loss_percentage, 50)


def print_percentiles(file_list):
    print("source_address, destination_address, transferred_bytes,"
          "bits_per_second (median), bits_per_second (10perc),"
          "bits_per_second (90perc)")
    for ff in file_list:
        if os.path.basename(ff).find("iperf") is not -1:
            compute_percentiles_iperf(ff)
        else:
            compute_percentiles_ping(ff)




#def collect_files(ip_list, file_path):
#    file_list = []
#    tmpdir = "/tmp/" + os.tempnam()
#    os.mkdir(temp_folder)
#    for ip in ip_list:
#        cmd = "scp " + ip + ":" + file_path + " " + tmpdir
#        retcode = subprocess.call(cmd, shell=True)
#        file_list.append(tmpdir + file_path)
#    return file_list


parser = argparse.ArgumentParser()
parser.add_argument("-f", help="pass a path for files to parse, "
                    "will expand to *.csv")
#parser.add_argument("-t", help="pass a list of IPs to scp files from",
#                    nargs="+")
#parser.add_argument("-p", help="pass a path for the file to scp and parse")

args = parser.parse_args()

if args.f:
    data_path = args.f+"*csv"
    file_list = glob.glob(data_path)
    print_percentiles(file_list)
elif args.h and args.p:
    file_list = collect_files(args.h)
    print_percentiles(file_list)
