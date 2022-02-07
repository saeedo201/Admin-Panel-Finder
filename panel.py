#!/usr/bin/env python 3
# -*- coding: UTF-8 -*-
import time, os, sys, random
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
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
     Y = "\033[33;1m"  # Yellow
     G = "\033[32m"    # Green
     W = "\033[0;1m"   # White
     R = "\033[31m"    # Red
     C = "\033[36;1m"  # Cyan
     rand = (BB,YY,GG,WW,RR,CC)
     P = random.choice(rand)
def cover():
    runntek(GL+"Have A Hunting Day.")
time.sleep(1)
cover()
def banner():
	print(f"""\n                {R} - {W}Athuer: Saeed Ahmed {R}  -\n   {R}        -{W} Telegram: https://t.me/Zoalktoom {R}-\n           -{W} Youtube: https://youtube.com/c/ThebandBlue {R}-\n           -{W} Github: https://github.com/saeedo201 {R}-\n          {R} - {W}Admin-Panel-Finder  Version: 2.0 {R} -\n""")
	print(f"""\n      {Y} [{W}The Options{Y}]""")
	print(f"""   	 {R} - {W}1{G} ~{W} Extraction Admin Panel .\n	 {R} - {W}2 {G}~ {W}Exit .\n""")
class Main:
    def start():
        choice = input(R+" ┌─["+GG+"Panel-Finder"+B+"~"+W+"@Options"+R+"""]
 ╰──➤ """+W)
        if choice == "1":
            print()
            Main.findAdmin()
        elif choice == "2":
            print("good bye")
            sys.exit()
        else:
            print(R +"invalid choice")
            time.sleep(2)
            os.system("clear")
            banner()
            Main.start()
    def findAdmin():
    	f = open("link.txt", "r")
    	link = input(C+" ┌─["+W+ "Your Link Without Http/Https"+C+"""]
 ╰──➤ """+W)
    	stt = C +"The admin panel is now being extracted"
    	for line in range(4):
    		print (f"\r{stt}", end = "")
    		time.sleep(1)
    		if line == 2:
    			stt += "."
    		else:
    			stt += "."
    	time.sleep(1)
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
    			print(GG+"OK => Page Founded ----> ", req_link)
    			print(CC+"Thanks For Usage..!")
    			break

banner()
Main.start()
