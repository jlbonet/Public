"""
### 2) Al realizar una consulta en un registro hemos recibido unos valores corruptos.
# Al parecer entrega el nombre y apellido del alumno al revés. ¿Qué puede hacer para obtener el siguiente mensaje por pantalla
> _NOMBRE APELLIDO ha sacado un NOTA_
"""
cadena_normal = 'José Luis Dominguez, 10'
cadena_alreves = cadena_normal[::-1]

print(cadena_alreves)

print(cadena_normal[4::], cadena_normal[:2])