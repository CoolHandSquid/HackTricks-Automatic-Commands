#!/usr/bin/env python3
import os
import pwd
import shlex
import pprint
import argparse
import subprocess
from netaddr import *

parser  = argparse.ArgumentParser()
parser.add_argument("IP", help="IP address of the target", type=str)
args    = parser.parse_args()

try:
    IP      = IPAddress(args.IP)
    LastOct = args.IP.split('.')[-1]
except:
    print("That does not seem to be a valid IP. Exiting...")
    exit()

cwd = os.getcwd()
trd = subprocess.getoutput("readlink /usr/bin/TmuxRecon")
trd = trd[:-12]

hassession  = subprocess.run(shlex.split("tmux has-session -t TR_{}".format(LastOct)), stderr=subprocess.DEVNULL)
if hassession.returncode == 0:
    print("A session for {} already exists. Exiting".format(IP))
    exit()
else:
    pass

subprocess.run(shlex.split("tmux new-session -s TR_{} -n Main -c {} -d".format(LastOct, cwd)))
subprocess.run(shlex.split("tmux send-keys -t TR_{}:0.0 '{}app.py {} {} {} {}' Enter".format(LastOct, trd, IP, LastOct, cwd, trd,)))
print("TmuxRecon session for {} named TR_{} has started successfully!\n\nList of running Tmux sessions:".format(IP, LastOct))
subprocess.run(shlex.split("tmux ls"))
