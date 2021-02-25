#!/usr/env python

from bs4 import BeautifulSoup
import requests
import os


print("Welcome!")
while True:

	get_domain = input("press 'c' to clean the screen and 'q' to quit the program!\nEnter domain: ")

	# Quit program
	if get_domain == 'q': 		
		break

	#Clear screen
	elif get_domain == 'c':		
		os.system("clear")

	else:
		try:
			# Get rid of protocol prefix in case user types it:
			if 'http://' in get_domain:
				get_domain = get_domain[7:] 
			
			elif 'https://' in get_domain:
				get_domain = get_domain[8:]

			else:
				with requests.get("https://"+get_domain , stream=True) as r:
					print("\nInformation about {}:".format(get_domain))
					
					# Requests library does not support an option to provide an IP, this is a socket hack:
					ip, port = r.raw._connection.sock.getpeername()
					print("IP: {} Port: {}".format(ip, port))

					print("Response: ",r)

					soup = BeautifulSoup(r.text, "html.parser")
					title = soup.find("title")
					print("Page Title: ", title)

					print("Headers: \n-----------------------")
					a = r.headers
					for k,v in a.items():
						print(k,v)

					r.close()
					print("\n")
		except:
			print("An error has occurred.\n")


print("\nExiting . . . Have a good day!")