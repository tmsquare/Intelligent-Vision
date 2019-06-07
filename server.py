import socket
import threading
import sys
#import RPi.GPIO as GPIO
import datetime
import random
import requests
import os
import subprocess
from time import sleep

#GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(11,GPIO.OUT)

host = ''
port = 8220
address = (host, port)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(address)
server_socket.listen(5)
#Variable for the number of connections
numbOfConn = 0

#Name of list used for connections
addressList = []
clients = set()
##############################################################################
#small database of our bot
questions = ["b'mouton'", "b'vache'"]
responses = ["reponse1", "reponse2"]

database={
    "b'test1'":'reponse  test 1',
    "b'test2'":'reponse test 2'
}

print ("Listening for client . . .")
###############################################################################
#chatbot code here
def chatbot(data):
    
    if data in database:
        print(database[data])
        #os.system("flite -t '"+ database[data] +"'")
        sclient(database[data].encode())
    elif data in questions:
        random_response = random.choice(responses)
        print(random_response)
        #os.system("flite -t '"+ random_response +"'")
        sclient(random_response.encode())
    elif 'heure' in data:
        now = datetime.datetime.now()
        time=str(now.hour)+str("hours")+str(now.minute)+str("minutes")
        print(time)
    
    ###############
    elif 'bonjour' in data:
        sclient(b"Bonjour. Comment allez vous ?")
    elif 'bonsoir' in data:
        sclient(b"Bonsoir. Comment allez vous ?")
    elif 'salut' in data:
        sclient(b"Salut. Comment allez vous ?")
        
    ################
    elif 'vais bien' in data:
        sclient(b"Je vais bien aussi merci.")
        
    ####################
    elif 'ton nom' in data:
        sclient(b"Je suis Intelligence Vision.")
        sleep(3)
        sclient(b"Je peux vous aider a vous informer sur le trafic actuel")
    elif 'votre nom' in data:
        sclient(b"Je suis Intelligence Vision.")
        sleep(3)
        sclient(b"Je peux vous aider a vous informer sur le trafic actuel")
    elif 'vous appelez' in data:
        sclient(b"Je suis Intelligence Vision.")
        sleep(3)
        sclient(b"Je peux vous aider a vous informer sur le trafic actuel")
    elif 'appelles' in data:
        sclient(b"Je suis Intelligence Vision.")
        sleep(3)
        sclient(b"Je peux vous aider a vous informer sur le trafic actuel")
    elif 'peux-tu faire' in data:
        sclient(b"Je suis Intelligence Vision.")
        sleep(3)
        sclient(b"Je peux vous aider a vous informer sur le trafic actuel")
    elif 'pouvez-vous faire' in data:
        sclient(b"Je suis Intelligence Vision.")
        sleep(3)
        sclient(b"Je peux vous aider a vous informer sur le trafic actuel")
    elif 'tu fais' in data:
        sclient(b"Je suis Intelligence Vision.")
        sleep(3)
        sclient(b"Je peux vous aider a vous informer sur le trafic actuel")
    elif 'vous faites' in data:
        sclient(b"Je suis Intelligence Vision.")
        sleep(3)
        sclient(b"Je peux vous aider a vous informer sur le trafic actuel")
       
    ##########################
    elif 'comment'  in data:
        sclient(b"C'est tres simple.")
        sleep(3)
        sclient(b"Dites moi juste le nom du carrefour.")
        sleep(3)
        sclient(b"Et je vous dirai la situation du trafic dans ce carrefour en ce moment.")
    elif 'dois-je'  in data:
        sclient(b"C'est tres simple.")
        sleep(3)
        sclient(b"Dites moi juste le nom du carrefour.")
        sleep(3)
        sclient(b"Et je vous dirai la situation du trafic dans ce carrefour en ce moment.")
    elif "m'aider"  in data:
        sclient(b"C'est tres simple.")
        sleep(3)
        sclient(b"Dites moi juste le nom du carrefour.")
        sleep(3)
        sclient(b"Et je vous dirai la situation du trafic dans ce carrefour en ce moment.")
    elif "allez y"  in data:
        sclient(b"C'est tres simple.")
        sleep(3)
        sclient(b"Dites moi juste le nom du carrefour.")
        sleep(3)
        sclient(b"Et je vous dirai la situation du trafic dans ce carrefour en ce moment.")
    elif "vas y"  in data:
        sclient(b"C'est tres simple.")
        sleep(3)
        sclient(b"Dites moi juste le nom du carrefour.")
        sleep(3)
        sclient(b"Et je vous dirai la situation du trafic dans ce carrefour en ce moment.")
        
    ##################    
    elif "quels sont"  in data:
        sclient(b"Je suis actuellement en phase test.")
        sleep(3)
        sclient(b"Je ne couvre qu'un seul carrefour pour le moment")
        sleep(3)
        sclient(b"Dites juste 'carrefour test' comme nom.")
    elif "carrefours"  in data:
        sclient(b"Je suis actuellement en phase test.")
        sleep(3)
        sclient(b"Je ne couvre qu'un seul carrefour pour le moment")
        sleep(3)
        sclient(b"Dites juste 'carrefour test' comme nom.")
    
    
    ####################
    elif "carrefour test"  in data:
        with open("chatbotdata.txt", "r") as f:
            b=f.read()
            
        sclient(b"Le carrefour test est actuellement saturer.")
        sleep(3)
        string = "Il y a un flux de plus de " + b + " voitures ces 30 dernieres minutes"
        sclient(string.encode())
    ####################
    elif "merci"  in data:
        sclient(b"Merci beaucoup a vous.")
        sleep(3)
        sclient(b"Je reste a votre disposition")
    elif "ok"  in data:
        sclient(b"Merci beaucoup a vous.")
        sleep(3)
        sclient(b"Je reste a votre disposition")
        
        
    
    elif 'prendre une photo' in data:
        myCmd = "sudo python /home/pi/Desktop/IntelligenceVision/Deploy/camera.py"
        
        p = subprocess.Popen(myCmd, shell=True)
        sclient(b"Traitement en cours")
    elif 'date'in data:
        now = datetime.datetime.now()
        date=str("%s/%s/%s" % (now.month,now.day,now.year))
        print(date)
        #os.system("flite -t '"+date+"'")
        sclient(date.encode())
    else:
        conn.send(b"Veuillez recommencer s'il vous plait..")
        add_data = open("newdata.txt", 'a')
        add_data.write("\n")
        add_data.write(data)
        add_data.close()
###############################################################################
#Sending Reply to all clients
def sclient(mess):
    for c in clients:
        try:
            c.send(mess)
        except:
            c.close()
##############################################################################
#server code here
def clientthread(conn,addressList):
#infinite loop so that function do not terminate and thread do not end.
     while True:
        output = conn.recv(2048);
        if output.strip() == "disconnect":
            conn.close()
            sys.exit("Received disconnect message.  Shutting down.")
            conn.send("connection loss")
        elif output:
            print ("Message received from client:")
            data=str(output).lower()
            print (data)
            print("Reply from the server:")
            chatbot(data)

while True:
#Accepting incoming connections
    conn, address = server_socket.accept()
    print ("Connected to client at ", address)
    clients.add(conn)
#Creating new thread. Calling clientthread function for this function and passing conn as argument.
    threading.Thread(target=clientthread,args=(conn,addressList)).start() #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.

conn.close()
sock.close()   
