import socket
import sys
from thread import *
from ConfigParser import SafeConfigParser

# initializing config.ini 
config = SafeConfigParser()
config.read('config.ini')
 
HOST = ''   #  all available interfaces
PORT = 8888 
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'
 
#Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error , msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
     
print 'bind complete..'
 
#Start listening on socket
s.listen(10)
print 'listening..'
 
# creating threads
def clientthread(conn):

    
    #infinite loop so keep server alive
    while True:
         
        #Receiving from client
	conn.send('enter server IP \n')
	sip = conn.recv(1024) # server ip
	conn.send('enter username \n')
	user = conn.recv(1024) # username
	conn.send('enter password \n')
	passw = conn.recv(1024) # password
	conn.send('enter program to execute \n')
	execu = conn.recv(1024) # program execute

  #      data = conn.recv(1024)
  #      reply = 'you said' + data
#	print "received data:", data
   #     if not data: 
   #         break
 	
	if config.get('user1', 'server') in sip and config.get('user1', 'user') in user and config.get('user1', 'password') in passw and config.get('user1', 'exec') in execu:
	 conn.send("Executing Program 1 \n")
	 execfile("programs/user1.py")

	if config.get('user2', 'server') in sip and config.get('user2', 'user') in user and config.get('user2', 'password') in passw and config.get('user2', 'exec') in execu:
	 conn.send("Executing Program 2 \n")
	 execfile("programs/user2.py")

	if config.get('user3', 'server') in sip and config.get('user3', 'user') in user and config.get('user3', 'password') in passw and config.get('user3', 'exec') in execu:
	 conn.send("Executing Program 3 \n")
	 execfile("programs/user3.py")

	if config.get('user4', 'server') in sip and config.get('user1', 'user4') in user and config.get('user4', 'password') in passw and config.get('user4', 'exec') in execu:
	 conn.send("Executing Program 4 \n")
	 execfile("programs/user4.py")

	else:
	 conn.send("Incorrect Credentials, please try again! \n")
	

	
 
       # conn.sendall(reply)
     
   
    conn.close()
 
#now keep talking with the client
while 1:
    #  accept a connection 
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
     

    start_new_thread(clientthread ,(conn,))
 
s.close()
