class pruebas (object):
   def __init__(self, string):
      self.string = string

   def imprimirClase(self):
      print(f"""El texto recibido es: {self.string}""")

instancia = pruebas("Texto de prueba")
instancia.imprimirClase()