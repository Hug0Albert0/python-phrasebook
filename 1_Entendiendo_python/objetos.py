lista = [1, 2, 3]
print(lista)
print (id(lista))
print (type(lista))

class prueba (object):
   def imprimirNumero(self):
      print(self.num)

objeto_prueba = prueba()
objeto_prueba.num = 75
objeto_prueba.imprimirNumero()