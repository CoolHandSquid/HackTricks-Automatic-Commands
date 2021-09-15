#!/usr/bin/env python3
import os
import pprint
import pwd
import argparse
import shlex
import subprocess
from netaddr import *

parser  = argparse.ArgumentParser()
parser = argparse.ArgumentParser(description='HackTricks Automatic Commands is Powered by book.hacktricks.xyz.')
parser.add_argument("IP", help="IP adress or hostname of the target", type=str)
parser.add_argument('-i', '--interface', default='tmux', help='Interact with HAC via "tmux", "tilix", or "terminator". tmux is default')
args    = parser.parse_args()

cwd     = os.getcwd()
hacd   = subprocess.getoutput("readlink /usr/bin/HAC")
hacd   = hacd[:-6]

try:
    IP      = IPAddress(args.IP)
    hostname = args.IP.replace('.','_')
except:
    hostname = IP = args.IP

def init_HAC_tmux():
    hassession  = subprocess.run(shlex.split("tmux has-session -t HAC_{}".format(hostname)), stderr=subprocess.DEVNULL)
    if hassession.returncode == 0:
        print("A session for {} already exists. Exiting".format(IP))
        exit()
    else:
        pass
    
    subprocess.run(shlex.split("tmux new-session -s HAC_{} -n Main -c {} -d".format(hostname, cwd)))
    subprocess.run(shlex.split("tmux send-keys -t HAC_{}:0.0 '{}HAC_tmux.py {} {} {} {}' Enter".format(hostname, hacd, IP, hostname, cwd, hacd)))
    print("HackTricks Automatic Commands session for {} named HAC_{} has started successfully!\n\nList of running Tmux sessions:".format(IP, hostname))
    subprocess.run(shlex.split("tmux ls"))

def init_HAC_tilix():
    if pwd.getpwuid(os.getuid())[0] != "root":
        print("Running the tilix inerface requres the user to be root.")
        exit()
    if os.environ['USER'] != "root":
        print("The shell environment user must be root. Try: sudo HAC x.x.x.x -i tilix")
        exit()
    
    os.system("tilix --maximize -t 'HackTricks Automatic Commands  Main Page' -x $SHELL -c '{}HAC_tilix.py {} ; $SHELL'".format(hacd, IP))
    

def init_HAC_terminator():
    print("Still in development. Hang tight!!")

if args.interface == "tmux":
    init_HAC_tmux()
elif args.interface == "tilix":
    init_HAC_tilix()
elif args.interface == "terminator":
    init_HAC_terminator()
else:
    print("That interface is not valid. Please chose tmux, tilix, or terminator (ex: --interface tilix).")
    exit()

