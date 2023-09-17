'''Un instituto de inglés necesita un programa que le permita, cada día, procesar
observaciones sobre las clases de ese día. El instituto dicta clases a estudiantes de
distintos niveles y cada nivel tiene clases en un día de la semana diferente: los lunes se
dicta nivel inicial, los martes el nivel intermedio, los miércoles el nivel avanzado, los
jueves son para práctica hablada y los viernes se dicta inglés para viajeros.
Se debe comenzar por solicitar al usuario que ingrese la fecha actual en formato “día,
DD/MM”, donde [día] es un día de la semana, DD es el número de día y MM es el
número de mes. Si el usuario ingresa un día de la semana inexistente o una fecha cuyo
día supere el número 31 o el mes supere el número 12, finalizar el programa indicando
que se produjo un error. Debe permitirse que ingrese el día de la semana en
minúsculas o mayúsculas indistintamente. Como precondición se tiene que lo
ingresado por el usuario tendrá la forma <[alfanumérico], [numérico]/[numérico]>.
Una vez indicada la fecha el usuario necesita poder indicar si ese día se tomaron los
exámenes, pero eso solo si se trata de los niveles inicial, intermedio o avanzado, ya
que las prácticas habladas y el inglés para viajeros no tienen exámenes. Si hubo
exámenes, el usuario ingresará cuántos alumnos aprobaron y cuantos no, y el
programa le mostrará el porcentaje de aprobados.
Si el día fue el correspondiente a práctica hablada, el usuario deberá ingresar el
porcentaje de asistencia a clase y el programa le indicará 'asistió la mayoría' en caso de
que la asistencia sea mayor al 50% o 'no asistió la mayoría' si no es así.
Si se trata del inglés para viajeros y la fecha actual corresponde al día 1 del mes 1 o del
mes 7, se deberá imprimir 'Comienzo de nuevo ciclo' y solicitar al usuario que ingrese
la cantidad de alumnos del nuevo ciclo y el arancel en $ por cada alumno, para luego
imprimir el ingreso total en $.'''
#Lunes-Nivel Inicial
#Martes-Nivel Intermedio
#Miercoles-Nivel Avanzado
#Jueves-Practica Hablada
#Viernes-Ingles para Viajeros
dia_actual, dia_numero, mes_numero = input('Ingrese día de la semana: '),int(input('Ingrese el número de día: ')),int(input('Ingrese el número de mes: '))
dia_actual = dia_actual.title()
if dia_actual!='Lunes' and dia_actual!='Martes' and dia_actual!='Miercoles' and dia_actual!='Jueves' and dia_actual!='Viernes':
    print('Se produjo un error')
elif dia_numero<1 or dia_numero>31:
    print('Se produjo un error')
elif mes_numero<1 or mes_numero>12:
    print('Se produjo un error')
if dia_actual=='Lunes' or dia_actual=='Martes' or dia_actual=='Miercoles':
    examen_si_o_no = input('Se tomó examen? ')
    examen_si_o_no = examen_si_o_no.title()
    if examen_si_o_no=='Si':
        alumnos_aprobados = int(input('Ingrese cuantos alumnos aprobaron: '))
        alumnos_desaprobados = int(input('Ingrese cuantos alumnos desaprobaron: '))
        porcentaje_aprobados = (alumnos_aprobados*100)/(alumnos_aprobados+alumnos_desaprobados)
        print(f'El porcentaje de alumnos aprobados es: {porcentaje_aprobados}%')
if dia_actual=='Jueves':
    porcentaje_asistencia = int(input('Ingrese el porcentaje de asistencia: '))
    if porcentaje_asistencia>50:
        print('Asistió la mayoria')
    else:
        print('No asistió la mayoria')
if dia_actual=='Viernes':
    if (dia_numero==1 and mes_numero==1) or (dia_numero==1 and mes_numero==7):
        print('Comienzo de nuevo ciclo')
        alumnos_nuevo_ciclo = int(input('Ingrese la cantidad de alumnos del nuevo ciclo: '))
        alumnos_nuevo_ciclo = float(alumnos_nuevo_ciclo)
        arancel = float(input('Ingrese el arancel en $ por cada alumno: '))
        ingreso_total = alumnos_nuevo_ciclo*arancel
        print(f'El ingreso total es ${ingreso_total}')
