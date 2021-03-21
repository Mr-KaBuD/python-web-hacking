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


def inform():
        banner()

        print(color.RED+"\n        [#] Information Gathering !! [#]")
        print("""
        """+color.YELLOW+"""["""+color.WHITE+"""1"""+color.YELLOW+"""]"""+color.GREEN+""" whois
        """+color.YELLOW+"""["""+color.WHITE+"""2"""+color.YELLOW+"""]"""+color.GREEN+""" port scan
        """+color.YELLOW+"""["""+color.WHITE+"""3"""+color.YELLOW+"""]"""+color.GREEN+""" whats run
        """+color.YELLOW+"""["""+color.WHITE+"""4"""+color.YELLOW+"""]"""+color.GREEN+""" get host ip
        """+color.YELLOW+"""["""+color.WHITE+"""5"""+color.YELLOW+"""]"""+color.GREEN+""" subdomain lister
        """+color.YELLOW+"""["""+color.WHITE+"""6"""+color.YELLOW+"""]"""+color.GREEN+""" DNS Lookup
        """+color.YELLOW+"""["""+color.WHITE+"""99"""+color.YELLOW+"""]"""+color.GREEN+""" exit
        """)
        choose_info = input("        "+color.RED+"["+color.WHITE+"?"+color.RED+"]"+color.BLUE+" choose an option "+color.YELLOW+"# "+color.WHITE+"──╼ >> : ")

        if choose_info == '1':
                whois()
        elif choose_info == '2':
                ports()
        elif choose_info == '3':
                whatsrun()
        elif choose_info == '4':
                gethost()
        elif choose_info == '5':
                subdom()
        elif choose_info == '6':
                dnslook()
        elif choose_info == '99':
                sys.exit()
        
        else:
                print(color.RED+"        [?] choose a number option !!")
                time.sleep(3)
                inform()


def whois():
        banner()
        print(color.RED+"\n        [#] WhoIs !! [#]\n")

        url = input(color.BLUE+"        [?] Enter The IP / URL # ──╼ >> : ")

        try:
                result = requests.get('http://api.hackertarget.com/whois/?q=' + url).text
                print(color.WHITE+"\n"+result)
                input(color.GREEN+"\n        [~] Enter for Back To Menu : ")
                inform()

        except:
                print(color.RED+"\n        [!] Error !! , Check your Internet Connection or false input ...")
                time.sleep(3)
                inform()


def ports():
        banner()
        print(color.RED+"\n        [#] Port Scan !! [#]\n")

        url = input(color.BLUE+"        [?] Enter The IP / URL # ──╼ >> : ")

        try:
                result = requests.get('https://api.hackertarget.com/nmap/?q=' + url).text
                print(color.WHITE+"\n"+result)
                input(color.GREEN+"\n        [~] Enter for Back To Menu : ")
                inform()
        except:
                print(color.RED+"\n        [!] Error !! , Check your Internet Connection or false input ...")
                time.sleep(3)
                inform()


def whatsrun():
        banner()
        print(color.RED+"\n        [#] Whats Run !! [#]\n")

        url = input(color.BLUE+"        [?] Enter The URL # ──╼ >> : ")
        
        url.split("http://")
        url.split("https://")
        url.split("www.")

        url = "http://"+url

        try:
                result = builtwith.builtwith(url)
                for i in result:
                        print(color.WHITE+"\n"+i , " : " , result[i][0])
                
                input(color.GREEN+"\n        [~] Enter for Back To Menu : ")
                inform()

        except:
                print(color.RED+"\n        [!] Error !! , Check your Internet Connection or false input ...")
                time.sleep(3)
                inform()


def gethost():
        banner()
        print(color.RED+"\n        [#] Get Host IP !! [#]\n")

        url = input(color.BLUE+"        [?] Enter The URL # ──╼ >> : ")

        try:
                result = socket.gethostbyname(url)
                print(color.GREEN+"\n        ip = ", result)
                input(color.GREEN+"\n        [~] Enter for Back To Menu : ")
                inform()

        except:
                print(color.RED+"\n        [!] Error !! , Check your Internet Connection or false input ...")


def subdom():
        banner()
        print(color.RED+"\n        [#] SUB Domain Lister !! [#]\n")

        subdoms = ['ftp', 'cpanel', 'webmail', 'localhost', 'local', 'mysql', 'forum', 'driect-connect', 'blog', 'vb', 'forums', 'home', 'direct', 'forums', 'mail', 'access', 'admin', 'administrator', 'email', 'downloads', 'dl', 'ssh', 'l', 'developer', 'app', 'owa', 'bbs', 'news', 'i', 'main', 'cp', 'wordprees', 'wp', 'user', 'apps', 'web', 'up', 'upload', 'error', 'developers', 'chat', 'users', 'mobile', 'webmin', 'paralel', 'my', 'me', 'portal', 'parallels', 'www0', 'www', 'www1', 'www2', 'www3', 'www4', 'www5', 'shop', 'api', 'blogs', 'test', 'mx1', 'cdn', 'mysql', 'mail1', 'secure', 'server', 'ns1', 'ns2', 'smtp', 'vpn', 'm', 'mail2', 'postal', 'support', 'web', 'dev']

        url = input(color.BLUE+"        [?] Enter The URL # ──╼ >> : ")
        
        url.split("http://")
        url.split("https://")
        url.split("www.")

        # try:
        for sub in subdoms:
                try:
                        hosts = str(sub) + "." + str(url)
                        bypass = socket.gethostbyname(str(hosts))
                        print(color.GREEN+"\n        [+] Founded = " + str(bypass) + ' - ' + color.YELLOW + str(hosts))
                except Exception:
                        pass
        
        input(color.GREEN+"\n        [~] Enter for Back To Menu : ")
        inform()
        # except:
        #         print(color.RED+"\n        [!] Error !! , Check your Internet Connection or false input ...")
        #         time.sleep(3)
        #         inform()


def dnslook():
        banner()
        print(color.RED+"\n        [#] DNS Lookup !! [#]\n")

        url = input(color.BLUE+"        [?] Enter The URL # ──╼ >> : ")

        try:
                result = requests.get('https://api.hackertarget.com/dnslookup/?q=' + url).text
                print(color.WHITE+"\n"+result)
                input(color.GREEN+"\n        [~] Enter for Back To Menu : ")
                inform()

        except:
                print(color.RED+"\n        [!] Error !! , Check your Internet Connection or false input ...")
                time.sleep(3)
                inform()