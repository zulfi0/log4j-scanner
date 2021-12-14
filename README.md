# log4j-scanner
**Cli log4j scanner vulnerability**

Built in socket tcp server and scan the url with some payload and headers.
If you find another headers or payload feel free to add it in line 14-15.

## How it works
- the script will create tcp server that listen on port 1389 
- while the server is ready for accepting connection the script will scan the supplied url.
- if the url is vulnerable the script will output an *Info: \<url\> is vulnerable* with the payload

### example:

## Installation
