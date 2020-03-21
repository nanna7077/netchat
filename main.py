  import os
import nt
import time
choice=0
sysname=""
def encrypter(msg):
    enc="$".join(msg)
    enc=enc[::-1]
    enc="&".join(enc)
    return enc

def decrypter(msg):
    lst1=msg.split("&")
    dec=""
    for a in lst1:
        dec=dec+a
    dec=dec[::-1]
    lst2=dec.split("$")
    str1=""
    for b in lst2:
        str1=str1+b
    return str1

def pass_check(passw):
    file=open("data.chtlog","r+")
    lst=file.readlines()
    pass1=int(decrypter(lst[0]))
    if pass1==int(passw):
        return
    else:
        print("       INVALID PASSWORD       ")
        time.sleep(2)
        m_menu()
        
def showmsgs():
    clrscr()
    count=0
    file=open("data.chtlog","r+")
    recentmsg=file.readlines()
    for line in recentmsg:
        if count==0:
            count+=1
        else:
            print(decrypter(line))
    file.close()
    
def close():
    time.sleep(5)
    exit()
    
def clrscr():
    nt.system("cls")
    
def header():
    print("===============================================================================")
    print("==                                      Network Chat                         ==")
    print("===============================================================================")

def footer():
    print("===============================================================================")
    print("==                                   Version 1.2.0                           ==")
    print("===============================================================================")

def seperator():
    print("===============================================================================")

def selection():
    global sysname
    global choice
    if choice==1:
        clrscr()
        header()
        ch_s1=input("Do you want to use this system as chat server?? (Warning! Existing chat data will be deleted if exists!!) y-yes n-no ")
        if ch_s1.lower()=='y':
            print("==                               Using current system name as chat server                      ==")
            sysname=
            try:
                os.chdir("C:\\Users\\Public\\CH_FILES\\")
            except:
                os.chdir("C:\\Users\\Public\\CH_FILES\\")
                os.mkdir("CH_FILES")
                os.chdir("C:\\Users\\Public\\CH_FILES\\")
            password=input("Set Chat password:  (Only numeric passwords are supported at the moment) \n")
            file.write(encrypter(password))
            file.write("\n")
            usrname=input("Enter your user name: ")
            print("Enter logout whenever you wish to leave chat")
            print("\n Press ENTER to refresh for new messages")
            for a in file:
                print(a.lstrip("\n"))
            msg=usrname+" has joined the chat"
            msg=encrypter(msg)
            file.write(msg)
            file.write("\n")
            file.close()
            while msg.lower()!="logout":
                showmsgs()
                file=open("data.chtlog","a+")
                msg=input("Enter msg: ")
                if msg=="" or msg==" ":
                    pass
                else:
                    file.write(encrypter(usrname+": "+msg))
                    file.write("\n")
                    file.close()
            clrscr()
            print("Logout successfull \n\n")
            file=open("data.chtlog","a+")
            file.write(encrypter(usrname+" logged out!"))
            file.close()
            time.sleep(5)
            m_menu()
        if ch_s1.lower()=='n':
            print("Enter system name to use as chat server: Example(SYSTEM36-PC) :")
            sysname=input("")
            try:
                os.chdir("\\\\"+sysname+"\\Users\\Public\\CH_FILES\\")
            except:
                try:
                    os.chdir("\\\\"+sysname+"\\Users\\Public\\")
                    os.mkdir("CH_FILES")
                    os.chdir("\\\\"+sysname+"\\Users\\Public\\CH_FILES\\")
                except:
                    print("Does system exist?? check")
                    time.sleep(5)
                    m_menu()
            file=open("data.chtlog","w+")
            password=input("Set Chat password:  (Only numeric passwords are supported at the moment) \n")
            file.write(encrypter(password))
            file.write("\n")
            usrname=input("Enter your user name: ")
            print("Enter logout whenever you wish to leave chat")
            print("\n Press ENTER to refresh for new messages")
            msg=usrname+"has joined the chat"
            file.write(encrypter(msg))
            file.write("\n")
            file.close()
            while msg.lower()!="logout":
                showmsgs()
                file=open("data.chtlog","a+")
                msg=input("Enter msg: ")
                if msg=="" or msg==" ":
                    pass
                else:
                    file.write(encrypter(usrname+": "+msg))
                    file.write("\n")
                    file.close()
            clrscr()
            print("Logout successfull \n\n")
            file=open("data.chtlog","a+")
            file.write(encrypter(usrname+" logged out!"))
            file.close()
            time.sleep(5)
            m_menu()

    if choice==2:
        clrscr()
        header()
        ch_s1=input("Do you want to use this system as chat server?? y-yes n-no ")
        if ch_s1.lower()=='y':
            print("==                               Using current system name as chat server                      ==")
            try:
                os.chdir("C:\\Users\\Public\\CH_FILES\\")
            except:
                os.chdir("C:\\Users\\Public\\CH_FILES\\")
                os.mkdir("CH_FILES")
                os.chdir("C:\\Users\\Public\\CH_FILES\\")
            file=open("data.chtlog","a+")
            password=input("Enter password: \n")
            pass_check(password)
            usrname=input("Enter your user name: ")
            print("Enter logout whenever you wish to leave chat")
            print("\n Press ENTER to refresh for new messages")
            time.sleep(2)
            for a in file:
                print(a.lstrip("\n"))
            msg=usrname+" has joined the chat"
            file.write(encrypter(msg))
            file.write("\n")
            file.close()
            while msg.lower()!="logout":
                showmsgs()
                file=open("data.chtlog","a+")
                msg=input("Enter msg: ")
                if msg=="" or msg==" ":
                    pass
                else:
                    file.write(encrypter(usrname+": "+msg))
                    file.write("\n")
                    file.close()
            clrscr()
            print("Logout successfull \n\n")
            file=open("data.chtlog","a+")
            file.write(encrypter(usrname+" logged out!"))
            file.close()
            time.sleep(5)
            m_menu()
        if ch_s1.lower()=='n':
            print("Enter system name to use as chat server: Example(SYSTEM36-PC) :")
            sysname=input("")
            try:
                os.chdir("\\\\"+sysname+"\\Users\\Public\\CH_FILES\\")
            except:
                print("File Not Found, Check System name")
                time.sleep(3)
                m_menu()
            file=open("data.chtlog","a+")
            password=input("Enter password: \n")
            pass_check(password)
            usrname=input("Enter your user name: ")
            print("Enter logout whenever you wish to leave chat")
            print("\n Press ENTER to refresh for new messages")
            msg=usrname+"has joined the chat"
            file.write(encrypter(msg))
            file.write("\n")
            file.close()
            while msg.lower()!="logout":
                showmsgs()
                file=open("data.chtlog","a+")
                msg=input("Enter msg: ")
                if msg=="" or msg==" ":
                    pass
                else:
                    file.write(encrypter(usrname+": "+msg))
                    file.write("\n")
                    file.close()
            clrscr()
            print("Logout successfull \n\n")
            file=open("data.chtlog","a+")
            file.write(encrypter(usrname+" logged out!"))
            file.close()
            time.sleep(2)
            m_menu()
    if choice==3:
        print("Delete chatfile? [Warning! UNRECOVERABLE! ] (y or n)")
        del_ch=input("\n")
        if del_ch.lower()=="y" and sysname!="":
            os.chdir("\\\\"+sysname+"\\Users\\Public\\")
            nt.system("del CH_FILES \\f")
        elif del_ch.lower()=="y":
            os.chdir("C:\\Users\\Public\\")
            nt.system("del CH_FILES \\f")
        else:
            header()
            print("==                                            Thank You                                                    ==")
            footer()
            close()

def m_menu():
    clrscr()
    header()
    print("==                             1. Start New Chat                              ==")
    print("==                             2. Continue Existing chat                      ==")
    print("==                             3. Exit                                        ==")
    seperator()
    print("==      Enter Option: ")
    global choice
    choice=int(input(""))
    selection()

m_menu()
