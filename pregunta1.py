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




# PREGUNTA 6
# Solicitar al usuario que ingrese cuántos shows musicales ha visto en el último año
shows_vistos = int(input("Por favor, ingresa cuántos shows musicales has visto en el último año: "))

# Mostrar el número ingresado por el usuario
print("Número de shows musicales vistos en el último año:", shows_vistos)

# Verificar si el usuario ha visto más de 3 shows y almacenar el resultado en una variable booleana
ha_visto_mas_de_3_shows = shows_vistos > 3

# Mostrar si el usuario ha visto más de 3 shows
print("¿Has visto más de 3 shows musicales en el último año?:", ha_visto_mas_de_3_shows)