#!/usr/bin/env python

import requests, socket

username = ""
password = ""
hostname = "" # your domain name hosted in no-ip.com

# Gets the current public IP of the host machine.
myip = requests.get('http://api.ipify.org').text

# Gets the existing dns ip pointing to the hostname.
old_ip = socket.gethostbyname(hostname)

# Noip API - dynamic DNS update.
# https://www.noip.com/integrate/request.
def update_dns(config):
    r = requests.get("http://{}:{}@dynupdate.no-ip.com/nic/update?hostname={}&myip={}".format(*config))

    if r.status_code != requests.codes.ok:
        print(r.content)
    pass

# Update only when ip is different.
if myip != old_ip:
    update_dns( (username, password, hostname, myip) )
pass

