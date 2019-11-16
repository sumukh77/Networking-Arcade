import socket
import select
import sys
import datetime
import time
#code = client.recv(2048)
moves=0
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("0.0.0.0",12000))
cards=client.recv(2048)
c1,c2=cards.split("=>")
card1=int(c1)
card2=int(c2)
print(card1,"  ",card2)
if(card1==0):
	inp=raw_input("1 or 11?")
	client.send(str(inp))
	card1=int(inp)
if(card2==0):
	inp=raw_input("1 or 11?")
	client.send(str(inp))
	card2=int(inp)
sumc=card1+card2

flag="1"
while(flag=="1"):
	flag=raw_input("0 for stay 1 for hit")
	client.send(flag)
	if(sumc>=21):
		flag="0"
	if(flag=="1"):
		c=client.recv(2048)
		card = int(c)
		print("Your New Card is ",card)
		sumc+=card
		print(sumc)
		
st=client.recv(2048)
print(st)




#guess=raw_input("enter")
#client.send(guess)

	
