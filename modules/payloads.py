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

def payload():
        banner()

        print(color.RED+"\n        [#] Payloads for vulnerability !! [#]")
        print("""
        """+color.YELLOW+"""["""+color.WHITE+"""1"""+color.YELLOW+"""]"""+color.GREEN+""" XSS
        """+color.YELLOW+"""["""+color.WHITE+"""2"""+color.YELLOW+"""]"""+color.GREEN+""" SQL Injection
        """+color.YELLOW+"""["""+color.WHITE+"""3"""+color.YELLOW+"""]"""+color.GREEN+""" OPEN Redirect
        """+color.YELLOW+"""["""+color.WHITE+"""4"""+color.YELLOW+"""]"""+color.GREEN+""" RFI / LFI
        """+color.YELLOW+"""["""+color.WHITE+"""5"""+color.YELLOW+"""]"""+color.GREEN+""" RCE
        """+color.YELLOW+"""["""+color.WHITE+"""6"""+color.YELLOW+"""]"""+color.GREEN+""" CSRF
        """+color.YELLOW+"""["""+color.WHITE+"""99"""+color.YELLOW+"""]"""+color.GREEN+""" exit
        """)
        choose_payload = input("        "+color.RED+"["+color.WHITE+"?"+color.RED+"]"+color.BLUE+" choose an option "+color.YELLOW+"# "+color.WHITE+"──╼ >> : ")

        if choose_payload == '1':
                xss()
        elif choose_payload == '2':
                sqli()
        elif choose_payload == '3':
                openredir()
        elif choose_payload == '4':
                rl_fi()
        elif choose_payload == '5':
                rce()
        elif choose_payload == '6':
                csrf()
        elif choose_payload == '99':
                sys.exit()
        
        else:
                print(color.RED+"\n        [-] choose a number option !!")
                time.sleep(3)
                payload()


def xss():
        xss = open("files/xss.txt", "r")
        read = xss.readlines()
        print(color.GREEN)
        for i in read:
                print(i)
        xss.close()
        input(color.GREEN+"\n        [~] Enter for Back To Menu : ")
        banner()
        payload()
def sqli():
        sqli = open("files/sql.txt", "r")
        read = sqli.readlines()
        print(color.GREEN)
        for i in read:
                print(i)
        sqli.close()
        input(color.GREEN+"\n        [~] Enter for Back To Menu : ")
        banner()
        payload()
def openredir():
        openredir = open("files/open_redir.txt", "r")
        read = openredir.readlines()
        print(color.GREEN)
        for i in read:
                print(i)
        openredir.close()
        input(color.GREEN+"\n        [~] Enter for Back To Menu : ")
        banner()
        payload()
def rl_fi():
        rl_fi = open("files/file_inc.txt", "r")
        read = rl_fi.readlines()
        print(color.GREEN)
        for i in read:
                print(i)
        rl_fi.close()
        input(color.GREEN+"\n        [~] Enter for Back To Menu : ")
        banner()
        payload()
def rce():
        rce = open("files/rce.txt", "r")
        read = rce.readlines()
        print(color.GREEN)
        for i in read:
                print(i)
        rce.close()
        input(color.GREEN+"\n        [~] Enter for Back To Menu : ")
        banner()
        payload()
def csrf():
        csrf = open("files/csrf.txt", "r")
        read = csrf.readlines()
        print(color.GREEN)
        for i in read:
                print(i)
        csrf.close()
        input(color.GREEN+"\n        [~] Enter for Back To Menu : ")
        banner()
        payload()
