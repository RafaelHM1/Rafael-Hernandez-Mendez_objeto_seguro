import base64
from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import numpy as np

class ObjetoSeguro:
    #esta es una clase de objeto seguro
    #recibe el nombre en formato string
    def __init__(self,nombre):
        self.nombre = nombre
        
    def gen_llaves(self):
        #genera la llave privada y su correspondiente llave pública
        self.llave = RSA.generate(2048, Random.new().read)
        self.llave_pub = self.llave.publickey().exportKey("PEM")
        self.llave_priv = self.llave.exportKey("PEM")
        return self.llave_pub.decode(), self.llave_priv.decode()

    def llave_publica(self):
        #obtiene la llave pública del objeto seguro
        self.publica = self.gen_llaves()
        #self.llave_pub = self.publica.exportKey()
        self.pub_key = RSA.importKey(self.llave_pub.decode()) 
        return self.pub_key

    def codificar64(self,msj):
        #codifica el texto plano en base 64
        #retorna el mensaje en texto plano codificado en base64
        self.msj_bytes=str.encode(msj)
        self.msj_codificado = base64.b64encode(self.msj_bytes)
        return self.msj_codificado

    def cifrar_msj(self, pub_key, msj):
        #cifra un mensaje con la llave pública del destinatario
        #retorna mensaje cifrado
        self.cifrar = PKCS1_OAEP.new(pub_key)
        self.msj_cifrado = self.cifrar.encrypt(self.codificar64(msj))
        return self.msj_cifrado

    def saludar(self, name, msj):
        #método accedido por el objeto que quiere comenzar comunicación
        #Entradas: nombre del objeto y mensaje cifrado con la llave pública del destinatario
        self.saludo = self.cifrar_msj(self.pub_key,msj)
        print(f'{name} dice: {self.saludo}')
        return self.saludo

    def decodificar64(self,msj):
        #decodifica el mensaje en base64 en texto en claro
        #retorna el mensaje en texto en plano
        self.msj_descifrado = msj
        self.mensaje_decodificado = base64.decodebytes(self.descifrar_msj(msj))
        self.decodificado = self.mensaje_decodificado.decode()
        return self.decodificado
                
    def descifrar_msj(self, msj):
        #descifra el mensaje cifrado
        #retorna el mensaje en texto en plano codificado en base64
        self.priv_key = RSA.importKey(self.llave_priv.decode()) 
        self.descifrar = PKCS1_OAEP.new(self.priv_key)
        self.msj_cifrado = msj
        self.mensaje_descifrado = self.descifrar.decrypt(msj)
        return self.mensaje_descifrado

    def responder(self, msj):
        #se ejecuta al recibir un saludo de otro objeto seguro
        #Entradas: nombre del objeto al que se responderá
        #Salidas: mensaje recibido con el string "MensajeRespuesta"
        self.decodificado = msj
        self.respuesta = msj.join("MensajeRespuesta")
        self.cifrar_msj(self.pub_key,self.respuesta)

    def almacenar_msj(self,msj):
        #almacena en un archivo el texto claro del mensaje
        #asigna un ID para identificarlo
        #El retorno es el ID en formato {"ID":<id>}.
        #El mensaje y el ID es lo mínimo que debe tener el registro
        self.contador=0
        registro = {'ID': self.contador+1, 'Nombre: ':self.nombre, 'Mensaje: ': msj}
        np.save(f'RegistroMsj {self.nombre}.npy', registro)
        with open(f'RegistroMsj {self.nombre}.txt', 'w') as registros_txt:
            registros_txt.write(str(registro))
        return f'ID:<{self.contador}>'
        
    def consultar_msj(self,id):
        leer_archivo = np.load(f'RegistroMsj {self.nombre}.npy',allow_pickle=True).item()
        print(leer_archivo)

    def esperar_respuesta(self,msj):
        #espera una respuesta cifrada
        #debe llamar al método para almacenar el mensaje de respuesta recibido en texto plano
        self.almacenar_msj(msj)

persona1 = ObjetoSeguro('Diego')
persona2 = ObjetoSeguro('Alfonso')

llave_publica_persona1 = persona1.llave_publica()
llave_publica_persona2 = persona2.llave_publica()
persona1.saludar('Alfonso','Buen día Diego!')
persona1.esperar_respuesta('Respuesta')
persona2.responder('Hola!')
persona1.consultar_msj(1)


