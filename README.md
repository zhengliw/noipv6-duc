# noipv6-duc
THE ULTIMATE NO-IP IPV6 DUC. JUST WORKS.

## How does this work?

I use the standard provided API from No-IP, by sending a HTTP GET request to their server.
Assuming you have access to ipv6 AND you run a linux-based system, or else this whole thing isn't gonna work.
But, a BIG but: With little modifications, this can also work on Windoze etc. The limitation is just your skill level.
Oh, are you allowed to roast people on GitHub XD

## How did you make this?

I'm a noob when it comes to network stuff in Python, so yeah, a lot of googling...

## How to set it up?

It's pretty simple. Just follow the steps.

1. Save the script as a backup before you start, in case you want to change something afterwards. If not, proceed.
2. Open the script and in the first lines, replace the placeholders by actual values. E.g. your email for No-IP.
3. This one's gotta be tricky, so follow closely.
You see the 'whichOne' variable, which has to be set according to your system.
First, go to 'test-ipv6.com' and remember the last 4 letters/numbers in your ipv6 address.
Then, open a terminal, type in hostname -I.
Find the ipv6 address in the hostname -I's output, which corresponds to the one that test-ipv6.com reported.
If it is the first ip, set the whichOne variable to 0. Is it the second, set whichOne to 1 and so on.

Let me show:

test-ipv6.com says xxxx:xxx:xxxx:xxxx:xxxx:xxxx:xxxx:3d18
hostname -I says 192.168.0.xxx xxx:xxx:xxx:xxxx:xxxx:xxxx:xxxx:3d18 xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx 

So it's the second one. In this case, set whichOne to 1.

There's a more advanced method without having to access the web, I will write it if you ask me in the issues reporter.
