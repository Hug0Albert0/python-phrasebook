nombres = 'Hugo Alberto'
apellido_paterno = "Rivera"
apellido_materno = """Díaz"""

mensaje = """
   Este es un mensaje para demostrar el uso de comillas triples en Python
"""

saludo = "Bienvenido, {nombre} {apellido_pat} {apellido_mat}".format(
   nombre = nombres,
   apellido_pat = apellido_paterno,
   apellido_mat = apellido_materno
)

#Python 2.6
print(saludo)
valor_uno = 150.56
valor_dos = 37.22
print("Si multiplicamos 150 x 37 el resultado es {resultado}".format(
   resultado = valor_uno * valor_dos
))

#Python3
print(f"Hola, tu nombre es {nombres}. You are {nombres} {apellido_paterno} {apellido_materno}.")
print(f"Si multiplicamos 150 x 37 el resultado es = {150.56 * 37.22}")