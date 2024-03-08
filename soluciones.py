# PREGUNTA 1
# Solicitar que ingrese su nombre de usuario
nombre_usuario = input('Por favor, ingrese su nombre de usuario: ')
# Mostrar un saludo al usuario después de haber ingresado su nombre
print('¡Hola',nombre_usuario +'!')

# PREGUNTA 2
# Solicitar al usuario que ingrese el monto de consumo y la cantidad de propina que desea dejar
monto_consumo = float(input('Ingrese el monto de su consumo: $'))
porcentaje_propina = float(input('Ingrese el porcentaje de propina que desea dejar (%): '))
# Calcular el porcentaje de propina
propina = monto_consumo * (porcentaje_propina / 100)
# Mostrar el resultado
print('La cantidad de dinero a dejar como propina es: $',propina)

# PREGUNTA 3
# Se solicita al vendedor que ingrese el número de payasos y muñecas que desea ordenar
numero_payasos = int(input('Introduzca el número de payasos que solicitan en el pedido: '))
numero_munecas = int(input('Introduzca el número de muñecas que solicitan en el pedido: '))
# Calcular el peso total del pedido
peso_muneca = 75 # peso en gramos
peso_payaso = 112 # peso en gramos
peso_total = (numero_munecas * peso_muneca) + (numero_payasos * peso_payaso)
# Mostrar el resultado
print('El peso total del paquete es:',peso_total,'gramos')

# PREGUNTA 4
# Solicitar al usuario ingresar un número entero positivo
n = int(input('Por favor, introduzca un número entero positivo: '))
# Calcular la suma de todos los enteros desde 1 hasta n
suma_total = n * (n + 1)/2
# Mostrar el resultado
print('La suma de todos los enteros de 1 hasta',n,'es:',suma_total)

# PREGUNTA 5
# Solicitar al usuario que ingrese el número de shows musicales que ha visto en el último año
numero_shows = int(input('Ingrese el número de shows musicales que ha visto en el último año: '))
# Almacenar el número de shows musicales vistos en una variable
mas_de_3_shows_vistos = numero_shows>3
# Mostrar si el usuario ha visto más de 3 shows musicales en el último año
print('¿Ha visto más de 3 shows musicales en el último año?',mas_de_3_shows_vistos)

# PREGUNTA 6
# Solicitar al usuario su edad 
edad = int(input('Por favor, ingrese su edad: '))
# Calcular el precio de la entrada que debe pagar el usuario en base a su edad
if edad < 4:
    precio_entrada = 'Gratis'
elif edad <= 18:
    precio_entrada = '$5'
else:
    precio_entrada = '$10'
# Mostrar precio de la entrada
print('El precio de entrada a pagar según su edad es',precio_entrada)

# PREGUNTA 7
# Solicitar al usuario ingresar dos números
print('Introduzca dos números')
numero_1 = float(input('Ingrese el primer número: '))
numero_2 = float(input('Ingrese el segundo número: '))
# Mostrar al usuario el menú de opciones 
print('Menú: ')
print('1. Mostrar suma de los dos números')
print('2. Mostrar la resta de los dos números (el primero menos el segundo)')
print('3. Mostrar la multiplicación de los dos números')
# Pedirle al usuario que introduzca la opción que desea ejecutar
opcion = input('Elije la opción 1, 2 o 3: ')
if opcion=='1':
    print('La suma de los números es igual a:',numero_1 + numero_2)
elif opcion=='2':
    print('La resta de los números es igual a:',numero_1 - numero_2)
elif opcion=='3':
    print('La multiplicación de los números es igual a:',numero_1 * numero_2)
else:
    print('La opción introducida no es válida')

# PREGUNTA 8
# Solicitar al usuario que indique la hora en formato hh:mm
hora = input('Por favor, ingrese la hora en formato hh:mm (24 horas): ')
# Extraer la hora y los minutos
hora_actual = int(hora.split(':')[0])
minutos_actual = int(hora.split(':')[1])
# Verificar si es hora de desayunar, almorzar o cenar
if hora_actual==7 or (hora_actual==8 and minutos_actual==0):
    print('Es hora de desayunar')
elif hora_actual==12 or (hora_actual==13 and minutos_actual==0):
    print('Es hora de almorzar')
elif hora_actual==18 or (hora_actual==19 and minutos_actual==0):
    print('Es hora de cenar')
else:
    pass

# PREGUNTA 9
lista = ['Di','buen','día','papá']
lista.reverse()
print('Lista invertida:',lista)

# PREGUNTA 10
lista_original =['Rojo','Verde','Blanco','Negro','Rosa','Amarillo']
lista_original.remove(lista_original[5])
lista_original.remove(lista_original[4])
lista_original.remove(lista_original[0])
print('Resultado:',lista_original)

# PREGUNTA 11
lista_duplicada = [1,1,2,3,4,4,5,1]
lista_procesada = set(lista_duplicada)
lista_nueva = list(lista_procesada)
print('Lista sin duplicados:',lista_nueva)

# PREGUNTA 12
# Solicitar al usuario que ingrese el nombre del archivo
archivo = input('Ingrese el nombre del archivo: ')
# Obtener la extensión
extension = archivo.lower().split('.')[-1]
# Definir el diccionario de extensiones y tipos de MIME correspondientes
extensiones_mime = {
'gif':'image/gif',
'jpg':'image/jpeg',
'jpeg':'image/jpeg',
'png':'image/png',
'pdf':'application/pdf',
'txt':'text/plain',
'zip':'application/zip'
}
# Obtener el tipo de MIME correspondiente
tipo_mime = extensiones_mime.get(extension,'application/octet-stream')
# Mostrar el resultado
print('El tipo MIME del archivo {} es: {}'.format(archivo,tipo_mime))