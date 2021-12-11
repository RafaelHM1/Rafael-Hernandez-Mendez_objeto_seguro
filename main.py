from proyecto import ObjetoSeguro

persona1 = ObjetoSeguro('Diego')
persona2 = ObjetoSeguro('Alfonso')

persona1.gen_llaves()
persona2.gen_llaves()

llave_publica_persona2 = persona2.llave_publica()
llave_publica_persona1 = persona1.llave_publica()

persona1.saludar('Alfonso','Buen día Diego!')
persona1.esperar_respuesta('Respuesta')
persona2.responder('Hola!')