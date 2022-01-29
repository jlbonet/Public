"""
### 6) Realiza una función separar() que tome una lista de números enteros
# y devuelva dos listas ordenadas: la primera con los números pares
# y la segunda con los números impares:

### Ejemplo: 
+ pares, impares = separar([1,2,4,5,7,8])
+ print(pares) = [2,4,8]
+ print(impares) = [1,5,7]

>  PROTIP: para ordenar una lista utiliza el método sort()
"""

def separar(numeros=None) :
    
    contador = 0
    lista_par =     []
    lista_impar =   []
    
    if numeros is None :
        return print("No ha introducido uno de los parámetros correctamente.")
    
    else :
        
        print(numeros)
        
        for l in numeros :

            if numeros[contador] % 2 == 0 :
                lista_par.append(l)
                contador += 1
            
            elif not numeros[contador] % 2 == 0 :
                lista_impar.append(l)
                contador += 1
                
        return print(f"Esta es la lista PAR {lista_par}") , print(f"Esta es la lista impar {lista_impar}")
    
separar(list(range(1,101,1)))