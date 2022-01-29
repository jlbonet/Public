"""
### 2) Dada una lista de *strings* (cadenas de caracteres), haga un programa que devuelva:
+ El número de strings que tienen una longitud de 2 o más caracteres, y cuyo primer y último caracter son iguales.
+ Una lista nueva con solo estos strings.
lista = ['avila', 'cafe', 'este', 'narracion', 'buda', 'extra', 'salida']
"""

lista = ['avila', 'cafe', 'este', 'narracion', 'buda', 'extra', 'salida', 'conejo', 'ruido', 'televisor', 'ana', 'local']

lista_nueva = []

for l in lista :
    if ((l[:][0]) == (l[:][-1])) and (len(l) >= 2 ) :
        lista_nueva.append(l)

print(f"La lista de parámentros pasados al programa es {lista} \n")
print(f"El número de elementos que cumplen con los parámetros es: {len(lista_nueva)} \n")
print(f"Los elementos agregados a la nueva lista son: {lista_nueva}")         
        
        
#and (l.startswith([1]) == l.endswith([-1])) :