#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# --== Coded by MR-KaBuD ==--
# - [ Web Hacking Tools ] -
# Version : 1.0

import sys, os, socket, time

try:
        import requests
        import builtwith
except:
        print(color.RED+"[*] Install requests & builtwith for do it")
        print("=> pip install requests")
        print("=> pip install builtwith")
        sys.exit()

def clean():
        os.system('cls' or 'clear')

class color : 
    GREEN = '\033[92m'
    RED = '\033[31m'
    WHITE = '\033[37m'
    YELLOW = '\033[33m'
    BLUE = '\033[94m'


def banner():
        clean()
        print(color.YELLOW+"""\n
 __ v.1      __  _       _    _            _    _               _______          _ 
 \ \        / / | |     | |  | |          | |  (_)             |__   __|        | |
  \ \  /\  / /__| |__   | |__| | __ _  ___| | ___ _ __   __ _     | | ___   ___ | |
   \ \/  \/ / _ \ '_ \  |  __  |/ _` |/ __| |/ / | '_ \ / _` |    | |/ _ \ / _ \| |
    \  /\  /  __/ |_) | | |  | | (_| | (__|   <| | | | | (_| |    | | (_) | (_) | |
     \/  \/ \___|_.__/  |_|  |_|\__,_|\___|_|\_\_|_| |_|\__, |    |_|\___/ \___/|_|
                                                         __/ |                     
                  """+color.WHITE+"""[~] Author : github.com/MR-KaBuD"""+color.YELLOW+"""      |___/                      
        """)


def server_vuln():
        banner()

        print(color.RED+"\n        [#] Check Vulnerability on Web Server !! [#]")
        print("""
        """+color.YELLOW+"""["""+color.WHITE+"""1"""+color.YELLOW+"""]"""+color.GREEN+""" check (Admin Pages)
        """+color.YELLOW+"""["""+color.WHITE+"""2"""+color.YELLOW+"""]"""+color.GREEN+""" check (Uploaders)
        """+color.YELLOW+"""["""+color.WHITE+"""3"""+color.YELLOW+"""]"""+color.GREEN+""" check (Injection - Sql - Xss - etc ...)
        """+color.YELLOW+"""["""+color.WHITE+"""99"""+color.YELLOW+"""]"""+color.GREEN+""" exit
        """)
        choose_info = input("        "+color.RED+"["+color.WHITE+"?"+color.RED+"]"+color.BLUE+" choose an option "+color.YELLOW+"# "+color.WHITE+"──╼ >> : ")

        if choose_info == '1':
                serv_vuln.admin()
        elif choose_info == '2':
                serv_vuln.upload()
        elif choose_info == '3':
                serv_vuln.inject()
        
        elif choose_info == '99':
                sys.exit()
        
        else:
                print(color.RED+"\n        [-] choose a number option !!")
                time.sleep(3)
                server_vuln()


def admin():
        banner()
        print(color.RED+"\n        [#] Check Admin Pages on Server for Bypass !! [#]\n")

        url = input(color.BLUE+"        [?] Enter The IP / URL # ──╼ >> : ")

        try:
                
                input(color.GREEN+"\n        [~] Enter for Back To Menu : ")
                server_vuln()

        except:
                print(color.RED+"\n        [!] Error !! , Check your Internet Connection or false input ...")
                time.sleep(3)
                server_vuln()

