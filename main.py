#!/usr/bin/env python3
import netchat_socket
import socket
import platform
import os
import subprocess
if platform.system().lower()=='linux':
    linux=True
    nt=False
    mac=True
elif platform.system().lower()=='windows':
    linux=False
    nt=True
    mac=False
elif platform.system().lower()=='darwin':
    linux=False
    nt=False
    mac=True
using_ports=[]
base_port=1900
if linux:
    x=os.system("xterm")
    if x==0:
        pass
    else:
        print("Please install \'xterm\' to continue!")
        exit(1)
while True:
    print("\n\n\t Inter-Network Chat Program \n\n\t\t 1.Start New Chat \n\n\t 2.Join New Chat \n\n\t 3.Exit")
    ch=int(input('\n ?'))
    if ch==1:
        if using_ports==[]:
            port=base_port
            using_ports.append(base_port)
            if nt:
                subprocess.call('python netchat_socket.py '+str(ch)+' '+str(port), creationflags=subprocess.CREATE_NEW_CONSOLE)
            elif linux:
                subprocess.call('xterm -r \'python3 netchat_socket.py '+str(ch)+' '+str(port)+'\'')
            elif mac:
                subprocess.call(['open', '-W', '-a', 'Terminal.app', 'python','netchat_socket.py '+str(ch)+' '+str(port)]) #EXPERIMENTAL!!!!!!
        else:
            port=base_port
            while port in using_ports:
                port+=10
            using_ports.append(port)
            if nt:
                subprocess.call('python netchat_socket.py '+str(ch)+' '+str(port), creationflags=subprocess.CREATE_NEW_CONSOLE)
            elif linux:
                subprocess.call('xterm -r \'python3 netchat_socket.py '+str(ch)+' '+str(port)+'\'')
            elif mac:
                subprocess.call(['open', '-W', '-a', 'Terminal.app', 'python','netchat_socket.py '+str(ch)+' '+str(port)]) #EXPERIMENTAL!!!!!!
    elif ch==2:
        if using_ports==[]:
            port=base_port
            using_ports.append(base_port)
            if nt:
                subprocess.call('python netchat_socket.py '+str(ch)+' '+str(port), creationflags=subprocess.CREATE_NEW_CONSOLE)
            elif linux:
                subprocess.call('xterm -r \'python3 netchat_socket.py '+str(ch)+' '+str(port)+'\'')
            elif mac:
                subprocess.call(['open', '-W', '-a', 'Terminal.app', 'python','netchat_socket.py '+str(ch)+' '+str(port)]) #EXPERIMENTAL!!!!!!
        else:
            port=base_port
            while port in using_ports:
                port+=10
            using_ports.append(port)
            if nt:
                subprocess.call('python netchat_socket.py '+str(ch)+' '+str(port), creationflags=subprocess.CREATE_NEW_CONSOLE)
            elif linux:
                subprocess.call('xterm -r \'python3 netchat_socket.py '+str(ch)+' '+str(port)+'\'')
            elif mac:
                subprocess.call(['open', '-W', '-a', 'Terminal.app', 'python','netchat_socket.py '+str(ch)+' '+str(port)]) #EXPERIMENTAL!!!!!!
    else:
        exit(0)
