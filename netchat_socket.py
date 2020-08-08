#!/usr/bin/env python3
import sys
import socket
import os
import datetime
import sys
msg_storage=[]
conn,s=None,None
choice=port=0
def clrscr():
    if os.name=='nt':
        os.system("cls")
    else:
        os.system("clear")

def getmsgs():
    global conn,s
    clrscr()
    if len(msg_storage)==0:
        pass
    else:
        for x in msg_storage:
            if x!="" or x!=" ":
                sender,msg=x.split("~~!@#")
                print(sender+": "+msg+"\n\n")
    print("\n\n\n Waiting for Message... \n\n")
    incoming_mssg=conn.recv(1024)
    incoming_mssg=incoming_mssg.decode()
    if incoming_mssg[:7]=="!!MEOUT":
        msg,usr=incoming_mssg.split('++')
        print("\n "+usr+" left the chat!")
        exit(1)
    else:
        sender,msg=str(incoming_mssg).split("~~!@#")
        clrscr()
        print("Got Message! \n\n")
        print(sender+": "+msg)
        msg_storage.append(str(incoming_mssg))
        
def getmsg():
    global s
    clrscr()
    if len(msg_storage)==0:
        pass
    else:
        for x in msg_storage:
            if x!="" or x!=" ":
                sender,msg=x.split("~~!@#")
                print(sender+": "+msg+"\n\n")
    print("\n\n Waiting for message...")
    incoming_mssg=s.recv(1024)
    incoming_mssg=incoming_mssg.decode()
    if incoming_mssg[:7]=="!!MEOUT":
        msg,usr=incoming_mssg.split('++')
        print("\n "+usr+" left the chat!")
        exit(1)
    else:
        sender,msg=str(incoming_mssg).split("~~!@#")
        clrscr()
        print("\n\n Got Message! \n\n\n")
        print(sender+": "+msg)
        msg_storage.append(str(incoming_mssg))

def main(choice,port):
    global s,conn
    if choice==1:
        host=[l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0]
        s=socket.socket()
        print("Hosted by:",host)
        s.bind((host,port))
        print("Waiting for connection...")
        s.listen(5) 
        conn,addr=s.accept() 
        print("Connected!")
        name=input("Enter your name: ")
        print("\n\n\n")
        while True:
            message=input(str(name+": "))
            if message.lower()=='exit':
                conn.send(str("!!MEOUT++"+name).encode())
                s.close()
                clrscr()
                exit(1)
            msg=name+"~~!@#"+message
            if message=="":
                continue
            else:
                msg_storage.append(str(msg))
                msg=msg.encode()
                conn.send(msg)
                getmsgs()

    if choice==2:
        s=socket.socket()
        host= input(str("Enter IP to connect to: "))
        s.connect((host,port))
        print("Connected")
        name=input("\n Enter your name:")
        getmsg()
        while True:
            message=input(str(name+": "))
            if message.lower()=='exit':
                s.send(str("!!MEOUT++"+name).encode())
                s.close()
                clrscr()
                exit(1)
            msg=name+"~~!@#"+message
            if message=="":
                continue
            else:
                msg_storage.append(msg)
                msg=msg.encode()
                s.send(msg)
                getmsg()
if __name__=='__main__':
    choice=sys.argv[1]
    port=sys.argv[2]
    main(int(choice),int(port))
