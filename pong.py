# upgrade pip, install pip/pyperclip
#python -m pip install --upgrade pip --trusted-host pypi.org --trusted-host files.pythonhosted.org
#python -m pip install pyperclip --trusted-host pypi.org --trusted-host files.pythonhosted.org

import socket
import pyperclip
from signal import signal, SIGINT
from sys import exit

print("""

8b,dPPYba,   ,adPPYba,  8b,dPPYba,   ,adPPYb,d8  
88P'    "8a a8"     "8a 88P'   `"8a a8"    `Y88  
88       d8 8b       d8 88       88 8b       88  
88b,   ,a8" "8a,   ,a8" 88       88 "8a,   ,d88  
88`YbbdP"'   `"YbbdP"'  88       88  `"YbbdP"Y8  
88                                   aa,    ,88  
88                                    "Y8bbdP"   
	           ,;;;!!!!!;;.
	         :!!!!!!!!!!!!!!;
	       :!!!!!!!!!!!!!!!!!;
	      ;!!!!!!!!!!!!!!!!!!!;
	     ;!!!!!!!!!!!!!!!!!!!!!
	     ;!!!!!!!!!!!!!!!!!!!!'
	     ;!!!!!!!!!!!!!!!!!!!'
	      :!!!!!!!!!!!!!!!!'
	       ,!!!!!!!!!!!!!''
	    ,;!!!''''''''''
	  .!!!!'
	 !!!!

Usage: enter hostname, returned ip will be copied
to clipboard. Typ exit, x or hit ctrl+c to exit.\n\n""")


def handler(signal_received, frame):
    # Handle any cleanup here
    print('\n\nExiting ...')
    exit(0)


if __name__ == '__main__':
	# Tell Python to run the handler() function when SIGINT is recieved
	signal(SIGINT, handler)

	while 1:
		ip = input('> ')
		if ip in ['exit','x','Exit']:
			print('\nExiting ...')
			exit(0)
		else:
			try:
				ip = socket.gethostbyname(ip)
				pyperclip.copy(ip)
				print('\t\t{0} \tcopied to clipboard'.format(ip))
			except:
				print("\tCouldn't resolve to an IP. Sad !")

