from requests import get
import time
import os
from sys import exit
from config.secrets import username, password

def log(text):
    if not os.path.exists("./logs"):
        os.makedirs("./logs")
    print(text)
    with open("./logs/no-ip-duc.txt", "a") as f: 
        f.write(text + "\n")

wait_time = os.environ.get('WAIT_TIME', 10)
domain_name = os.environ.get('DOMAIN')


try:
    wait_time = int(wait_time)
except Exception as e:
    log("[-] 'WAIT_TIME' MUST BE A NUMBER, EXITING...")
    exit(1)

if not domain_name:
    log("[-] 'DOMAIN' NOT FOUND, EXITING...")
    exit(1)

if not username:
    log("[-] 'username' NOT FOUND, EXITING...")
    exit(1)

if not password:
    log("[-] 'username' NOT FOUND, EXITING...")
    exit(1)

sleep_time_min = wait_time
sleep_time = sleep_time_min * 60

while True:
    try:    
        ip = get('https://api.ipify.org').content.decode('utf8')
        log(f"[+] GOT IP {ip}...")
    except Exception as e: 
        log(f"[-] COULD NOT GET IP...RETRYING IN {sleep_time} MINUTES")
        time.sleep(sleep_time)
    try:
        update = get(f"http://{username}:{password}@dynupdate.no-ip.com/nic/update?hostname={domain_name}&myip={ip}")
        log(f"[+] UPDATED IP TO {ip}...WATINING {sleep_time} MINUTES")
        time.sleep(sleep_time)
    except Exception as e: 
        log(f"[-] COULD NOT UPDATE IP...RETRYING IN {sleep_time} MINUTES")
        time.sleep(sleep_time)
