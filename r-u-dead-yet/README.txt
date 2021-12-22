R-U-Dead-Yet is run in one of two modes:

1) Interactive menu mode
2) Unattended configuration-based execution

In order to run using the first mode, run as following:

r-u-dead-yet.py <URL>

whereas URL is the FQDN link leading to a web page containing a web form to attack. r-u-dead-yet will take care of the rest of the procedure allowing the user to pick what form to attack, what field, and with how many concurrent connections.

In the unattended mode, you will need to place a file called:

rudeadyet.conf

in the same directory as the code (BeautifulSoup.py is also required).
The file should look like this:

[parameters]



URL: http://www.victim.com/path-to-post-url.php

number_of_connections: 500

attack_parameter: login

Whereas URL = POST URL
number_of_connections = concurrent processes to execute
attack_parameter = POST parameter to fuzz

TODO
----

- Add the ability to manage cookies
- Add custom headers and POST parameters needed