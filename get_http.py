#! /usr/bin/env python

import os
import urllib2
import json
import subprocess
import StringIO

#os.environ['http_proxy'] = ''
kp = ""
eth0mac = open('/sys/class/net/eth0/address')
wlan0mac = open('/sys/class/net/wlan0/address')
wlan0  = wlan0mac.read()
eth0 = eth0mac.read()
print wlan0
print eth0

kp = 'http://greensnakedesign.com/michael/pitest.php?mac=%s' %(eth0)
#kp = 'http:
print kp
#request = urllib2.Request(kp)

response = urllib2.urlopen(kp)

html = response.read()

print html

js =  json.loads(html)
print js
dump =  json.dumps(html)

if js['status'][0] == 'good':
	print js['status'][0]
else:
	print "not good"

p = subprocess.Popen("date", stdout = subprocess.PIPE)
output, err = p.communicate()
jd = json.dumps(output)
jl = json.loads(jd)
jls = jl.split()

print jls[0]

