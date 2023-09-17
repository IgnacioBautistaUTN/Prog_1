'''1.Calcular el perimetro y area de un rectangulo dada su base y su altura'''
base = float(input('Ingrese la longitud de la base del rectángulo (en cm): '))
altura = float(input('Ingrese la altura del rectángulo (en cm): '))
perimetro = 2 * base + 2 * altura
area = base * altura
print(f'El perímetro del rectángulo es: {perimetro}cm y su área es: {area}cm²')
'''2.Dados los catetos de un triángulo rectángulo calcular su hipotenusa'''
cateto1 = float(input('Ingrese la longitud del primer cateto (en cm): '))
cateto2 = float(input('Ingrese la longitud del segundo cateto (en cm):'))
hipotenusa = (cateto1**2 + cateto2**2)**(1/2)
print(f'La longitud de la hipotenusa es: {round(hipotenusa,2)}cm.')
'''3.Dado dos números mostrar la suma, resta, multiplicación y división de ambos.'''
numero1 = float(input('Ingrese el primer número: '))
numero2 = float(input('Ingrese el segundo número: '))
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2
print(f'La suma entre ambos números es: {suma}, la resta entre ambos números es: {resta}, la división entre ambos números es: {division} y la multiplicación entre ambos números es: {multiplicacion}.')
'''4.Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius. Recordar que la fórmula para la conversión es: C= (F-32)*5/9'''
valor_fahrenheit = float(input('Ingrese la temperatura en grados Fahrenheit: '))
valor_celsius = (valor_fahrenheit - 32)*5/9
print(f'La temperatura ingresada en grados Fahrenheit es: {valor_fahrenheit} y dicha temperatura expresada en grados Celsius es: {valor_celsius}.')
'''5.¿Que problemas tienen las siguientes instrucciones?¿Como las solucionarías?'''
'''a) Primero que se definió a la variable con una letra mayuscula lo cuál no está recomendado, 
segundo si quisiera que el usuario ingrese su nombre y su cancion favorita deberia hacerlo de otra manera: 
nombre, cancion_favorita = str(input('Ingrese su nombre: ')),str(input('¿Cuál es su canción favorita? '))'''
'''b) El error es que cuando se le pidió al usuario ingresar el precio, no se utilizo el metodo float o int 
por lo que al intentar utilizar la variable en un procedimiento matemático nos salta error porque no se puede 
operar con variables tipo string'''
'''c) El error esta en el print. Solución: 
edad = int(input(Edad: ))
print(f'Tu edad es {edad})'''
'''d) Para corroborar si la edad ingresada por el usuario es igual a 18 deberia hacerse por medio de un 'if'. Solución:
edad = int(input('Edad: '))
if edad == 18:
    print('Usted tiene 18 años!')
else:
    print(f'Usted no tiene 18 años, usted tiene {edad} años')'''
'''6. Calcular la media de tres números pedidos por teclado.'''
primer_numero = float(input('Ingrese el primer número: '))
segundo_numero = float(input('Ingrese el segundo número: '))
tercer_numero = float(input('Ingrese el tercer número: '))
media = (primer_numero + segundo_numero + tercer_numero) / 3
print(f'La media de los tres números ingresados es: {media}')
'''7. Realizar un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas 
horas y minutos corresponde. Por ejemplo: 1000 minutos son 16 horas y 40 minutos.'''
minutos = int(input('Ingrese la cantidad de minutos: '))
if minutos % 60 == 0:
    print(f'{minutos} minutos son {minutos // 60} horas.')
else:
    print(f'{minutos} minutos son {minutos // 60} horas y {(minutos % 60)} minutos.')
'''8. Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, el vendedor desea saber
cuanto dinero obtendrá por concepto de comisiones por las tres ventas que realiza en el mes y el total que recibirá 
en el mes tomando en cuenta su sueldo base y comisiones.'''
primer_venta = float(input('Ingrese el monto de su primer venta: '))
segunda_venta = float(input('Ingrese el monto de su segunda venta: '))
tercer_venta = float(input('Ingrese el monto de su tercer venta: '))
sueldo_base = float(input('Ingrese su sueldo base (sin comisiones): '))
comision_mensual = (primer_venta + segunda_venta + tercer_venta)*0.1
sueldo_total = sueldo_base + comision_mensual
print(f'Su comisión mensual es {round(comision_mensual,2)} y su sueldo total es {round(sueldo_total,2)}')
'''9. Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuanto 
deberá pagar finalmente por su compra'''
valor_inicial_compra = float(input('Ingrese el monto inicial de la compra: '))
print(f'El monto final a pagar es ${(valor_inicial_compra)*0.85}')
'''10. Un alumno desea saber cual será su calificación final en la materia de Algoritmos. Dicha calificación se 
compone de los siguientes porcentajes: -55% del promedio de sus tres calificaciones parciales. 
-30% de la calificación del examen final. -15% de la calificación de un trabajo final.'''
primer_parcial, segundo_parcial, tercer_parcial, examen_final, trabajo_final = int(input('Ingrese la nota del primer parcial: ')),int(input('Ingrese la nota del segundo parcial: ')),int(input('Ingrese la nota del tercer parcial: ')),int(input('Ingrese la nota del examen final: ')),int(input('Ingrese la nota del trabajo final: '))
if 0<=primer_parcial<=10 and 0<=segundo_parcial<=10 and 0<=tercer_parcial<=10 and 0<=examen_final<=10 and 0<=trabajo_final<=10:
    calificacion_final = 0.55 * ((primer_parcial + segundo_parcial + tercer_parcial)/3) + 0.30 * (examen_final) + 0.15 * (trabajo_final)
    print(f'Su calificación final es: {calificacion_final}')
else: 
    print(f'Ingresó una nota incorrectamente')
'''11. Pide al usuario dos números y muestra la 'distancia' entre ellos 
(el valor absoluto de su diferencia, de modo que el resultado sea siempre positivo.)'''
numero1 = float(input('Ingrese el primer número: '))
numero2 = float(input('Ingrese el segundo número: '))
distancia_numeros = abs(numero1 - numero2)
print(f'La distancia entre ambos números es {distancia_numeros}')
'''12.	Realizar un algoritmo que lea un número y que muestre su raíz cuadrada y su raíz cúbica.'''
numero = float(input('Ingrese un número: '))
print(f'El cuadrado del número ingresado es: {numero**2}')
print(f'El cubo del número ingresado es: {numero**3}')
'''13.	Dado un número de dos cifras, diseñe un algoritmo que permita obtener el número invertido. 
Ejemplo, si se introduce 23 que muestre 32.'''
numero = int(input('Ingrese un número entero de dos cifras: '))
if 10<=numero<=99:
    numero = str(numero)
    numero = numero[1] + numero[0]
    print(f'El inverso del número ingresado es: {numero}')
else: 
    print('El número ingresado no es válido')
'''14.	Dadas dos variables numéricas A y B, que el usuario debe teclear, 
se pide realizar un algoritmo que intercambie los valores de ambas variables y 
muestre cuanto valen al final las dos variables.'''
variableA = float(input('Ingrese el valor de A, su primer variable numerica: '))
variableB = float(input('Ingrese el valor de B, su segunda variable numerica: '))
variableC = variableA
variableA = variableB
variableB = variableC
print(f'El valor de su variable A es: {variableA} y el valor de su variable B es: {variableB}')
'''15.	Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. 
El tiempo de viaje hasta llegar a otra ciudad B es de T segundos. 
Escribir un algoritmo que determine la hora de llegada a la ciudad B.'''
print('Ingrese el horario de partida del ciclista (formato HH horas MM minutos SS segundos): ')
horas_partida, minutos_partida, segundos_partida = int(input('horas: ')), int(input('minutos: ')), int(input('segundos: '))
tiempo_viaje = int(input('Ingrese el tiempo de viaje (en segundos): '))
horas_viaje = tiempo_viaje // 3600
minutos_viaje = (tiempo_viaje % 3600)//60
segundos_viaje = (tiempo_viaje % 3600)%60
print(f'El tiempo de viaje fue: {horas_viaje} horas, {minutos_viaje} minutos, {segundos_viaje} segundos')
hora_llegada = horas_partida + horas_viaje
minutos_llegada = minutos_partida + minutos_viaje
segundos_llegada = segundos_partida + segundos_viaje
if segundos_llegada>59:
    segundos_llegada = segundos_llegada % 60
    minutos_llegada = minutos_llegada + 1 
if minutos_llegada>59:
    minutos_llegada = minutos_llegada % 60 
    hora_llegada = hora_llegada + 1 
print(f'El ciclista llego a las: {hora_llegada} horas, {minutos_llegada} minutos, {segundos_llegada} segundos')
'''16.	Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales.'''
nombre = input('Ingrese su nombre: ')
primer_apellido, segundo_apellido = input('Ingrese su primer apellido: '), input('Ingrese su segundo apellido: ')
print(f'Las iniciales de su nombre y apellidos son: {nombre[0]}{primer_apellido[0]}{segundo_apellido[0]}')
'''17.	Solicitar al usuario que ingrese su nombre. El nombre se debe almacenar en una variable 
llamada usuario. A continuación mostrar por pantalla: “Ahora estás en la matrix, [nombre del usuario]”.'''
usuario = input('Ingrese su nombre: ')
print(f'Ahora estas en la matrix, {usuario}')
'''18.	Hacer un programa que solicite al usuario cuánto costó una cena en un restaurante. A ese valor, 
sumarle un 6.2% en concepto de servicio y un 10% de propina. Imprimir en pantalla el monto final a pagar.'''
costo_inicial = float(input('Ingrese el monto inicial a pagar de la cena: '))
costo_final = costo_inicial + costo_inicial*0.062 + costo_inicial*0.1
print(f'El monto final a pagar es ${costo_final}')
'''19.	Solicitar al usuario que ingrese el día, mes y año de su nacimiento y almacenar cada uno 
de ellos en una variable numérica (en total, tres variables diferentes). 
Finalmente, mostrar la fecha en formato dd/mm/aaaa.'''
dia_nacimiento, mes_nacimiento, anio_nacimiento = int(input('Ingrese el día de nacimiento(formato DD): ')), int(input('Ingrese el mes de su nacimiento(formato MM): ')), int(input('Ingrese el año de su nacimiento(formato AAAA): '))
print(f'Su fecha de nacimiento es: {dia_nacimiento}/{mes_nacimiento}/{anio_nacimiento}')
'''20.	Hacer otra versión del programa, 
pero esta vez almacenado todo en una única variable con formato DDMMAAA.'''
fecha_nacimiento = input('Ingrese su fecha de nacimiento(formato DDMMAAAA): ')
print(f'Su fecha de nacimiento es: {fecha_nacimiento[0]}{fecha_nacimiento[1]}/{fecha_nacimiento[2]}{fecha_nacimiento[3]}/{fecha_nacimiento[4]}{fecha_nacimiento[5]}{fecha_nacimiento[6]}{fecha_nacimiento[7]}')
'''21.	Una pareja de motociclistas necesita hacer ciertos cálculos antes de emprender un viaje en moto, 
para saber cuántos tanques de combustible consumirá el viaje entero.
Para eso deben ingresar: cuántos kilómetros puede recorrer su moto con 1 litro de combustible, 
qué capacidad (en litros) tiene el tanque y cuántos kilómetros en total recorrerán.
Hacer un programa que solicite los datos necesarios y luego informe la cantidad de tanques de 
combustible necesarios.'''
km_autonomia = int(input('Ingrese la cantidad de kilometros que puede recorrer con un litro: '))
capacidad_moto = int(input('Ingrese la capacidad de litros de nafta que tiene su moto: '))
km_recorridos = int(input('Ingrese la cantidad de kilometros que recorrerán: '))
cantidad_tanques = (km_recorridos / km_autonomia)/capacidad_moto
print(f'Usted necesita {round(cantidad_tanques,2)} tanques de combustibles para realizar su viaje.')
