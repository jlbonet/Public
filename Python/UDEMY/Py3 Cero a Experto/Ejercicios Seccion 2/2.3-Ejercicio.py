"""
### 3) Utilizando operadores lógicos determina
# si una cadena de texto introducida por el usuario
# tiene una longitud mayor o igual a 3 y menor o igual a 12 (Basta con mostrar _True o False_ )
"""

texto_usario = input("Introduzca un texto para medir su longitud: ")

resultado = bool(len(texto_usario) >= 3 and len(texto_usario) <= 12)

print(f"¿El texto introducido tienes más de 3 carácteres y menos de 12? {resultado}" )