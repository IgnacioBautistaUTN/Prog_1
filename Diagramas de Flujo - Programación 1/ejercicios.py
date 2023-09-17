'''Realizar la carga del lado de un cuadrado, mostrar por pantalla el perímetro del mismo.'''
lado = int(input('Ingrese la longitud del lado de un cuadrado(cm): '))
perimetro = lado * 4
print(f'El perimetro del cuadrado es {perimetro}cm.')
'''Realizar un programa que lea cuatro valores numéricos e informar su suma y promedio.'''
primer_valor = float(input('Ingrese el primer número: '))
segundo_valor = float(input('Ingrese el segundo número: '))
tercer_valor = float(input('Ingrese el tercer número: '))
cuarto_valor = float(input('Ingrese el cuarto número: '))
suma = primer_valor + segundo_valor + tercer_valor + cuarto_valor
promedio = suma / 4
print(f'La suma de los valores ingresados es: {suma} y el promedio de dichos valores: {promedio}')
'''Calcular el sueldo mensual de un operario conociendo la cantidad de horas trabajadas 
y el valor por hora.'''
horas_trabajadas = float(input('Ingrese la cantidad de horas trabajadas este mes: '))
valor_hora = float(input('Ingrese el valor por hora trabajada: '))
sueldo_mensual = horas_trabajadas * valor_hora
print(f'Su sueldo mensual es: ${sueldo_mensual}')