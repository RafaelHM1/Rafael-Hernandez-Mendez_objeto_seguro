import socket
import threading
import base64
from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import numpy as np

class Servidor:
    def __init__(self, host, puerto, usuario):
        self.__HOST = host
        self.__PUERTO = puerto
        self.usuario = usuario
        self.CONEXIONES=[]
        self.USUARIOS=[]

    def configurar_conexion(self):
        self.servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.servidor.bind((self.__HOST, self.__PUERTO))
        self.servidor.listen()
        print(f"Servidor funcionando {self.__HOST}:{self.__PUERTO}") #nomás pa decir que funciona
        return self.servidor

    def enviar_mensaje(self,mensaje,conexion_envio):
        for conexion in self.CONEXIONES:
            if conexion != conexion_envio:
                conexion.send(mensaje)

    def gestiona_usuarios(self,conexion):
        while True:
            try:
                mensaje = conexion.recv(1024)
                self.enviar_mensaje(mensaje,conexion)
            except:
                indice = self.CONEXIONES.index(conexion)
                self.usuario = self.USUARIOS[indice]
                self.enviar_mensaje(f"{self.usuario} se fue :(".encode("utf-8"),conexion)
                self.CONEXIONES.remove(conexion)
                conexion.close()
                break
    
    def recibir_peticiones(self):
        while True:
            lo_que_sea=self.configurar_conexion()
            conexion, dir_IP = lo_que_sea.accept()
            conexion.send("Dame tu usuario".encode("utf-8"))
            usuario = conexion.recv(1024).decode("utf-8")

            self.CONEXIONES.append(conexion)
            self.USUARIOS.append(usuario)

            print(f"{usuario} está conectado")

            mensaje = f"El usuario {usuario} se unió a la conversasión".encode("utf-8")
            self.enviar_mensaje(mensaje,conexion)
            conexion.send("Conectado al servidor".encode("utf-8"))

persona1 = Servidor('127.0.0.1',5000,'Rafael')
persona1.recibir_peticiones()


