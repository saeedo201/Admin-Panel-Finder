#!/usr/bin/env python 2.7.16
# -*- coding: UTF-8 -*-

from urllib2 import Request, urlopen, URLError, HTTPError

def Space(j):
	i = 0
	while i<=j:
		print " ",
		i+=1


def findAdmin():
	f = open("link.txt","r");
	link = raw_input("Enter Your Site Name \n(ex : example.com or www.example.com ): ")
	print "\n\nTrying for links.\..\...\ : \n"
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
			print "OK => Page Founded",req_link
			print "Thanks For Usage..!"
			break

def Credit():
	Space(9); print "+++++++++++++++++++++++++++++++++++++"
	Space(9); print "#   +++ Admin Panel Finder    +++   #"
	Space(9); print "#   CopyRight by : Zoal Ktoom       #"
	Space(9); print "#    Thanks For Usage My Tool       #"
	Space(9); print "+++++++++++++++++++++++++++++++++++++"

Credit()
findAdmin()
