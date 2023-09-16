'''Realizar la carga del precio de un producto y la cantidad a llevar. Mostrar cuanto se debe pagar.'''
precio = float(input('Ingrese el precio del producto: '))
cantidad = int(input('Ingrese la cantidad de unidades que lleva del producto: '))
cantidad_a_pagar = precio * cantidad
print(f'El total de su compra es: ${cantidad_a_pagar}.')
'''Realizar la carga del lado de un cuadrado, mostrar por pantalla el perímetro del mismo.'''
longitud_lado = float(input('Ingrese la longitud de un lado del cuadrado: '))
perimetro = longitud_lado * 4
print(f'El perimetro del cuadrado es: {perimetro}')
'''Realizar un programa que lea cuatro valores numéricos e informar su suma y promedio.'''
primer_valor = float(input('Ingrese el primer valor: '))
segundo_valor = float(input('Ingrese el segundo valor: '))
tercer_valor = float(input('Ingrese el tercer valor: '))
cuarto_valor = float(input('Ingrese el cuarto valor: '))
suma = primer_valor + segundo_valor + tercer_valor + cuarto_valor
promedio = suma / 4
print(f'La suma de los cuatro valores ingresados es: {suma}')
print(f'El promediop de los cuatro valores ingresados es: {promedio}')
'''Calcular el sueldo mensual de un operario conociendo la cantidad de horas trabajadas y el valor por hora.'''
cantidad_horas = float(input('Ingrese el numero de horas trabajadas este mes: '))
valor_hora = float(input('Ingrese el valor por hora trabajada: '))
sueldo_mensual = cantidad_horas * valor_hora
print(f'Su sueldo mensual es: ${sueldo_mensual}')
  