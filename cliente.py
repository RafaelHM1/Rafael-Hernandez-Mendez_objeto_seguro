import socket
import threading
import base64
from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import numpy as np

class Cliente:
    def __init__(self, host, puerto, usuario):
        self.__HOST = host
        self.__PUERTO = puerto
        self.usuario = usuario

    def configurar_conexion(self):
        self.cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.cliente.connect((self.__HOST, self.__PUERTO))
        return self.cliente

    def recibe(self):
        #mensaje=conexion.recv(1024).decode("utf-8")
        pass
        
    def envia(self):
        pass


persona2 = Cliente('127.0.0.1',5000,'Diego')
persona2.configurar_conexion()