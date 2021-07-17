####################################################
# Import Python modules
####################################################

import subprocess

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
	print ("03. Exit the Script")
	print ()

	MenuListOption = int(input("Select an option: "))
	
	print()
	
	if MenuListOption == 1:
		subprocess.run(["netstat","-tnlp4"])
		input("\nPress Enter to continue...")
		menu()
	elif MenuListOption == 2:
		subprocess.run(["systemctl","status","ssh"])
		input("\nPress Enter to continue...")
		menu()
	elif MenuListOption == 3:
		subprocess.run("clear")
		exit()
		
			
####################################################
# Call main Method
####################################################

if __name__ == "__main__":
	menu()
