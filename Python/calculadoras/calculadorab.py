"""
Programa para la creación de una calculadora básica mediante el uso el uso de clases.

Operaciones:
Sumar
Restar
Multiplicar
Dividir

"""
import re

# Definimos una clase básica para las operaciones a realizar.
class Calculadora :
    
    def __init__(self) :
        pass
        
    def sumar(self, sum1, sum2) :
        
        self.sum1 = sum1
        self.sum2 = sum2
        
        suma = sum1 + sum2
        
        return suma
    
    def restar(self, rum1, rum2) :
        
        self.rum1 = rum1
        self.rum2 = rum2
        
        resta = rum1 - rum2
        
        return resta
    
    def multiplicar(self, mum1, mum2) :
        
        self.mum1 = mum1
        self.mum2 = mum2
        
        multiplica = mum1 * mum2
        
        return multiplica
    
    def dividir(self, dum1, dum2) :
        
        self.dum1 = dum1
        self.dum2 = dum2
        
        divide = dum1 / dum2
        
        return divide
        
# Menú selección para el usuario.
contador = 0
while contador < 1 :

    print('Bienvenido al programa "Calculadora básica". \n')
    
    contador_menu = 0
    
    while contador_menu < 1 :
    
        
        print('Se pueden realizar las siguientes operaciones: ')
        print("""
        1.- Sumar.
        2.- Restar.
        3.- Multiplicar.
        4.- Dividir.

        5.- Salir.
        """)
        
        seleccion = input("Introduce la opción que deseas: ")
        
        if not re.match('(1|2|3|4|5)' , seleccion) :
            print("\nNo has seleccionado una opción válida. Por favor, vuelve a elegir: \n")
            
        elif seleccion == '5' :
            
            print("Has elegidor salir. Hasta luego!")
            contador_menu   += 1
            contador        += 1 
        
        elif seleccion == '1' :
            contador_suma = 0
            while contador_suma < 1 :
                num1 = input("Introduce el primer número: ")
                num2 = input("Introduce el segundo número: ")

                if not re.match('^([0-9]|[0-9]+.[0-9]+)$', num1) or not re.match('^([0-9]|[0-9]+.[0-9]+)$', num2) :
                    print("No has introducido uno de los números correctamente, por favor, vuelve a introducirlos.\n")
                else :
                    num1, num2 = float(num1), float(num2)
                    num_suma = Calculadora()
                    print( f"\nEl resultado de la suma es {num_suma.sumar(num1, num2)}" , "\n")
                    contador_suma += 1
                    
        elif seleccion == '2' :
            contador_resta = 0
            while contador_resta < 1 :
                num1 = input("Introduce el primer número: ")
                num2 = input("Introduce el segundo número: ")

                if not re.match('^([0-9]|[0-9]+.[0-9]+)$', num1) or not re.match('^([0-9]|[0-9]+.[0-9]+)$', num2) :
                    print("No has introducido uno de los números correctamente, por favor, vuelve a introducirlos.\n")
                    
                else :
                    num1, num2 = float(num1), float(num2)
                    num_resta = Calculadora()
                    print( f"\nEl resultado de la resta es {num_resta.restar(num1, num2)}" , "\n")
                    contador_resta += 1
                    
        elif seleccion == '3' :
            contador_multi = 0
            while contador_multi < 1 :
                num1 = input("Introduce el primer número: ")
                num2 = input("Introduce el segundo número: ")

                if not re.match('^([0-9]|[0-9]+.[0-9]+)$', num1) or not re.match('^([0-9]|[0-9]+.[0-9]+)$', num2) :
                    print("No has introducido uno de los números correctamente, por favor, vuelve a introducirlos.\n")
                    
                else :
                    num1, num2 = float(num1), float(num2)
                    num_multi = Calculadora()
                    print( f"\nEl resultado de la multiplicación es {num_multi.multiplicar(num1, num2)}" , "\n")
                    contador_multi += 1
                    
        elif seleccion == '4' :
            contador_div = 0
            while contador_div < 1 :
                num1 = input("Introduce el primer número: ")
                num2 = input("Introduce el segundo número: ")

                if not re.match('^([0-9]|[0-9]+.[0-9]+)$', num1) or not re.match('^([0-9]|[0-9]+.[0-9]+)$', num2) :
                    print("No has introducido uno de los números correctamente, por favor, vuelve a introducirlos.\n")
                    
                else :
                    num1, num2 = float(num1), float(num2)
                    num_div = Calculadora()
                    print( f"\nEl resultado de la división es {num_div.dividir(num1, num2)}" , "\n")
                    contador_div += 1
