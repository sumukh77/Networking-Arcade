from socket import *
from Tkinter import *
import thread
import random
import time
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(("",serverPort))
serverSocket.listen(1)
print("The server is ready to receive")
cards=[0,2,3,4,5,6,7,8,9,10,10,10,10,0,2,3,4,5,6,7,8,9,10,10,10,10,0,2,3,4,5,6,7,8,9,10,10,10,10,0,2,3,4,5,6,7,8,9,10,10,10,10,0,2,3,4,5,6,7,8,9,10,10,10,10,0,2,3,4,5,6,7,8,9,10,10,10,10,0,2,3,4,5,6,7,8,9,10,10,10,10,0,2,3,4,5,6,7,8,9,10,10,10,10,0,2,3,4,5,6,7,8,9,10,10,10,10,0,2,3,4,5,6,7,8,9,10,10,10,10,0,2,3,4,5,6,7,8,9,10,10,10,10,0,2,3,4,5,6,7,8,9,10,10,10,10,0,2,3,4,5,6,7,8,9,10,10,10,10,0,2,3,4,5,6,7,8,9,10,10,10,10,0,2,3,4,5,6,7,8,9,10,10,10,10,0,2,3,4,5,6,7,8,9,10,10,10,10]
def ran():
	r=random.randint(0,len(cards)-1)
	c=cards[r]
	del cards[r]
	return c
lc={}
card=ran()
card1=ran()
sersum=card+card1
print(card,card1)
if(card==0):
	if(card1==0):
		card=11
		card1=1
	else:
		if(sersum<=10):
			card=11
		else:
			card=1
elif(card1==0):
	if(sersum<=10):
		card1=11
	else:
		card1=1
sersum=card+card1
client_count=0
list_of_clients=[]
print("check")
cnn, addr = serverSocket.accept()
print("check")
client_count+=1
card=ran()
card1=ran()
st=str(card)+"=>"+str(card1)
lc[client_count]=card+card1
list_of_clients.append(cnn)
cnn.send(st)
if(card==0):
	c=cnn.recv(2048)
	card=int(c)
if(card1==0):
	c=cnn.recv(2048)
	card1=int(c)

#cli = cnn.recv(1024)
#client_count+=1

#start_new_thread(b_j,(cnn,addr,client_count))

for i in range(1,client_count+1):
	flag="1"
	while(flag=="1"):
		if(lc[client_count]<=21):
			flag=list_of_clients[i-1].recv(2048)
			print('')
			print(type(flag),flag)
			if(flag=="1"):
				card=ran()
				#print("jsbvjkjshvdkjsdvbkj")
				card1=str(card)
				list_of_clients[i-1].send(card1)
				time.sleep(1)
				lc[i]+=card
				if(lc[i]>=21):
					flag="0"

while(sersum<=16):
	card=ran()
	#print(card)
	sersum+=card
	print(sersum)
if(sersum>21):
	sersum=0
	
for i in range(1,client_count+1):
	print("nbb")
	if(lc[i]<=21  and lc[i]>=sersum) or sersum==0:
		st1="You Win"
	else:
		st1="You Loose"
	list_of_clients[i-1].send(st1)

serverSocket.close()
