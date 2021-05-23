#! /usr/bin/python3.7
#
import sys
import os


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    IPadres = '192.168.1.1'
    os.system("sudo nmap -O " + IPadres)
    os.system("sudo nmap -sP  " + IPadres + " | awk '/Nmap scan report for/{printf $5;}/MAC Address:/{print $3;}' | sort")
    os.system("sudo nmap -sP 192.168.1.0/24")

