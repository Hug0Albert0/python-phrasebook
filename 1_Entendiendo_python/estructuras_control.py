#Estructura if
variable = True
if variable == True:
   print("La variable es verdadera")

salario_semanal = 5000
if salario_semanal > 5000:
   print("Ganas bien")
elif salario_semanal < 5000:
   print("No ganas tanto")
else:
   print("Ganas exactamente 5000 pesos")

#Estructura while
indice = 1
while indice < 100:
   indice += 1
print(indice)

#Ciclo for
palabra = "Python"
lista = []
for letra in palabra:
   print(letra)
   lista.append(letra)
print(lista)
#Implementacion con range()
print("Contemos hasta 10")
for elemento in range(1, 11):
   print(elemento)