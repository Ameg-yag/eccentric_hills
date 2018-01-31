import socket
import sys
import os

HOST = ""
PORT = ""
DIRECTORY = os.path.dirname(os.path.realpath(__file__))
with open(DIRECTORY+"/help.txt", 'r') as inputhandle:
    HELPPROMPT = inputhandle.read()

def main():
    cmd = ""
    connection = socket.socket()

    while True:
        cmd = raw_input("Enter command. Type 'help' for options."+'\n').lower()

        if cmd == "help":
            print HELPPROMPT

        elif cmd == "connect":
            try:
                connection.connect((HOST, PORT))
            except socket.error:
                #Change this later to do something instead
                sys.exit(1)

        elif cmd == "quit":
            connection.shutdown(socket.SHUT_RDWR)
            connection.close()
            sys.exit(0)

        elif cmd == "ping":
            request = "ping"
            print "Sending: %s" % request
            try:
                connection.send(request)
            except:
                #Change later to do something instead
                sys.exit(1)
            #bufsize 4096
            response = client.recv(4096)
            print "Received: %s" % response

        else:
            print "Command not recognized."


if __name__ == '__main__':
    main()
