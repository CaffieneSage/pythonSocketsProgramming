import sys
import socket



try:
    conSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created!")

except:
    print("Socket Failed!")



port = int(input())
try:
    host_ip = socket.gethostbyname('www.google.com')

except socket.gaierror:
    print("Cannot resolve host!")
    sys.exit()

conSock.connect((host_ip, port))
print("Connection succesful!")
print(host_ip, port)










    
