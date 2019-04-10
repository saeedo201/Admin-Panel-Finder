#!/usr/bin/env python 2.7.16
# -*- coding: UTF-8 -*-
import time
import sys
import random
from urllib2 import Request, urlopen, URLError, HTTPError
def runntek(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(10. / 100)
if sys.platform == "linux" or sys.platform == "linux2":
     GL = "\033[96;1m" # Blue aqua
     BB = "\033[34;1m" # Blue light
     YY = "\033[33;1m" # Yellow light
     GG = "\033[32;1m" # Green light
     WW = "\033[0;1m"  # White light
     RR = "\033[31;1m" # Red light
     CC = "\033[36;1m" # Cyan light
     B = "\033[34m"    # Blue
     Y = "\033[33;1m"    # Yellow
     G = "\033[32m"    # Green
     W = "\033[0;1m"     # White
     R = "\033[31m"    # Red
     C = "\033[36;1m"    # Cyan
     rand = (BB,YY,GG,WW,RR,CC)
     P = random.choice(rand)
def cover():
    print """    
     """
    runntek(GL+"           Have A Nice Day. ^_^...")

time.sleep(1)
print " "
cover()
def Wellcome():
        Space(9); print "+++++++++++++++++++++++++++++++++++++"
        Space(9); print "*   +++ Admin Panel Finder    +++   *"
        Space(9); print "*   CopyRight by : Zoal Ktoom       *"
        Space(9); print "*    Thanks For Usage My Tool       *"
        Space(9); print "+++++++++++++++++++++++++++++++++++++"

def Space(j):
	i = 0
	while i<=j:
		print " ",
		i+=1


def findAdmin():
	f = open("link.txt","r");
	link = raw_input("Enter Your Site  \n(ex : example.com or www.example.com ): ")
	print "\n\nTrying for links.\..\\...\\\ : \n"
	while True:
		sub_link = f.readline()
		if not sub_link:
			break
		req_link = "http://"+link+"/"+sub_link
		req = Request(req_link)
		try:
			response = urlopen(req)
		except HTTPError as e:
			continue
		except URLError as e:
			continue
		else:
			print "OK => Page Founded ----> ",req_link
			print "Thanks For Usage..!"
			break

Wellcome()
findAdmin()
