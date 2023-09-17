'''1-	Crear un programa que reciba el número de años que tiene nuestra computadora y muestre 
en la consola que el computador es nuevo si es menor o igual a 2 años y que el computador 
es viejo si es mayor a 2 años.'''
años_computador = int(input('Ingrese el número de años que tiene nuestra computadora: '))
if 0<=años_computador<=2:
    print('El computador es nuevo')
elif años_computador>2:
    print('El computador es viejo')
'''2-	Hacer que el programa anterior muestre un mensaje de error si el usuario digita un número negativo.'''
if años_computador<0:
    print('Error, ingresó un número negativo')
'''3-	Solicitar al usuario que ingrese los nombres de dos personas, los cuales se almacenarán en dos
 variables. A continuación. Imprimir 'coincidencia' si ambos nombres comienzan con la misma letra. 
 Si no es así, imprimir 'no hay coincidencia'.'''
primer_nombre, segundo_nombre = input('Ingrese el nombre de la primer persona: '), input('Ingrese el nombre de la segunda persona: ')
primer_nombre = primer_nombre.title()
segundo_nombre = segundo_nombre.title()
if primer_nombre[0]==segundo_nombre[0]:
    print('Coincidencia')
else:
    print('No hay coincidencia')
'''4-	Crear un programa que permita al usuario elegir un candidato por el cual votar. 
Las posibilidades son: candidato A por el partido rojo, candidato B por el partido verdad, 
candidato C por el partido azul.
Según el candidato elegido (A, B o C) se debe imprimir el mensaje: 
'Usted ha votado por el partido [color del candidato elegido].
Si el usuario ingresa una opción que no corresponde a ninguno de los candidatos disponibles, 
indicar 'Opción errónea.'
'''
candidato_votado = input('Ingrese que candidato quiere votar(A,B o C): ')
candidato_votado = candidato_votado.title()
if candidato_votado=='A':
    print('Usted ha votado por el candidato del partido rojo')
elif candidato_votado=='B':
    print('Usted ha votado por el candidato del partido verde')
elif candidato_votado=='C':
    print('Usted ha votado por el candidato del partido azul')
else:
    print('Opción errónea')
'''5-	Escribir un programa que solicite al usuario una letra, si es una vocal, mostrar el 
mensaje 'Es vocal'.
Se debe validar que el usuario ingrese sólo un carácter. Si ingresa un string de más de un carácter, 
informarle que no se puede procesar el dato.'''
letra = (input('Ingrese una letra: '))
letra = letra.title()
if len(letra)==1:
    if letra=='A' or letra=='E' or letra=='I' or letra=='O' or letra=='U':
        print('Es vocal')
    elif letra=='-9' or letra=='-8' or letra=='-7' or letra=='-6' or letra=='-5' or letra=='-4' or letra=='-3' or letra=='-2' or letra=='-1' or letra=='0' or letra=='9' or letra=='8' or letra=='7' or letra=='6' or letra=='5' or letra=='4' or letra=='3' or letra=='2' or letra=='1':
        print('No se puede procesar el dato')
    else: 
        print('No es vocal')
if len(letra)!=1:
    print('No se puede procesar el dato')
'''6-	Hacer un programa que permita saber si un año es bisiesto. Para que un año sea bisiesto 
debe ser divisible por 4 y no debe ser divisible por 100, excepto que también sea divisible por 400.'''
anio = int(input('Ingrese el año: '))
if anio%4==0 and anio%100!=0 and anio%400!=0:
    print('Es año bisiesto')
else:
    print('No es año bisiesto')
'''7-	Escribí un programa para solicitar al usuario tres números y mostrar en pantalla al 
menor de los tres.'''
primer_numero, segundo_numero, tercer_numero = float(input('Ingrese el primer número: ')), float(input('Ingrese el segundo número: ')), float(input('Ingrese el tercer número: '))
menor_numero = 0
if primer_numero<segundo_numero:
    menor_numero = primer_numero
else: 
    menor_numero = segundo_numero
if segundo_numero>tercer_numero:
    menor_numero = tercer_numero
print(f'El menor número es {menor_numero}')
'''8-	Escribí un programa que solicite ingresar un nombre de usuario y una contraseña. 
Si el nombre es “Gwenevere” y la contraseña es “excalibur”, mostrar en pantalla “Usuario y 
contraseña correctos. Puede ingresar a Camelot”. Si el nombre o la contraseña no coinciden, 
mostrar “Acceso denegado”.'''
usuario = input('Ingrese su nombre de usuario: ')
contrasenia = input('Ingrese su contraseña: ')
if usuario=='Gwenevere' and contrasenia=='excalibur':
    print('Usuario y contraseña correctos. Puede ingresar a Camelot')
else: 
    print('Acceso denegado')
'''9-	Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. 
El grupo A está formado por las mujeres con un nombre anterior a la M y los hombres con un nombre 
posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, 
y muestre por pantalla el grupo que le corresponde.'''
nombre = input('Ingrese su nombre: ')
sexo = input('Ingrese su sexo (hombre o mujer): ')
nombre = nombre.title()
sexo = sexo.title()
if (sexo=='Mujer' and (nombre[0]=='A' or nombre[0]=='B' or nombre[0]=='C' or nombre[0]=='D' or nombre[0]=='E' or nombre[0]=='F' or nombre[0]=='G' or nombre[0]=='H' or nombre[0]=='I' or nombre[0]=='J' or nombre[0]=='K' or nombre[0]=='L')) or (sexo=='Hombre' and (nombre[0]=='Ñ' or nombre[0]=='O' or nombre[0]=='P' or nombre[0]=='Q' or nombre[0]=='R' or nombre[0]=='S' or nombre[0]=='T' or nombre[0]=='U' or nombre[0]=='V' or nombre[0]=='W' or nombre[0]=='X' or nombre[0]=='Y' or nombre[0]=='Z')):
    print('Pertenece al grupo A')
else: 
    print('Pertenece al grupo B')
'''10-	Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere
calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe 
preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 
4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar $500 y si es mayor de 18 años, $1000.'''
edad = int(input('Ingrese su edad: '))
if 0<=edad<4:
    print('Puede ingresar gratis')
if 4<=edad<18:
    print('Debe pagar $500') 
if 18<=edad:
    print('Debe pagar $1000')
'''11-	La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los 
ingredientes para cada tipo de pizza aparecen a continuación.
•	Ingredientes vegetarianos: Pimiento y tofu.
•	Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su 
respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede elegir un 
ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar 
por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.'''
tipo_de_pizza = input('Bienvenidos, seleccione que tipo de pizza quiere (regular o vegetariana): ')
tipo_de_pizza = tipo_de_pizza.title()
if tipo_de_pizza=='Regular':
    print('Todas nuestras pizzas contienen mozzarella y tomate')
    print('Elija que ingrediente desea agregarle a su pizza(solo puede seleccionar un ingrediente extra): ')
    agregado = input('1.Peperoni 2.Jamon 3.Salmon: ')
    agregado = agregado.title()
    if agregado=='Peperoni' or agregado=='1':
        print('Usted seleccionó una pizza regular con agregado de Peperoni')
    if agregado=='Jamon' or agregado=='2':
        print('Usted seleccionó una pizza regular con agregado de Jamon')
    if agregado=='Salmon' or agregado=='3':
        print('Usted seleccionó una pizza regular con agregado de Salmon')
elif tipo_de_pizza=='Vegetariana':
    print('Todas nuestras pizzas contienen mozzarella y tomate')
    print('Elija que ingrediente desea agregarle a su pizza(solo puede seleccionar un ingrediente extra): ')
    agregado = input('1.Pimiento 2.Tofu: ')
    agregado = agregado.title()
    if agregado=='Pimiento' or agregado=='1':
        print('Usted seleccionó una pizza regular con agregado de Pimiento')
    if agregado=='Tofu' or agregado=='2':
        print('Usted seleccionó una pizza regular con agregado de Tofu')
else:
    print('Opción incorrecta')
'''12-	Escriba un programa que pida el año actual y un año cualquiera y que escriba cuántos años han 
pasado desde ese año o cuántos años faltan para llegar a ese año.'''
anio_actual = int(input('Ingrese el año actual: '))
anio_cualquiera = int(input('Ingrese un año (pasado o futuro): '))
diferencia_anios = abs(anio_actual - anio_cualquiera)
if anio_actual<anio_cualquiera:
    print(f'Faltan {diferencia_anios} años para llegar a ese año.')
elif anio_actual>anio_cualquiera:
    print(f'Han pasado {diferencia_anios} años desde ese año')
else:
    print('Usted ingresó el mismo año')
'''13-	Escriba un programa que pida dos números enteros y que escriba si el mayor es múltiplo del 
menor. Haciendo que el programa avise cuando se escriben valores negativos o nulos.'''
primer_numero = int(input('Ingrese un número entero: '))
segundo_numero = int(input('Ingrese otro número entero: '))
if primer_numero<=0 or segundo_numero<=0:
    print('Ingreso valor/es negativos o nulos')
else:
    if primer_numero>segundo_numero:
        if primer_numero%segundo_numero==0:
            print(f'El número {primer_numero} es múltiplo de {segundo_numero}')
        else:
            print(f'El número {primer_numero} no es múltiplo de {segundo_numero}')
    if primer_numero<segundo_numero:
        if segundo_numero%primer_numero==0:
            print(f'El número {segundo_numero} es múltiplo de {primer_numero}')
        else:
            print(f'El número {segundo_numero} no es múltiplo de {primer_numero}')
    if primer_numero==segundo_numero:
        print('Ingreso los mismos números')
'''14-	Escriba un programa que pida los coeficientes de una ecuación de primer grado (a x + b = 0) 
y escriba la solución.'''
print('Dada la ecuación: a x + b = 0. Escriba los coeficientes: ')
a = float(input('Ingrese el coeficiente a: '))
b = float(input('Ingrese el coeficiente b: '))
x = 0
if a==0:
    print('La ecuación no tiene solución')
else:
    x = -b / a 
    print(f'La solución es {x}')
'''15-	Escriba un programa que pregunte primero si se quiere calcular el área de un triángulo o la de
 un círculo. Si se contesta que se quiere calcular el área de un triángulo (escribiendo T o t), el 
 programa tiene que pedir entonces la base y la altura y escribir el área. Si se contesta que se quiere 
 calcular el área de un círculo (escribiendo C o c), el programa tiene que pedir entonces el radio y 
 escribir el área.'''
figura = input('Elija de que figura quiere calcular el área, un triángulo (ingresando t o T) o un círculo (ingresando c o C): ')
if figura=='T' or figura=='t':
    base, altura = float(input('Ingrese la longitud de la base del triángulo(en cm): ')), float(input('Ingrese la longitud de la altura del triángulo(en cm): '))
    area = (base*altura)/2
    print(f'El área del triángulo es {area}cm²')
elif figura=='C' or figura=='c':
    radio = float(input('Ingrese el radio del círculo(en cm): '))
    import math
    area = math.pi*(radio**2)
    print(f'El área del círculo es {area}cm²')
else:
    print('Opción incorrecta')
'''16-	Haz una calculadora básica pida al usuario dos valores, a y b.
Según la opción que desean, realizar la operación:
•	Si operación es 1 entonces debemos ver el resultado de a + b
•	Si operación es 2 entonces debemos ver el resultado de a * b
•	Si operación es 3 entonces debemos ver el resultado de a - b
•	Si operación es 4 entonces debemos ver el resultado de a / b
'''
a = float(input('Ingrese el valor de "a": '))
b = float(input('Ingrese el valor de "b": '))
print('Seleccione la operación que desea realizar:')
operacion = input('Opción 1 (Suma) - Opción 2 (Multiplicación) - Opción 3 (Resta) - Opción 4 (División): ')
if operacion=='1':
    resultado = a + b
    print(f'El resultado es {resultado}')
elif operacion=='2':
    resultado = a * b
    print(f'El resultado es {resultado}')
elif operacion=='3':
    resultado = a - b
    print(f'El resultado es {resultado}')
elif operacion=='4':
    resultado = a / b
    print(f'El resultado es {resultado}')
else:
    print('Opción incorrecta')
'''17-	Requerir al usuario que ingrese un día de la semana e imprimir un mensaje si es lunes, 
otro mensaje diferente si es viernes, otro mensaje diferente si es sábado o domingo. Si el día 
ingresado no es ninguno de esos, imprimir otro mensaje.'''
dia = input('Ingrese que día de la semana es: ')
dia = dia.title()
if dia=='Lunes':
    print('Buen comienzo de semana')
elif dia=='Viernes':
    print('Termino la semana laboral, disfrutá el finde')
elif dia=='Sabado' or dia=='Domingo':
    print('Disfruta tu día')
elif dia=='Martes' or  dia=='Miercoles' or dia=='Jueves':
    print('Vamos que falta menos para el finde')
else:
    print('Dato inválido')
'''18-	Preguntar al usuario el total de horas trabajadas en el mes y el salario por hora.
La jornada de trabajo máxima es de 48 horas. Calcular, dadas las horas trabajadas, si trabajó horas 
extras y mostrar esta cantidad.
Mostrar su salario total, tomando en cuenta que las horas extras serán pagadas un 10% más que las 
horas laborales comunes.'''
horas_trabajadas = int(input('Ingrese el número de horas trabajadas este mes: '))
salario_hora = float(input('Ingrese su salario por hora trabajada: '))
if horas_trabajadas>48:
    horas_extras = horas_trabajadas - 48
    print(f'Usted trabajó {horas_extras}hs extras')
salario_total = (salario_hora*48)+(salario_hora*0.1 +salario_hora)*horas_extras
print(f'Su salario total del mes es: ${salario_total}')
'''19-	Determinar cuánto se debe pagar por una cantidad de lápices considerando que si 
son 1000 o más, existe un descuento de 7% y teniendo en cuenta que el costo por lápiz es de $60; 
de lo contrario no hay descuento.'''
cantidad = int(input('Ingrese la cantidad de lapices que desea comprar: '))
if cantidad>=1000:
    total = (cantidad * 60)*0.93
    print(f'El monto total de su compra es ${total}')
elif 0<=cantidad<1000:
    total = cantidad * 60
    print(f'El monto total de su compra es ${total}')
else: 
    print('Cantidad incorrecta')
'''20-	Determinar si un alumno aprueba o reprueba un curso, sabiendo que aprobara si su promedio 
de cuatro (4) notas, es mayor o igual a 6; caso contrario saldrá desaprobado.'''
primer_nota, segunda_nota, tercer_nota, cuarta_nota = int(input('Ingrese la primer nota: ')), int(input('Ingrese la segunda nota: ')), int(input('Ingrese la tercer nota: ')), int(input('Ingrese la cuarta nota: '))
promedio = (primer_nota + segunda_nota + tercer_nota + cuarta_nota)/4
if 6<=promedio<=10:
    print(f'Aprobó con un promedio de {promedio}')
elif 0<=promedio<6:
    print(f'Desaprobó con un promedio de {promedio}')
else: 
    print('Ingreso incorrecto de notas')