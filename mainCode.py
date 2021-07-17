####################################################
# Import Python modules
####################################################

import subprocess

####################################################
# Import Python files
####################################################

import syslog_script

####################################################
# Main Method
####################################################

def menu():

	subprocess.run("clear")
	
	print ()
	print ("*****************************************")
	print ("      WELCOME TO MY HOME AUTOMATION")
	print ("*****************************************")
	print ()
	print ("01. Syslog")
	print ()

	MenuListOption = int(input("Select an option: "))
	
	if MenuListOption == 1:
		syslog_script.menu()
	else:
		print ("Invalid Choice!!!!!")

####################################################
# Call main Method
####################################################

if __name__ == "__main__":
	menu()
