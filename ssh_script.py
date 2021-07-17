####################################################
# Import Python modules
####################################################

import subprocess
import datetime

####################################################
# Import Python files
####################################################



####################################################
# Main Method
####################################################

def menu():

	subprocess.run("clear")
	
	print ()
	print ("*****************************************")
	print ("        WELCOME TO SSH MODULE")
	print ("*****************************************")
	print ()
	print ("01. Verify Server is listening on TCP Port 22")
	print ("02. Verify SSH Service is Running")
	print ()

	MenuListOption = int(input("Select an option: "))
	
	if MenuListOption == 1:
		subprocess.run(["netstat","-tnlp4"])
	elif MenuListOption == 2:
		subprocess.run(["systemctl","status","ssh"])
		
			
####################################################
# Call main Method
####################################################

if __name__ == "__main__":
	menu()
