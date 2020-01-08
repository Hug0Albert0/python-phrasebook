diccionario = {
   "nombre": "Hugo",
   "apellido": "Rivera",
   "edad": 18,
   "capital": 11500.75
}

print(diccionario)
"""
   Si afuera se usan comillas dobles, las de dentro deben ser simples y viceversa, aplica tambien
   para comillas triples
"""
print(f"""
   Mi nombre completo es {diccionario["nombre"]} {diccionario["apellido"]}, tengo {diccionario["edad"]}
   y actualmente cuento con un capital de ${diccionario["capital"]}
 """)

#Generando datos con listas y diccionarios. Su implementacion es vital en aplicaciones/sistemas que
#ocupen la integracion con una base de datos.

productos_precio = []

productos = [
   "Leche",
   "Galletas",
   "Aceite",
   "Jabon",
   "Agua"
]

precios = [
   23.00,
   12.50,
   13.66,
   9.54,
   10.00
]

for indice, producto in enumerate(productos):
   coleccion = {} #Puede declararse como coleccion = dict ()
   coleccion["nombre"] = producto
   coleccion["precio"] = precios[indice]
   productos_precio.append(coleccion)

print(productos_precio)

