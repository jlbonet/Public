"""
Programa para la creación de una calculadora básica mediante el uso el uso de clases.

Operaciones:
Sumar
Restar
Multiplicar
Dividir

"""
# Importamos a re para utilizar el método match para poder realizar comprobaciones con "regex"
import re

# Definimos una clase básica para las operaciones a realizar.
class Calculadora :
    
    # Varibles de clase, son accesibles desde cualquier método dentro de la clase.
    # Se accede a ellas mediante SELF.
    # Se pueden elimiar pues han sido declaradas dentro del método __init__
    num1 = 0
    num2 = 0
    
    # Constructor, su objetivo es asignar valores de inicio a las variables de clase.
    # Aquellas que están declaradas fueras de cualquier método.
    # En el constructor se inicializa el objeto
    # Las varibles a y b son "locales" y por tanto solo existen denttro de __init__
    # Para poder acceder a las varibles locales, las asignames a las variables de clase mediante SELF.
    def __init__(self, a, b) :
        self.num1 = a
        self.num2 = b

    # Definimos la función para realizar la suma, recogiendo los parámetros introducidos al crear el objeto                
    def sumar(self) :
        resultado = self.num1 + self.num2
        return resultado
    
    # Definimos la función para realizar la suma, recogiendo los parámetros introducidos al crear el objeto
    def restar(self) :
        resultado = self.num1 - self.num2
        return resultado
        
    # Definimos la función para realizar la suma, recogiendo los parámetros introducidos al crear el objeto
    def multiplicar(self) :
        resultado = self.num1 * self.num2
        return resultado
    
    # Definimos la función para realizar la suma, recogiendo los parámetros introducidos al crear el objeto
    def dividir(self) :
        resultado = self.num1 / self.num2
        return resultado

# Menú selección para el usuario.
# Agregamos un contador y abrimos el primer bucle para 
# dejar el programa activo hasta seleccionar salir
contador = 0
while contador < 1 :
    print('Bienvenido al programa "Calculadora básica 2". \n')
    contador_menu = 0
    
    # Bucle para selección de menú e impedir argumentos incorrectos
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
                    num_suma = Calculadora(num1, num2)
                    print( f"\nEl resultado de la suma es {num_suma.sumar()}" , "\n")
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
                    num_resta = Calculadora(num1, num2)
                    print( f"\nEl resultado de la resta es {num_resta.restar()}" , "\n")
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
                    num_multi = Calculadora(num1, num2)
                    print( f"\nEl resultado de la multiplicación es {num_multi.multiplicar()}" , "\n")
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
                    num_div = Calculadora(num1, num2)
                    print( f"\nEl resultado de la división es {num_div.dividir()}" , "\n")
                    contador_div += 1