#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
Author: https://github.com/michael-pena

A quick and dirty post exploitation tool I made to assist with SUID privilege escalation.
After gaining a shell on the target and running the command:

find / -type f -perm -04000 -ls 2>/dev/null

to find SUID files, a penetration tester will often compare the results of the output
on the target to the binaries listed on GTFOBins. This tool lets you know which binaries 
on the target system can be found on GTFOBins, saving you a lot of time.

Simply run the find command and save the output to a text file (on your attacking machine). 
Run this tool with the text file as a command line parameter and it will tell you which 
binaries can be found on GTFObins along with a url to the page that provides a method to perform privilege escalation.

Example:
python3 gtfobin-grabber.py results.txt
'''

import argparse
import re
import requests
from bs4 import BeautifulSoup


class bcolors:    
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    ORANGE = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'    


BIN_PAGE = 'https://gtfobins.github.io/gtfobins/'

# get command line argument
parser = argparse.ArgumentParser(description='After running a command like "find / -type f -perm -04000 -ls 2>/dev/null" \
 to find all SUID files on a target system, copy the output to a text file and feed it as command line parameter to this \
 tool. It will tell you which binaries can be foud on GTFOBins along with a link to the page.')
parser.add_argument('filename')
args = parser.parse_args()

# process every line in the file and get the binary name and append it to a list
print(f"\n{bcolors.OKBLUE}[+] Processing text file{bcolors.ENDC}")
system_suid_binaries = []
with open(args.filename, 'r') as file:
    lines = file.readlines()

    for line in lines:
        binary = re.findall("([^/]+$)", line)[0]
        system_suid_binaries.append(binary.strip('\n'))


# get all the names of the SUID binaries from GTFOBins
print(f"{bcolors.OKBLUE}[+] Reaching out to GTFOBins & grabbing SUID list{bcolors.ENDC}")
response = requests.get(url='https://gtfobins.github.io/#+suid')
response.raise_for_status()
html = response.text
soup = BeautifulSoup(html, 'html.parser')
gtfo_bin_tags = soup.find_all('a', class_='bin-name')
gtfo_bin_names = [binary.text for binary in gtfo_bin_tags]

# get the matches and print them out
matches = set(system_suid_binaries) & set(gtfo_bin_names)

if len(matches) > 0:
    print(f"{bcolors.OKGREEN}[+] Total matches found: {len(matches)}{bcolors.ENDC}")
    print(f"\n{bcolors.OKBLUE}════════════════════════════════════╣{bcolors.ENDC} {bcolors.OKCYAN}Matches{bcolors.ENDC} {bcolors.OKBLUE}╠════════════════════════════════════{bcolors.ENDC}\n")
    for match in matches:
        print(f"{bcolors.ORANGE}{match}{bcolors.ENDC} - {BIN_PAGE}{match}")
else:
    print(f"{bcolors.RED}[-] No matches found{bcolors.ENDC}")
