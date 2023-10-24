'''1. El siguiente programa debería imprimir el número 2 si se le ingresan como valores x=5,
y=1 pero en su lugar imprime 5. ¿Qué hay que corregir?'''
'''
#DEFINICIÓN DE FUNCIONES

def most(a,b):
    if (x>y):
        return x
    else:
        return y

def least(a,b):
    if (x<y):
        return x
    else:
        return y
    
#PROGRAMA PRINCIPAL

x = int(input('Ingrese un número: '))
y = int(input('Ingrese otro número: '))
print(most((x-3), least((x+2), (y-5))))
'''
#Habria que corregir las funciones, cambiar x e y por a y b. De la siguiente manera:

#DEFINICIÓN DE FUNCIONES

def most(a,b):
    if (a>b):
        return a
    else:
        return b

def least(a,b):
    if (a<b):
        return a
    else:
        return b
    
#PROGRAMA PRINCIPAL

x = int(input('Ingrese un número: '))
y = int(input('Ingrese otro número: '))
print(most((x-3), least((x+2), (y-5))))