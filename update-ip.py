import base64, urllib2

print "No-IP Updater \n"

hostname = 'mysite.ddns.net'
user, pswd = 'myEmail@isMyUsername.com', 'myPassword'
noip_url = 'https://dynupdate.no-ip.com/nic/update?hostname='

request_link = noip_url + hostname
print request_link

request = urllib2.Request(request_link)
print "Request is sent "

auth = base64.encodestring(user + ':' + pswd).replace('\n','')
print "String is encoded: " + auth

request.add_header('Authorization', 'Basic ' + auth)
print "Authorization header added"

resp = urllib2.urlopen(request)
print "Response:"
print resp

content = resp.read()
if "good" in content:
    print "DNS hostname update successful."
if "nochg" in content:
    print "IP address is current, no update performed."
if "nohost" in content:
    print "Hostname supplied does not exist under specified account."
if "badauth" in content:
    print "Invalid username password combination."
if "badagent" in content:
    print "Client disabled."
if "!donator" in content:
    print "An update request was sent including a feature that is not available to that particular user such as offline options."
if "abuse" in content:
    print "Username is blocked due to abuse."
if "911" in content:
    print "A fatal error on No-IP server. Retry the update no sooner 30 minutes."

