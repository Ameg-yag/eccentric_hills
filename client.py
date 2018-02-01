import socket
import sys
import os

PORT = "6669"
DIRECTORY = os.path.dirname(os.path.realpath(__file__))
with open(DIRECTORY+"/help.txt", 'r') as inputhandle:
    HELPPROMPT = inputhandle.read()

def main():
    connection = socket.socket()

    while True:
        cmd = raw_input("Enter command. Type 'help' for options."+'\n').lower()

        if cmd == "help":
            print HELPPROMPT

        elif cmd == "connect":
            host = raw_input("Enter host IP address: ")
            try:
                connection.connect((host, PORT))
            except socket.error:
                #Change this later to do something instead
                sys.exit(1)

        elif cmd == "quit":
            connection.shutdown(socket.SHUT_RDWR)
            connection.close()
            sys.exit(0)

        else:
            print "Command not recognized."


if __name__ == '__main__':
    main()
