"""
Programa para la creación de una calculadora de fracciones mediante el uso de clases.

Operaciones:
Sumar
Restar
Multiplicar
Dividir

"""
import re

class Fracciones :
    
    def __init__(self, n1, d1, n2, d2) :
        
        self.n1 = n1
        self.d1 = d1
        self.n2 = n2
        self.d2 = d2
        
    def sumar(self) :
        if self.d1 == self.d2 :
            numerador = (self.n1 + self.n2)
            denominador = ((self.d1 + self.d2)/2)
            resultado = print((numerador) , "/", (denominador))
        elif not self.d1  == self.d2 :
            numerador = ((self.n1 * self.d2) + (self.n2 * self.d1))
            denominador = ((self.d1 * self.d2))
            resultado = print("\nEl resultado de la suma es: ", (numerador) , "/" , (denominador) , "\n")
            
        return resultado
    
    def restar(self) :
        if self.d1 == self.d2 :
            numerador = (self.n1 - self.n2)
            denominador = ((self.d1 + self.d2)/2)
            resultado = print((numerador) , "/", (denominador))
        elif not self.d1  == self.d2 :
            numerador = ((self.n1 * self.d2) - (self.n2 * self.d1))
            denominador = ((self.d1 * self.d2))
            resultado = print("\nEl resultado de la resta es: ", (numerador) , "/" , (denominador) , "\n")
        
        return resultado
    
    def multiplicar(self) :
        numerador = (self.n1 * self.n2)
        denominador = (self.d1 * self.d2)
        resultado = print("\nEl resultado de la multiplicación es: ", (numerador) , "/" , (denominador) , "\n")
        
        return resultado
    
    def dividir(self) :
        self.fn2 = self.d2
        self.fd2 = self.n2
        
        numerador = (self.n1 * self.fn2)
        denominador = (self.d1 * self.fd2)
        resultado = print("\nEl resultado de la divisón es: ", (numerador) , "/" , (denominador) , "\n")
        
        return resultado

contador = 0
while contador < 1 :
    print('Bienvenido a "Calculadora de fracciones básica". \n')
    contador_menu = 0
    
    while contador_menu < 1 :
        print('Se pueden realizar las siguientes operaciones con fracciones: ')
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
                num1 = input("introduce la primera fracción del modo x/y: ")
                num2 = input("introduce la segunda fracción del modo x/y: ")

                if not re.match('^([0-9]+\.[0-9]+\/[0-9]+\.[0-9]+|[0-9]+[0-9]+\/[0-9]+[0-9]+|[0-9]\/[0-9])$', num1) or not re.match('^([0-9]+\.[0-9]+\/[0-9]+\.[0-9]+|[0-9]+[0-9]+\/[0-9]+[0-9]+|[0-9]\/[0-9])$', num2) :
                    print("No has introducido una de los fracciones correctamente, por favor, vuelve a introducirlas.\n")
                else :
                    l1 = num1.replace("/", " ").split()
                    l2 = num2.replace("/", " ").split()
                    n1 = float(l1[0])
                    d1 = float(l1[1])
                    n2 = float(l2[0])
                    d2 = float(l2[1])
                    num_suma = Fracciones(n1, d1, n2, d2)
                    num_suma.sumar()
                    contador_suma += 1
                    
        elif seleccion == '2' :
            contador_resta = 0
            while contador_resta < 1 :
                num1 = input("introduce la primera fracción del modo x/y: ")
                num2 = input("introduce la segunda fracción del modo x/y: ")

                if not re.match('^([0-9]+\.[0-9]+\/[0-9]+\.[0-9]+|[0-9]+[0-9]+\/[0-9]+[0-9]+|[0-9]\/[0-9])$', num1) or not re.match('^([0-9]+\.[0-9]+\/[0-9]+\.[0-9]+|[0-9]+[0-9]+\/[0-9]+[0-9]+|[0-9]\/[0-9])$', num2) :
                    print("No has introducido una de los fracciones correctamente, por favor, vuelve a introducirlas.\n")
                else :
                    l1 = num1.replace("/", " ").split()
                    l2 = num2.replace("/", " ").split()
                    n1 = float(l1[0])
                    d1 = float(l1[1])
                    n2 = float(l2[0])
                    d2 = float(l2[1])
                    num_resta = Fracciones(n1, d1, n2, d2)
                    num_resta.restar()
                    contador_resta += 1
                    
        elif seleccion == '3' :
            contador_multi = 0
            while contador_multi < 1 :
                num1 = input("introduce la primera fracción del modo x/y: ")
                num2 = input("introduce la segunda fracción del modo x/y: ")

                if not re.match('^([0-9]+\.[0-9]+\/[0-9]+\.[0-9]+|[0-9]+[0-9]+\/[0-9]+[0-9]+|[0-9]\/[0-9])$', num1) or not re.match('^([0-9]+\.[0-9]+\/[0-9]+\.[0-9]+|[0-9]+[0-9]+\/[0-9]+[0-9]+|[0-9]\/[0-9])$', num2) :
                    print("No has introducido una de los fracciones correctamente, por favor, vuelve a introducirlas.\n")
                else :
                    l1 = num1.replace("/", " ").split()
                    l2 = num2.replace("/", " ").split()
                    n1 = float(l1[0])
                    d1 = float(l1[1])
                    n2 = float(l2[0])
                    d2 = float(l2[1])
                    multi = Fracciones(n1, d1, n2, d2)
                    num_resta.multiplicar()
                    contador_multi += 1
                    
        elif seleccion == '4' :
            contador_div = 0
            while contador_div < 1 :
                num1 = input("introduce la primera fracción del modo x/y: ")
                num2 = input("introduce la segunda fracción del modo x/y: ")

                if not re.match('^([0-9]+\.[0-9]+\/[0-9]+\.[0-9]+|[0-9]+[0-9]+\/[0-9]+[0-9]+|[0-9]\/[0-9])$', num1) or not re.match('^([0-9]+\.[0-9]+\/[0-9]+\.[0-9]+|[0-9]+[0-9]+\/[0-9]+[0-9]+|[0-9]\/[0-9])$', num2) :
                    print("No has introducido una de los fracciones correctamente, por favor, vuelve a introducirlas.\n")
                else :
                    l1 = num1.replace("/", " ").split()
                    l2 = num2.replace("/", " ").split()
                    n1 = float(l1[0])
                    d1 = float(l1[1])
                    n2 = float(l2[0])
                    d2 = float(l2[1])
                    multi = Fracciones(n1, d1, n2, d2)
                    num_resta.dividir()
                    contador_div += 1
                    
        