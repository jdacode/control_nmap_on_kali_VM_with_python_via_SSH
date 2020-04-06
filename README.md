
## Prerequisites

The following are the tools used in the project:

- Python 3
- Flask
- VirtualBox
- paramiko
- kali linux
- Nmap


## Launch 

Launch it in your terminal:
```sh
pip3 install -r requirements.txt

python3 app.py
```

On the virtual machine:
```sh
sudo systemctl start ssh
```

Result:
```sh
kali SSH!

NMAP:

Starting Nmap 7.80 ( https://nmap.org ) at 2020-04-06 13:25 EDT
Nmap scan report for m.home (192.168.1.1)
Host is up (0.038s latency).
Not shown: 998 closed ports
PORT STATE SERVICE
53/tcp open domain
80/tcp open http

Nmap done: 1 IP address (1 host up) scanned in 0.60 seconds 
```

## Screenshots

![image](static/img/1.png)