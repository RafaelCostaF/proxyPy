from server.player import Player
import socket
from server.agentProxy import AgentProxy
import threading
import time

class Proxy:


    def __init__(self,agent_port,server_port=3100,server_host='localhost'):

        self.SERVER_HOST = server_host
        self.SERVER_PORT = server_port
        self.AGENT_PORT = agent_port

        self.agentSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.agentSock.bind((self.SERVER_HOST, self.AGENT_PORT))
   
        self.proxies = []

    def start(self):
        threading._start_new_thread(self.main,())

    def getMessagesFromAgent(self,agentNumber:str):
        messages = []
        for x in range(len(self.proxies)):
            if self.proxies[x].getAgentNumber() == agentNumber:
                messages = self.proxies[x].getAgentMessages()
        
        self.verifyAgent(agentNumber)
        return messages
    
    def getPlayerObj(self,agentNumber:str):
        for x in range(len(self.proxies)):
            if self.proxies[x].getAgentNumber() == agentNumber:
                player = self.proxies[x].getPlayerObj()
                self.verifyAgent(agentNumber)
                return player
        
        self.verifyAgent(agentNumber)
        return

    def verifyAgent(self,agentNumber:str):
        for x in range(len(self.proxies)):
            if self.proxies[x].getAgentNumber() == agentNumber:
                if not self.proxies[x].getIsConnected():
                    self.proxies.remove(self.proxies[x])

    def main(self):
        while True:
            self.agentSock.listen()
            newAgentSock, _ = self.agentSock.accept()

            try:
                pxy = AgentProxy(newAgentSock,self.SERVER_PORT,self.SERVER_HOST)
                pxy.connectionManager()
                self.proxies.append(pxy)
                print("[PROXY] New agent connected on port : " + str(self.AGENT_PORT))
            except:
                print("[PROXY] Couldn't connect new agent.")