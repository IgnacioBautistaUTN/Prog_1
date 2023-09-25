'''1-	Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.'''
palabra = input('Ingrese una palabra: ')
print(10* palabra) 
'''2-	Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos 
los años que ha cumplido (desde 1 hasta su edad).'''
edad = int(input('Ingrese su edad: '))
for i in range(1,edad+1):
    print(i)
'''3-	Escribir un programa que pida al usuario un número entero positivo y
muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.'''
numero = int(input('Ingrese un número entero positivo: '))
if numero>0:
    numeros_impares= '1' 
    for i in range(2,numero+1):
        if i%2!=0:
            i = str(i)
            numeros_impares = numeros_impares + ', ' + i
print (numeros_impares)
'''4-	Escribir un programa que pida al usuario un número entero positivo 
y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.'''
numero = int(input('Ingrese un número entero positivo: '))
if numero>0:
    for i in range(numero,-1,-1):
        print(i, end=', ')
'''5-	Escribir un programa que pregunte al usuario una cantidad a invertir, 
el interés anual y el número de años, y muestre por pantalla el capital obtenido en la 
inversión cada año que dura la inversión.'''
cantidad_a_invertir = float(input('Ingrese la cantidad a invertir: '))
interes_anual = float(input('Ingrese el interes anual: '))
numeros_anios = int(input('Ingrese el número de años: '))
for i in range(numeros_anios+1):
    capital_obtenido = (cantidad_a_invertir * interes_anual)/100
    cantidad_a_invertir = cantidad_a_invertir + capital_obtenido
    print(f'Capital obtenido en el año {i} es {capital_obtenido}')
'''6-	Escribir un programa que pida al usuario un número entero 
y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.'''
numero = int(input('Ingrese un número entero: '))
altura = abs(numero)
for i in range(0,altura+1):
    print(i*'*')
'''7-	Escribir un programa que muestre por pantalla las tablas de multiplicar del 1 al 10.'''
for i in range(1,11):
    for n in range(1,11):
        resultado = i * n
        print(f'{i} x {n} = {resultado}')
'''8-	Escribir un programa que pida 
al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.'''
numero = int(input('Ingrese un número entero: '))
altura = abs(numero)
sumatoria = ''
for i in range(0,altura+1):
    if i%2!=0:
        i = str(i)
        sumatoria += i + ' '
        print (sumatoria[::-1])
#Otra manera de resolver el problema:
'''numero = int(input('Ingrese un número entero: '))
altura = abs(numero)
sumatoria = ''
for i in range(0,altura+1):
    if i%2!=0:
        i = str(i)
        sumatoria = i + ' ' + sumatoria
        print (sumatoria)'''
'''9-	Escribir un programa que almacene la cadena de caracteres contraseña en una 
variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.'''
contrasenia = input('Ingrese la contraseña: ')
while contrasenia!='contraseña':
    contrasenia = input('Ingrese la contraseña: ')
print ('Contraseña correcta!')
'''10-	Escribir un programa que pida al usuario 
un número entero y muestre por pantalla si es un número primo o no.'''
numero = int(input('Ingrese un número entero: '))
divisores = 0
for divisor in range(1,numero+1):
    if numero%divisor==0:
        divisores += 1
if divisores==2:
    print ('ES UN NÚMERO PRIMO')
'''11-	Escribir un programa que pida al usuario una palabra 
y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.'''
palabra = input('Ingrese una palabra: ')
palabra_invertida = ''
for letra in palabra:
    palabra_invertida = letra + palabra_invertida
for i in palabra_invertida:
    print(i)
'''12-	Escribir un programa en el que se pregunte al usuario por una frase y 
una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.'''
frase = input('Ingrese una frase: ')
frase = frase.lower()
letra = input('Ingrese una letra: ')
letra = letra.lower()
sumatoria = 0
if len(letra)==1:
    for i in frase:
        if i == letra:
            sumatoria += 1
print(f'La letra {letra} aparece {sumatoria} en la frase')
'''13-	Escribir un programa que muestre el 
eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.'''
palabra = input('Ingrese una palabra: ')
palabra = palabra.lower()
while palabra != 'salir':
    print (10*palabra)
    palabra = input('Ingrese una palabra: ')
    palabra = palabra.lower()
'''14-	Escriba un programa que pida dos números 
enteros y escriba qué números son pares y cuáles impares desde el primero hasta el segundo.'''
primer_numero = int(input('Ingrese el primer número: '))
segundo_numero = int(input('Ingrese el segundo número: '))
if primer_numero%2==0:
    print(f'El número {primer_numero} es par')
else: 
    print(f'El número {primer_numero} es impar')
if segundo_numero%2==0:
    print(f'El número {segundo_numero} es par')
else: 
    print(f'El número {segundo_numero} es impar')
'''15-	Escriba un programa que pida un número entero mayor que cero y que escriba sus divisores.'''
numero = int(input('Ingrese un número entero mayor que cero:'))
divisores = ''
if numero>0:
    for i in range(1,numero+1):
        if numero%i==0:
            i = str(i)
            divisores = divisores + ' ' + i
print(f'Los divisores de {numero} son {divisores}')
'''16-	Escriba un programa que pregunte 
cuántos números se van a introducir, pida esos números y escriba cuántos negativos ha introducido.'''
cantidad_numeros = int(input('Ingrese cuantos números va a introducir: '))
cantidad_numeros_negativos = 0
for i in range(0,cantidad_numeros):
    numero = int(input('Ingrese el número: ')) 
    if numero<0:
        cantidad_numeros_negativos +=1
print(f'Ingresó {cantidad_numeros_negativos} números negativos')
'''17-	Solicitar al usuario que ingrese una frase y 
luego imprimir un listado de las vocales que aparecen en esa frase (sin repetirlas).'''
frase = input('Ingrese una frase: ')
vocales = 'aeiou'
vocales_que_aparecen = ''
for letra in frase:
    if letra in vocales and letra not in vocales_que_aparecen:
        vocales_que_aparecen = vocales_que_aparecen + ' ' + letra
print(f'Las vocales que aparecen en la frase son {vocales_que_aparecen}')
'''18-	Crear un algoritmo que muestre los primeros 10 números de la sucesión de Fibonacci. 
La sucesión comienza con los números 0 y 1 y, a partir de éstos, cada elemento es la suma de 
los dos números anteriores en la secuencia: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…'''
a = 0
b = 1
print(a, b, end=' ')
for i in range(11):
    c = a + b
    a = b
    b = c
    print (c, end=' ')
'''19-	Escriba un programa que simule una alcancía. El programa solicitará primero una cantidad, 
que será la cantidad de dinero que queremos ahorrar. A continuación, el programa solicitará una y 
otra vez las cantidades que se irán ahorrando, hasta que el total ahorrado iguale o supere al objetivo. 
El programa deberá comprobar que las cantidades ingresadas sean positivas.'''
cantidad_a_ahorrar = float(input('Ingrese la cantidad que desea ahorrar: '))
total_ahorrado = 0
while True:
    cantidad_a_ahorrar = float(input('Ingrese la cantidad que desea ahorrar: '))
    if cantidad_a_ahorrar>0:
        break
while total_ahorrado<cantidad_a_ahorrar:
    ingrese_ahorro = float(input('Ingrese el monto ahorrado: '))
    if ingrese_ahorro>0:
        total_ahorrado = total_ahorrado + ingrese_ahorro
    else:
        print('El monto ingresado es incorrecto')
print(f'El monto ahorrado es {total_ahorrado}')
'''20-	Leer números enteros de teclado, hasta que el 
usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números ingresados.'''
sumatoria_numeros = 0
while True:
    numero = int(input('Ingrese un número: '))
    sumatoria_numeros = sumatoria_numeros + numero
    if numero==0:
        break
print(sumatoria_numeros)
'''21-	Leer números enteros positivos de teclado, 
hasta que el usuario ingrese el 0. Informar cuál fue el mayor número ingresado.'''
num_mayor = 0
while True:
    numero = int(input('Ingrese un número entero positivo: '))
    if numero>0:
        if numero>num_mayor:
            num_mayor = numero
    elif numero<0:
        print('Ingreso un número negativo')
    else: 
        break
print(f'El mayor número ingresado fué {num_mayor}')
'''22-	Solicitar al usuario que ingrese números enteros positivos y, por cada uno, 
imprimir la suma de los dígitos que lo componen. La condición de corte es que se ingrese el 
número -1. Al finalizar, mostrar cuántos de los números ingresados por el usuario fueron números pares.'''
sumatoria_numeros_pares = 0
while True:
    numero = int(input('Ingrese un número entero positivo (Si desea salir del programa ingrese -1): '))
    if numero>=0:
        if numero%2==0:
            sumatoria_numeros_pares += 1
        numero = str(numero)
        n = len(numero)
        suma_digitos = 0
        for digito in range(0,n):
            digito_numero = numero[digito]
            digito_numero = int(digito_numero)
            suma_digitos = suma_digitos + digito_numero
        print(f'El número ingresado fué {numero} y la suma de sus digitos es {suma_digitos}')
    elif numero<-1:
        print('Ingreso un número negativo')
    else: 
        print(f'De los números enteros positivos ingresados {sumatoria_numeros_pares} fueron pares. Muchas gracias!')
        break
'''23-	Crear un programa que permita al usuario ingresar los montos de las compras de un cliente 
(se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución), cortando el 
ingreso de datos cuando el usuario ingrese el monto 0.'''
while True:
    monto_compra = float(input('Ingrese el monto de la compra (para finalizar el ingreso de datos digite 0): '))
    if monto_compra==0:
        break
'''24-	Si ingresa un monto negativo, no se debe procesar y se debe pedir que ingrese un nuevo monto. 
Al finalizar, informar el total a pagar teniendo que cuenta que, si las ventas superan el total 
de $1000, se le debe aplicar un 10% de descuento.'''
total_a_pagar = 0
while True:
    monto_compra = float(input('Ingrese el monto de la compra (para finalizar el ingreso de datos digite 0): '))
    total_a_pagar = total_a_pagar + monto_compra
    if monto_compra<0:
        print('Monto incorrecto, ingrese nuevamente')
    if monto_compra==0:
        if total_a_pagar>1000:
            total_a_pagar = total_a_pagar*0.9
        print(f'El total a pagar es {total_a_pagar}')
        break
'''25-	Dado un número entero positivo, mostrar su factorial. El factorial de un número se obtiene 
multiplicando todos los números enteros positivos que hay entre el 1 y ese número. 
El factorial de 0 es 1.'''
numero = int(input('Ingrese un número entero positivo: '))
factorial = 1
if numero>0:
    for i in range(1,numero+1):
        factorial = factorial * i
    print(factorial)
elif numero==0:
    print(factorial)
else:
    print('Ingreso un número negativo')