# A simple no-ip DUC for Linux, with ipv6 support

# put ya account info & hostname here
# email in the first, password in the second
account = ('wanghui15189@gmail.com', 'LL20090426noip')
toBeUpdated = 'servusbro.ddns.net'

# This has also to be changed
# Go to the github wiki or the readme for more info
whichOne = 2

######################################################################################

# Import needed libs
import requests
import subprocess

# This is the standard server provided by no-ip to
# update the dns
updateurl = "http://dynupdate.no-ip.com/nic/update"

# execute hostname -I to get your ipv6
hostnameReturn = subprocess.Popen("hostname -I", shell=True, stdout=subprocess.PIPE)

# ipv6 addr is the 3rd output of hostname -I
# so let's grab that
ipv6addrs = hostnameReturn.stdout.read()
ipv6addr = str(ipv6addrs).split(' ')[whichOne]
print(ipv6addr)  # print out just to be sure

# define parameters for updating dns
parameters = {'hostname': toBeUpdated, 'myipv6': ipv6addr}

# some stuff ya dont need to care about
requestHeader = {'User-Agent': 'Linux Custom DUC'}

# request ddns update
serverreturn = requests.get(url = updateurl, params = parameters, auth=account)
print(serverreturn.url)
print(serverreturn.text)
