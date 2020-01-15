def funcion (argumento):
   print(f"""
      Has ejecutado la funcion y como argumento le has pasado el valor: {argumento}
   """)

funcion(True)
funcion("Hola")
funcion(123456)

def funcion_parametro_default(nombre = "Usuario"):
   print(f"Bienvenido al sistema: {nombre}")

funcion_parametro_default()
funcion_parametro_default("Hugo")

valores = {
   "nombre": "Litro de Agua 1L",
   "precio": 12.50,
   "stock_actual": 20
}

def funcion_diccionario_parametros(nombre, precio, stock_actual):
   print(f"""
      El producto {nombre} cuesta ${precio} y cuenta con un stock actual de {stock_actual}
      """)

funcion_diccionario_parametros(**valores)

def calculo_iva(cantidad):
   return cantidad * 0.16

cantidad_ejemplo = 120.00
iva_cantidad_ejemplo = calculo_iva(cantidad_ejemplo)

print(cantidad_ejemplo)
print(iva_cantidad_ejemplo)