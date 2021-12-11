from proyecto import ObjetoSeguro

persona1 = ObjetoSeguro('Diego')
persona2 = ObjetoSeguro('Alfonso')

llave_publica_persona2 = persona2.llave_publica()
llave_publica_persona1 = persona1.llave_publica()

persona1.saludar('Alfonso','Buen día Diego!')
persona2.saludar('Diego','Que tal Alfonso')

persona1.esperar_respuesta('Respuesta')
persona2.esperar_respuesta('Hola')
persona2.consultar_msj(1)