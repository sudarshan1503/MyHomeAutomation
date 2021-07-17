####################################################
# Import Python modules
####################################################

import subprocess
import datetime

####################################################
# Import Python files
####################################################



####################################################
# Find Syslog Definition
####################################################

def FindSyslog():

	print()
	FindSyslogForDevice = input("Find Syslog for Device: ")
	print()

	DateTimeObj = datetime.datetime.now()
	CurrentTime = str(DateTimeObj.strftime("%y%m%d_%H%M%S_"))
	DeviceSyslogFile = "/home/sudaak/Desktop/Scripting/Python/VENV/MyHomeAutomation/logs/" + CurrentTime + FindSyslogForDevice + ".txt"
	
	with open('/var/log/syslog','rb') as f:
    		FileLinesList = f.readlines()
	
	f = open(DeviceSyslogFile,'w')

	for i in range (0,len(FileLinesList)):
		try:
			if FindSyslogForDevice in FileLinesList[i].decode():
				f.write(FileLinesList[i].decode())
		except:
			continue
			
	f.close()


####################################################
# Troubleshoot Syslog Service Definition
####################################################

def TshootSyslogService():

	print ()
	print ("*****************************************")
	print ("       Troubleshoot Syslog Service")
	print ("*****************************************")
	print ()
	print ("01. Verify Server is listening on UDP Port 514")
	print ("02. Verify Syslog Service is Running")
	print ("03. Check for errors in configuration file")
	print ()
	
	TshootListOption = int(input("Select an option: "))
	print()
	
	if TshootListOption == 1:
		subprocess.run(["netstat","-anup"])
	elif TshootListOption == 2:
		subprocess.run(["systemctl","status","rsyslog.service"])
	elif TshootListOption == 3:
		subprocess.run(["rsyslogd","-f","/etc/rsyslog.conf","-N1"])
	
	print()
	
####################################################
# Main Method
####################################################

def menu():

	subprocess.run("clear")
	
	print ()
	print ("*****************************************")
	print ("        WELCOME TO SYSLOG MODULE")
	print ("*****************************************")
	print ()
	print ("01. Verify Server is listening on UDP Port 514")
	print ("02. Verify Syslog Service is Running")
	print ("03. Find Syslogs for specfic Device")
	print ("04. Exit the Script")
	print ()

	MenuListOption = int(input("Select an option: "))
	
	if MenuListOption == 1:
		subprocess.run(["netstat","-unlp4"])
		input("\nPress Enter to continue...")
		menu()
	elif MenuListOption == 2:
		subprocess.run(["systemctl","status","rsyslog"])
		input("\nPress Enter to continue...")
		menu()
	elif MenuListOption == 3:
		FindSyslog()
		print ("Log File is Created")
		input("\nPress Enter to continue...")
		menu()
	elif MenuListOption == 4:
		subprocess.run("clear")
		exit()
		
			
####################################################
# Call main Method
####################################################

if __name__ == "__main__":
	menu()
