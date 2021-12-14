# log4j-scanner
**Cli log4j scanner vulnerability**

Built in socket tcp server and scan the url with some payload and headers.
If you find another headers or payload feel free to add it in line 14-15.

## How it works
- the script will create tcp server that listen on port 1389 
- while the server is ready for accepting connection the script will scan the supplied url.
- if the url is vulnerable the script will output an *Info: \<url\> is vulnerable* with the payload

### example:
![Screenshot_20211214-084050_Termux](https://user-images.githubusercontent.com/68773572/145911840-fd57614c-713f-4305-bc38-93b3103cc223.png)

## Installation
```
git clone https://github.com/zulfi0/log4j-scanner.git
cd log4j-scanner 
python3 4jscan.py http://vuln.com 127.0.0.1:1389
```

## Usage 
```
python3 4jscan.py <url> <localhost:1389>
```
the script accept file that contain url in txt format.
### example using file.txt and ngrok tcp 1389
```
python3 4jscan.py file.txt 0.tcp.ngrok.io:12345
```

#### note :
you need to press ctrl+c manually to exit the script (hehe)

## Demo 


https://user-images.githubusercontent.com/68773572/145912730-2562c511-2d5c-4b01-a8cd-3100393867e2.mp4



