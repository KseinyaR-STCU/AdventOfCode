#!/usr/bin/python3
import argparse
import subprocess
import sys
import httplib2

# Usage: ./get_input.py > 1.in
# You must fill in SESSION following the instructions below.
# DO NOT run this in a loop, just once.

# You can find SESSION by using Chrome tools:
# 1) Go to https://adventofcode.com/2022/day/1/input
# 2) right-click -> inspect -> click the "Application" tab.
# 3) Refresh
# 5) Click https://adventofcode.com under "Cookies"
# 6) Grab the value for session. Fill it in.

session = ''

with open('session.txt') as f:
    for line in f:
        session = line

SESSION = session

parser = argparse.ArgumentParser(description='Read input')
parser.add_argument('--year', type=int, default=2020)
parser.add_argument('--day', type=int, default=1)
args = parser.parse_args()

cookies = f"session={SESSION}"

headers = { "Cookie": cookies }

url = f'https://adventofcode.com/{args.year}/day/{args.day}/input'

http = httplib2.Http(".cache", disable_ssl_certificate_validation=True)

response, content = http.request(url, 'GET', headers=headers)

print(content.decode('utf-8'))
