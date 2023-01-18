import os
import socket


s = socket.socket()
port = 8080 
host = "YOUR IP OR HOSTNAME" #Add your Hostname or your IP adress
s.connect((host, port))
print("")
print("Connectted to the server successfuly")
print("")
while True:
    command = s.recv(1024)
    command = command.decode()
    print("Command recieved")
    print("")
    # send the client.py directory to the server 
    if command == "view_cwd": 
        files = os.getcwd()
        files = str(files)
        s.send(files.encode())
        print("Command has been succesfuly executed...")
    # Navigate into Client device
    elif command == "custom_dir":
        user_input = s.recv(5000)
        user_input = user_input.decode()
        files = os.listdir(user_input)
        files = str(files)
        s.send(files.encode())
        print("")
        print("Command has been executed succesfully...")
        print("")
    elif command == 'exit':
        break
    else:
        print("")
        print("Command not reconised")
