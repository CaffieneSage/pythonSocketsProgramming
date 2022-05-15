import sys
import socket


#create our socket using black magic. Or not.
try:
    conSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created!")

except:
    print("Socket Failed!")


#store an int value for our port.
conPort = int(input())
#bind the socket to a loccal connection via inputted port.
conSock.bind(('', conPort))
print("Socket bound to %s" %(conPort))

#Listen.
conSock.listen(5)
print("Socket listening")

#create a loop so we can keep listening on the port.
while True:
    #????
    client, address = conSock.accept()
    print('Connected to %s' %address)
    #Profit.
    client.send('Thanks for connecting!'.encode())

    client.shutdown()
    client.close()

    break

    












    
