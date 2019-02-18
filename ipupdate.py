#!/usr/bin/env python
# encoding: utf-8

"""
no-ipDUC.py
Created by Robert Dempsey on 12/6/14.
Copyright (c) 2014 Robert Dempsey. Use at your own peril.

This script works with Python 3.x

NOTE: replace values in ALL CAPS with your own values
"""

import os
import smtplib
import time
import urllib2
import base64
import sys
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from subprocess import call
from glob import glob;

COMMASPACE = ', '

def main():

  # global parameters
  #=====================================================================
  myurl = "mydomain.ddns.net"
  username = "xxxx@xxx.xxx.xx"
  password = "xxxxxxx"
  recipients = ['xxxx@xxx.xxx.xx']

  # no-ip setup
  #=====================================================================
  web_page = urllib2.urlopen("http://iptools.bizhat.com/ipv4.php")
  myip = web_page.read()

  update_url = "https://dynupdate.no-ip.com/nic/update?hostname=" + myurl + "&myip=" + myip

  req = urllib2.Request(update_url)
  req.add_header('Authorization', ' Basic '+base64.encodestring(username+":"+password).replace("\n",""))
  resp = urllib2.urlopen(req)
  content = resp.read()

  # Create the enclosing (outer) message
  #=====================================================================
  outer = MIMEMultipart()
  outer['Subject'] = '[no-ip] - UPDATE: ' + myip
  outer['To'] = COMMASPACE.join(recipients)
  outer['From'] = username
  outer.preamble = 'You will not see this in a MIME-aware mail reader.\n'

  timestr = time.strftime("%Y%m%d-%H%M%S")
  file_name = timestr+".jpg"

  # Take picture
  #=====================================================================

#    for filename in glob("/home/pi/*.jpg"):
#     os.remove(filename)

#    call(["/home/pi/webcam.sh", file_name])

    # List of attachments
#    full_path = "/home/pi/"+file_name
#    attachments = [full_path]

    # Add the attachments to the message
#    for file in attachments:
#        try:
#            with open(file, 'rb') as fp:
#                msg = MIMEBase('application', "octet-stream")
#                msg.set_payload(fp.read())
#            encoders.encode_base64(msg)
#            msg.add_header('Content-Disposition', 'attachment', filename=os.path.basename(file))
#            outer.attach(msg)
#        except:
#            print("Unable to open one of the attachments. Error: ", sys.exc_info()[0])
#            raise

  composed = outer.as_string()

  # Send the email
  try:
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    #s.ehlo()
    s.login(username, password)
    s.sendmail(username, recipients, composed)
    s.close()
    print("Email sent!")
  except:
    print("Unable to send the email. Error: ", sys.exc_info()[0])
    raise

if __name__ == '__main__':
  main()


