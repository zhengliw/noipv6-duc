# A simple no-ip DUC for Linux, with ipv6 support

# put ya account info & hostname here
# email in the first, password in the second
account = ('email', 'password')
toBeUpdated = 'host.tobeupdated.com'

# This has also to be changed
# Go to the github readme for more info
whichOne = 0

# update every ... seconds
updateFrequency = 300 
######################################################################################

# Import needed libs
import requests
import subprocess
from time import sleep

# This is the standard server provided by no-ip to
# update the dns
updateurl = "http://dynupdate.no-ip.com/nic/update"

# dummy last addr
# lastaddr to compare if anything changed
# this is for avoiding too many requests and
# getting blocked
lastaddr = str() 

while True:
	# execute hostname -I to get your ipv6
	hostnameReturn = subprocess.Popen("hostname -I", shell=True, stdout=subprocess.PIPE)

	# ipv6 addr is the 3rd output of hostname -I
	# so let's grab that
	ipv6addrs = hostnameReturn.stdout.read()
	ipv6addr = str(ipv6addrs).split(' ')[whichOne]
	print(ipv6addr)  # print out just to be sure
	
	
	# define parameters for updating dns
	parameters = {'hostname': toBeUpdated, 'myipv6': ipv6addr}
	# user-agent defining
	requestHeader = {'User-Agent': 'Personal noipv6-duc_1_0.py/linux-v5.0'}
	

	if lastaddr != ipv6addr:
		lastaddr = ipv6addr # update the latest ip address
		# request ddns update
		serverreturn = requests.get(url = updateurl, params = parameters, auth=account)
		if(serverreturn.status_code == 911):
			print("Updating paused. No-IP server asks to stop requesting due to a server-side error for 30 minutes.")
			sleep(1800) # sleep 1800 seconds = 30 minutes
		print(serverreturn.url)
		print(serverreturn.text)
		print("updated. noice job!")
	sleep(updateFrequency)
