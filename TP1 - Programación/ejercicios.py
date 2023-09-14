'''1.Indica si los siguientes identificadores son válidos en Python. 
En el caso de que el identificador no sea válido, explica el motivo.'''

'''
a) alumno1 #Es válido en Python
b) 1alumno #No es válido en Python ya que comienza con un número
c) primerNombre #Es válido en Python pero se recomienda utilizar snake_case
d) /apellido #No es válido en Python ya que comienza con un simbolo 
e) tamaño_máximo #Es válido en Python pero no es recomendable utilizarlo
f) for #No es válido en Python ya que se trata de una palabra reservada del lenguaje
g) _$nombre #No es válido en Python ya que contiene un simbolo
h) global #No es válido en Python ya que se trata de una palabra reservada del lenguaje
i) primer_nombre #Es válido en Python
j) num_mayor #Es válido en Python
k) menor-num #No es válido en Python ya que utiliza un simbolo
l) dni@alumno #No es válido en Python ya que utiliza un simbolo
m) 5var #No es válido en Python ya que comienza con un número
n) with #No es válido en Python ya que se trata de una palabra reservada del lenguaje
o) Auto-seleccionado #No es válido en Python ya que utiliza un simbolo
p) %aumento #No es válido en Python ya que utiliza un simbolo
q) _123 #Es válido en Python 
r) ValorTotal #Es válido en Python pero no es recomendable 
s) DESCUENTO #Es válido en Python pero no es recomendable
t) año #Es válido en Python pero no es recomendable
u) mes_actual #Es válido en Python
v) apellido&nombre #No es válido en Python ya que utiliza un simbolo
w) 89GW5 #No es válido en Python ya que comienza con un número
x) valido? #No es válido en Python ya que contiene un simbolo
'''

'''2.Indica qué dato se guarda en la variable x en cada caso, 
suponiendo una ejecución secuencial del programa.'''

'''a.   x=46 
        x=15
        x=30''' #El dato que se guarda es: x=30
'''b.   x=46 
        x=15
        x=30''' #El dato que se guarda es: x=30
'''c.   x=25 
        x+10''' #El dato que se guarda es: x=25
'''d.   x=10-2 
        10+2''' #El dato que se guarda es: x=8
'''e.   y=3*(4+2)
        x=y+2 
        z=5
        x=y-z''' #El dato que se guarda es: x=13
'''f.   x=3 
        y=x+6
        x=y-1''' #El dato que se guarda es: x=8

'''3.Indica qué tipo de dato se guarda en cada variable.'''

'''     a) var1 = 100/5 #Se guardará un dato tipo 'float'
        b) var2 = 7/2   #Se guardará un dato tipo 'float'
        c) var3 = 7//2  #Se guardará un dato tipo 'integers'
        d) var4 = 7%2   #Se guardará un dato tipo 'integers'
        e) var5 = 'a'   #Se guardará un dato tipo 'string'
        f) var6 = 'casa'+'s' #Se guardará un dato tipo 'string'
        g) var7 = 'automovil'[1 + 1] #Se guardará un dato tipo 'string'
        h) var8 = len('carpeta') #Se guardará un dato tipo 'integers'
        i) var9 = int('748') #Se guardará un dato tipo 'integers'
        j) var10 = float('832') #Se guardará un dato tipo 'float'
        k) var11 = float(321) #Se guardará un dato tipo 'float'
        l) var12 = str(65) #Se guardará un dato tipo 'string'
        m) var13 = 1 + 5 != 3 #Se guardará un dato tipo 'boolean'
        n) var14 = 177 % 2 == 0 #Se guardará un dato tipo 'boolean'
        o) var15 = len ('ola') <= 12 #Se guardará un dato tipo 'boolean'
'''

'''4.Indica cuáles de las siguientes operaciones no son válidas.'''

'''     a) 11 - (4%2 + 10) #Esta operación es válida
        b) '30' + '2' #Esta operación es válida
        c) '30' + 2 #Esta operación no es válida, ya que se trata de un intento de concatenación de un str y un int
        d) 'hola'[len('hola')] #Esta operación no es válida, ya que 'len('hola')' supera el rango de 'hola'
        e) len (456) #Esta operación no es válida, ya que 'len' es válido para variables de tipo string
        f) 'hola'[len('fin')] #Esta operación es válida
        g) int('4') #Esta operación es válida
        h) int(4) #Esta operación es válida pero innecesaria ya que devuelve el mismo tipo de variable 
        i) int('z') #Esta operación no es válida, ya que no es posible convertir a integers este tipo de dato
        j) int('4.') #Esta operación no es válida, ya que contiene un '.' y este no se puede convertir a integers
        k) 4 < 'f' #Esta operación no es válida, ya que no es posible aplicar una operación relacional o de comparación entre datos de distinto tipo 
        l) 'palabra'='rama' #Esta operación no es válida
'''

'''5.Declara una variable de cada tipo de dato y asígnale un valor.'''

'''     a) var_int = 456
        b) var_float = 1.5
        c) var_complex = 4j
        d) var_string = 'hola' 
        e) var_bool = True
        f) var_list = [7,True,1.5,'hola mundo']
        g) var_tuple = (7,None,True,'chau',6.5)
        h) var_dict = {1:True,2:False,3:6.5,4:4j}
        i) var_null = None
'''

'''6.Teniendo la variable de tipo string: 
frase = “Caminante, no hay camino, se hace camino al andar.”, indica qué obtendríamos si aplicáramos:'''

'''     a) frase[5] #Obtendriamos 'a'
        b) frase[-1] #Obtendriamos 'r'
        c) frase[0:8] #Obtendriamos 'Caminant' 
        d) frase[::3] #Obtendriamos 'Cin,oaci,ea molnr' #En este caso nos imprime de 3 en 3
'''

'''7.Usando la variable del ejercicio anterior:'''

'''     a) ¿Cómo obtenemos la cadena al revés? '.radna la onimac ecah es ,onimac yah on ,etnanimaC' 
                La obtenemos de la siguiente manera: print(frase[::-1])
        
        b) ¿Cómo obtenemos la subcadena 'hace'? 
                La obtenemos de la siguiente manera: print(frase[29:34]) 
'''

'''8.Métodos upper(), lower() y title().'''

'''     a) Pon en mayúsculas la primera letra de cada palabra del siguiente nombre: 'lucas mauricio barros'.
                frase = 'lucas mauricio barros'
                print (frase.title())
        b) Deja esta frase totalmente en letras minúsculas: 'El qUe No arRiesGa, nO gANa.'
                frase = 'El qUe No arRiesGa, nO gANa'
                print (frase.lower())
        c) Deja esta frase totalmente en letras mayúsculas: 'El qUe No arRiesGa, nO gANa.'
                frase = 'El qUe No arRiesGa, nO gANa'
                print (frase.upper())
'''

'''9.Convierte en expresiones algorítmicas las siguientes expresiones algebraicas.
Coloca paréntesis solamente donde sean necesarios.'''

'''     a)      resultado = b/2 - 4*a*c
        b)      resultado = 3*x*y - 5*x + 12*x - 17
        c)      resultado = (b + d)/(c + 4)
        d)      resultado = (x*y)/y + 2
        e)      resultado = (1/y) + (3*x)/z + 1
        f)      resultado = 1/(y + 3) + x/y + 1
        g)      resultado = a**2 + b**2
        h)      resultado = (a + b)**2
        i)      resultado = b*(1/3) + 34
        j)      resultado = (x/y)*(z + w)*math.pi
        k)      resultado = (x + y)/[u + (w/b)]
'''
'''10. Convierte en expresiones algebraicas las siguientes expresiones algorítmicas.
Coloca paréntesis solamente donde sean necesarios.'''
  
'''     a)      x = [-b + (b² - 4 x a x c)½]/(2 x a)
        b)      (x² + y²)/z²
        c)      4 x (x²) - 2 x (x) + 7
        d)      (b²)½ - 4 x a x c
        e)      (a - b)² + (c - d)³
        f)      (x + y)/y - (3x)/5  
        g)      (a² + b²)^(1/3)
        h)      [3 x (x²)]/{[3 x (x)³]/(4 x y + 6)}½ 
'''
'''11. Dada la siguiente expresión aritmética:
Deterinar que resultado obtendremos'''

'''     a) resultado = 10.625'''
'''12. Escribe las expresiones algoritmicas equivalentes a los siguientes enunciados'''

'''     a)      resultado = 5 + 3 
        b)      promedio = (4 + 7 + 9) / 3
        c)      área = 8 * 5
        d)      numero = int(input('Ingrese un número par: '))
                if numero % 2 == 0 
                 print (f'El número ingresado: {numero} ES PAR)
                else: 
                 print (f'El número ingresado: {numero} NO ES PAR)
        e)      resultado = 2 * 16
        f)      resultado = 6 * (8 - 3)
        g)      resultado = (2 * 6) - (4 + 3)
        h)      numeroN = int(input('Ingrese un número: ))
                if numeroN % 3 == 0 and numeroN % 2 == 0:
                        print(f'El número ingresado es múltiplo de los números 3 y 2')
                else:
                        print(f'El número ingresado no es múltiplo de los números 3 y 2')
        i)      precio = int(input('Ingrese el precio: '))
                if precio <= 15 and precio < 90:
                        print(f'El precio es menor o igual que 15 y menor que 90')
                else: 
                        print(f'El precio no cumple con los parámetros')
        j)      variableN = int(input('Ingrese un número entero: '))
                variableN = variableN + 12
                print(f'El resultado es: {variableN}')
        k)      variableN = int(input('Ingrese un número entero: '))
                variableN = variableN - 5
                print(f'El resultado es: {variableN}')
        l)      variableN = int(input('Ingrese un número entero: '))
                variableN = variableN * 3
                print(f'El resultado es: {variableN}')
        m)      variableN = int(input('Ingrese un número entero: '))
                variableN = variableN / 2
                print(f'El resultado es: {variableN}')'''

'''13. ¿Qué resultado (True/False) dan las siguientes operaciones?'''
'''     a) resultado = False
        b) resultado = True
        c) x = False
        d) resultado = False
        e) resultado = False
        f) resultado = False
        g) resultado = True
        h) resultado = True
        i) resultado = True
'''
'''14.  a) 6
        b) 3
        c) 25
        d) 1
'''
'''15.  a) 'amarillo', print(colores[3])
        b) posición 0, posición 7
        c) numeros = ['tres', 'dos', 'cinco', 'cuatro', uno']
        d) verde
        e) numeros = (10, 1, 5, 11) 
           operacion = (numeros[0] + numeros[0] + numeros[2])
           print(operacion)
        f) 4
        g) diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
         print(diccionario['c']) 
'''
'''16. nombre = str(input('Ingrese su nombre por favor: '))
       print(f'Bienvenido {nombre} a la Universidad Tecnologica Nacional')
        a) primer_numero = float(input('Ingrese el primer número: '))
           segundo_numero = float(input('Ingrese el segundo número: '))
           suma = primer_numero + segundo_numero
           print(f'El resultado es {suma})   
        b) edad = int(input('Ingrese su edad: '))
           años_faltantes = 100 - edad
           print(f'Para que usted llegue a la edad de 100 años le faltan {años_faltantes} años')
'''
'''17. a) numero = int(input('Ingrese un número entero: '))
          if numero % 2 == 0:
                print('El número ingresado es par')
          else: 
                print('El número ingresado no es par')
        b) numero = float(input('Ingrese un número: '))
           if numero < 0:
                print(f'El valor absoluto del número ingresado es: {int(numero*(-1))}')
           else:
                print(f'El valor absoluto del número ingresado es: {int(numero)}')
        c) primer_numero = float(input('Ingrese el primer número: '))
           segundo_numero = float(input('Ingrese el segundo numero: '))
           mayor_numero = 0
           if mayor_numero < primer_numero:
                mayor_numero = primer_numero
           if mayor_numero < segundo_numero:
                mayor_numero = segundo_numero
           print(f'El mayor número es: {mayor_numero}')     
'''


