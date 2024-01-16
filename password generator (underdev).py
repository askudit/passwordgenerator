while True:
	import random
	lower = "abcdefghijklmnopqrstuvwxyz"
	upper = lower.upper()
	digits="123456789"
	symbols="@*-_~"
	print("password generator")
	print ('''	1.wifi
	2.facebook
	3.Instagram
	4.Email
	5.Microsoft teams
	6.Only letters
	7.Letters and digits
	8.Letters and symbols
	Enter the serial number only.''')
	n=int(input ("enter the category:"))
	
	all=""
	
	if n==1:
		I=int(input ("enter the number of characters to be in your password:"))
		N=int(input ("enter the amount of password you want:"))
		all+=upper+lower+digits+symbols
		for x in range (N):
			password="".join(random.sample(all,I))
			print("your password:- ", password)
	elif n==2:
		I=int(input ("enter the number of characters to be in your password:"))
		N=int(input ("enter the amount of password you want:"))
		all+=upper+lower+digits
		for x in range (N):
			password="".join(random.sample(all,I))
			print("your password:- ", password)
	elif n==3:
		I=int(input ("enter the number of characters to be in your password:"))
		N=int(input ("enter the amount of password you want:"))
		all+=upper+lower+ digits
		for x in range (N):
			password="".join(random.sample(all,I))
			print("your password:- ", password)
	elif n==4:
		I=int(input ("enter the number of characters to be in your password:"))
		N=int(input ("enter the amount of password you want:"))
		all+=upper + lower + digits + symbols
		for x in range (N):
			password="".join(random.sample(all,I))
			print("your password:- ", password)
	elif n==5:
		I=int(input ("enter the number of characters to be in your password:"))
		N=int(input ("enter the amount of password you want:"))
		all+=upper + lower + digits
		for x in range (N):
			password="".join(random.sample(all,I))
			print("your password:- ", password)
	elif n==6:
		I=int(input ("enter the number of characters to be in your password:"))
		N=int(input ("enter the amount of password you want:"))
		all+=upper+lower
		for x in range (N):
			password="".join(random.sample(all,I))
			print("your password:- ", password)
	elif n==7:
		I=int(input ("enter the number of characters to be in your password:"))
		N=int(input ("enter the amount of password you want:"))
		all+=upper+lower+digits
		for x in range (N):
			password="".join(random.sample(all,I))
			print("your password:- ", password)
	elif n==8:
		I=int(input ("enter the number of characters to be in your password:"))
		N=int(input ("enter the amount of password you want:"))
		all+=upper+lower+symbols
		for x in range (N):
			password="".join(random.sample(all,I))
			print("your password:- ", password)
	else:
		print("enter the appropriate serial number")
		
	d=input("do you want to continue?(y/n): ").lower()
	if d == "y":
		continue
	else:
		break