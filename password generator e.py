import random

n=int(input("enter length of the password : "))
a=20 #int(input("enter no. of passwords you want : "))

upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower=upper.lower()
digits="0123456789"
symbols="@_-**@_-@_"

all=" "

if upper:
	all+=upper
if lower:
	all+=lower
if digits:
	all+=digits
if symbols:
	all+=symbols

length=n
amount=a

for i in range(amount):
	password="".join((random.sample)(all, length))
	print(password)