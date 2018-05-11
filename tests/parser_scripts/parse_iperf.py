#!/usr/bin/env python2
import glob
from collections import defaultdict
import sys
import numpy as np
import tempfile
import argparse
import os

def compute_percentiles_iperf(ff, source_ip=""):
        f = open(ff)
        bitrate_list = []
        transferred_list = []
        data = defaultdict(dict)
        s = source_ip
        d  = ""
        for l in f.readlines():
            data = l.split(",")
            if not s:
                s = data[1]
            d = data[3]
            bitrate_list.append(float(data[-1][:-1]))
            transferred_list.append(float(data[7]))
        if not s or not d or s == d:
            return []
        return s, d, np.percentile(bitrate_list, 50),\
              np.percentile(bitrate_list, 10),\
              np.percentile(bitrate_list, 90),\
              np.percentile(transferred_list, 50)


def compute_percentiles_ping(ff, source_ip=""):
        f = open(ff)
        loss_percentage = []
        avg_rtt = []
        data = defaultdict(dict)
        s = source_ip
        for d in f.readlines():
            data = d.split(",")
            if len(data) < 4:
                return
            if not s:
                s = data[0]
            try:
                loss_percentage.append(float(data[2]))
                d = data[1]
                avg_rtt.append(float(data[4].strip("ms")))
            except Exception:
                return []
        if not s or s == d:
            return []
        return s, d, np.percentile(loss_percentage, 50),\
               np.percentile(avg_rtt, 50)


print_header = True
sort_by = 0
def print_percentiles(file_list, source_ip=""):
    global print_header
    global sort_by
    lines = []
    for ff in file_list:
        if os.path.basename(ff).find("iperf") is not -1 and args.k == "iperf":
            sort_by = 2
            if print_header:
                print("source_address, destination_address, transferred_bytes,"
                      "bits_per_second (median), bits_per_second (10perc),"
                      "bits_per_second (90perc)")
                print_header = False
            l = compute_percentiles_iperf(ff, source_ip=source_ip)
            if l:
                lines.append(l)
        elif os.path.basename(ff).find("ping") is not -1 and args.k == "ping":
            sort_by = 3
            if print_header:
                print("source_address, destination_address, ping median loss")
                print_header = False
            l = compute_percentiles_ping(ff, source_ip=source_ip)
            if l:
                lines.append(l)
    return lines



def collect_files(ip_list, file_path):
    file_list = []
    tmpdir = "/tmp/" + os.tempnam()
    os.mkdir(temp_folder)
    for ip in ip_list:
        cmd = "scp " + ip + ":" + file_path + " " + tmpdir
        retcode = subprocess.call(cmd, shell=True)
        file_list.append(tmpdir + file_path)
    return file_list


parser = argparse.ArgumentParser()
parser.add_argument("-f", help="pass a path for files to parse, "
                    "will expand to *.csv")
parser.add_argument("-d", help="pass a dir made of dirs in the format:"
                    "iperf_test_SOURCE_IP/ each of them containing log file")
parser.add_argument("-t", help="pass a list of IPs to scp files from",
                    nargs="+")
parser.add_argument("-p", help="pass a path for the file to scp and parse")
parser.add_argument("-k", choices=["iperf", "ping"], default="ping",
                    help="force to some kind of log")


args = parser.parse_args()

data_lines = []
if args.d:
    sub_folder = args.d
    folders = [x[0] for x in os.walk(sub_folder)]
    for f in folders[1:]:
        try:
            source_ip = f.split("/")[-1].split("_")[2]
        except Exception:
            continue
        data_path = f+"/*csv"
        file_list = glob.glob(data_path)
        data_lines += print_percentiles(file_list, source_ip=source_ip)

for line in sorted(data_lines, key=lambda x: x[sort_by]):
    print ",".join(map(str,line))
exit()

if args.f:
    data_path = args.f+"*csv"
    file_list = glob.glob(data_path)
    data_lines += print_percentiles(file_list)
elif args.h and args.p:
    file_list = collect_files(args.h)
    data_lines += print_percentiles(file_list)
