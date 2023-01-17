import os
import socket

s = socket.socket()
host = socket.gethostname()
port = 8080
s.bind((host, port))
print("")
print(" Sever is curently running @", host)
print("")
print("Waiting for incoming connection...")
s.listen(1)
conn, addr = s.accept()
print("")
print(addr, " Has connected to the server successfully")

while True:
    command = input(str("Command >>"))
    # Ask the client device where is client.py 
    if command == "view_cwd":
        conn.send(command.encode())
        print("")
        print("COmmand sent waiting for execution...")
        print("")
        files = conn.recv(5000)
        files = files.decode()
        print("Command output :", files)
    # Let the server navigate into the client device
    elif command == "custom_dir":
        conn.send(command.encode())
        print("")
        user_input = input(str("Custom dir : "))
        conn.send(user_input.encode())
        print("")
        print("COmmand has been sent")
        print("")
        files = conn.recv(5000)
        files = files.decode()
        print("Custom dir", files)
    elif command == "exit":
        conn.send(command.encode())
        print("")
        print("COmmand sent waiting for execution...")
        print("")
        break
    else :
        print("Command not reconized")
        
