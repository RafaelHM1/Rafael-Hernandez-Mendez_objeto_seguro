import base64
from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


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
        self.msj_cifrado = self.cifrar.encrypt(msj)
        return self.msj_cifrado
    
    def saludar(self, name, msj):
        #método accedido por el objeto que quiere comenzar comunicación
        #Entradas: nombre del objeto y mensaje cifrado con la llave pública del destinatario
        self.name = name
        self.msj = msj
        self.responder(msj)

    def responder(self, msj):
        #se ejecuta al recibir un saludo de otro objeto seguro
        #Entradas: nombre del objeto al que se responderá
        #Salidas: mensaje recibido con el string "MensajeRespuesta"
        pass
    
    def descifrar_msj(self, msj):
        #descifra el mensaje cifrado
        #retorna el mensaje en texto en plano codificado en base64
        self.priv_key = RSA.importKey(self.llave_priv.decode()) 
        self.descifrar = PKCS1_OAEP.new(self.priv_key)
        self.mensaje_descifrado = self.descifrar.decrypt(msj)
        return self.mensaje_descifrado
                
    def decodificar64(self,msj):
        #decodifica el mensaje en base64 en texto en claro
        #retorna el mensaje en texto en plano
        self.mensaje_decodificado = base64.decodebytes(msj)
        self.msj = self.mensaje_decodificado.decode()
        return self.msj

    def almacenar_msj(self,msj):
        #almacena en un archivo el texto claro del mensaje
        #asigna un ID para identificarlo
        #El retorno es el ID en formato {"ID":<id>}.
        #El mensaje y el ID es lo mínimo que debe tener el registro

        #with open('llave_privada.txt', 'w') as objeto_archivo:
        #objeto_archivo.write(llave_privada.decode())
       
        pass

    def consultar_msj(self,id):
        #consula un mensaje en el registro usando ID asignado
        #Formato: {"ID":"id", MSJ: "Mensaje_consultado", "campo1":"valor1"}
        #with open('llave_privada.txt') as objeto_archivo:
        #contenido_privado = objeto_archivo.read()
        pass

    def esperar_respuesta(self,msj):
        #espera una respuesta cifrada
        #debe llamar al método para almacenar el mensaje de respuesta recibido en texto plano
        pass

persona1 = ObjetoSeguro('Diego')
persona2 = ObjetoSeguro('Alfonso')

persona1.gen_llaves()
persona2.gen_llaves()

llave_publica_persona2 = persona2.llave_publica()
llave_publica_persona1 = persona1.llave_publica()

persona1.codificar64('Buen día Alfonso!')
persona1.cifrar_msj(llave_publica_persona2, persona1.msj_codificado)
persona1.saludar('Diego',persona1.msj_cifrado)

persona2.descifrar_msj(persona1.msj_cifrado)
persona2.decodificar64(persona2.mensaje_descifrado)
print(persona2.msj)

#print(persona1.msj_cifrado)
#print(persona2.mensaje_descifrado)
#print(persona1.llave_pub)
#print(persona1.llave_priv)



#print(persona2.llave_pub)
#print(persona2.llave_priv)

  