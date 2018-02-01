import socket
import sys
import os

#Might want to change default port at some point
PORT = 6669
CURR_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
with open(CURR_DIRECTORY+"/help.txt", 'r') as inputhandle:
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
                print "Failed to connect to host IP."
                userChoice = raw_input("Exit? Y/N"+'\n').lower()
                if userChoice == "y":
                    sys.exit(0)

        elif cmd == "quit":
            try:
                connection.shutdown(socket.SHUT_RDWR)
                connection.close()
            except:
                print("No connection to close. Terminating program.")
            sys.exit(0)

        else:
            print "Command not recognized."


if __name__ == '__main__':
    main()
