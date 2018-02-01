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
        server_reply = conn.recv(4096)

        if server_reply == "quit":
            connection.shutdown(socket.SHUT_RDWR)
            connection.close()
            break

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
                server_data = listen(connection)
            except socket.error:
                print "Failed to connect to host IP."
                userChoice = raw_input("Exit? Y/N"+'\n').lower()
                if userChoice == "y":
                    sys.exit(0)

        elif cmd == "quit":
            try:
                connection.send("quit")
<<<<<<< HEAD
                connection.shutdown(socket.SHUT_RDWR)
                connection.close()
=======
>>>>>>> 4a8af7e0da74928c942ab7606d6c5ba13418bbdf
            except:
                print "No connection to close. Terminating program."
            sys.exit(0)

        else:
            print "Command not recognized."


if __name__ == '__main__':
    main()
