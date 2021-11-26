from os import sendfile
import sys
import socket
import select as slt
import time
sys.path.append('/home/mask/workspace/bahiart-openaigym')

from server.proxy import Proxy
from server.agentParser import AgentParser


# TO RUN TYPE : python3 runProxy.py <agentConnectionPort>
# Ex: python3 runProxy.py 3300
#proxy = Proxy(int(sys.argv[1]))
#proxy = Proxy(3500)

#  -------------------- OPTION 1 ------------------------
# TO RUN THE PROXY
#proxy.start()


file = open("/home/mask/workspace/gymOut.txt", "w")
file.write("PYTHON\n")
file.close()

# print("starting...")
# while True:
#     msg = proxy.getMessagesFromAgent('1')
#     if(msg):
#         print(msg[0])
#     print('\n')
#     print("Message List Size: " + str(len(msg)))
#     print('\n')
#     time.sleep(5)

#  -------------------- TESTE COM SOCKET -----------------
# HOST = "localhost"
# PORT = 4200

# teamSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# teamSock.bind((HOST, PORT))
# print("GYM BIND.")
    
# teamSock.listen() 
# newTeamSock, _ = teamSock.accept()
# print("GYM ACCEPT")

# while True:
#     newTeamSock.send("teste".encode())
#     print("GYM SENT")
#Check if a message was received with a timeout of 5 seconds
    # ready = slt.select([sock], [], [], 5)
    # if not ready[0]:
    #     continue
    #print('')
    #msg = newAgentSock.recv(1024)
    #print(msg.decode())

# ------------------------ FIM DO TESTE -------------------





######Intance Parser
# parser = AgentParser()
# agent = None
# while True:
#     #lista = proxy.getMessagesFromAgent('1')
#     if agent == None:
#         agent = proxy.getPlayerObj('1')
#     else:
#         if agent.getUnum() == None:
#             pass
#         else:
#             pass
#             print(agent.neckYaw)

#  -------------------- OPTION 2 ------------------------
# TO RUN THE PROXY IN ANOTHER THREAD AND STILL BE ABLE TO CALL 
# ANOTHER FUNCTIONS WITHOUT BEING STUCK IN THE START FUNCTION.

# IN THIS WAY, WE CAN RECEIVE THE MESSAGES FROM A SPECIFIC AGENT
# proxy.main()

# while True:
#    msg = proxy.getMessagesFromAgent('1')
#    if msg != '':
#        print(msg)
#        print("\n")
