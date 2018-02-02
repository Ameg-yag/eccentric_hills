import socket
import sys
import os

#Might want to change default port at some point
PORT = 6669
CURR_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
with open(CURR_DIRECTORY+"/help.txt", 'r') as inputhandle:
    HELPPROMPT = inputhandle.read()

def listen(connection):
    while True:

        #response from server
        buffer = ""
        while "^-^" not in buffer:
            buffer += connection.recv(4096)
        buffer = buffer[0:(len(buffer)-5)]
        print buffer
        command = raw_input()
        if command == 'quit':
            connection.send("quit")
            break
        else:
            connection.send(command)

def main():
    connection = socket.socket()
    print HELPPROMPT
    while True:
        cmd = raw_input("ECHI> ").lower()

        if cmd == "help":
            print HELPPROMPT

        elif cmd == "connect":
            host = raw_input("Enter server IP address: ")
            try:
                connection.connect((host, PORT))
                connection.send("gunclawpythonratniBBa")
                server_data = listen(connection)
            except socket.error:
                print "Failed to connect to host IP."
                userChoice = raw_input("Exit? Y/N"+'\n').lower()
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
