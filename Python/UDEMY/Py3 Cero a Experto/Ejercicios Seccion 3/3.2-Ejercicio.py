###  2) En la siguiente matriz, el cuarto elemento siempre es la suma de los tres anteriores. Utilizando la indexación corrige las listas que no cumplan esta condición.

"""
matriz= [
    [1,1,1,3],
    [2,2,2,7],
    [3,3,3,9], 
    [4,4,4,13]
];

matriz;

"""

matriz= [
    [1,1,1,3],
    [2,2,2,7],
    [3,3,3,9], 
    [4,4,4,13]
]
"""
matriz[0][3] = matriz[0][0] + matriz[0][1] + matriz[0][2]
matriz[1][3] = matriz[1][0] + matriz[1][1] + matriz[1][2]
matriz[2][3] = matriz[2][0] + matriz[2][1] + matriz[2][2]
matriz[3][3] = matriz[3][0] + matriz[3][1] + matriz[3][2]

print(matriz[0][:])
print(matriz[1][:])
print(matriz[2][:])
print(matriz[3][:])

for m in matriz :
    print(m)
    
"""

# Propuesta
#matriz[1][-1] = sum(matriz[1][:-1])
print(matriz, '\n')

contador_matrix = 0


# Correción a bucle FOR
for m in  matriz :
    matriz[contador_matrix][-1] = sum(matriz[contador_matrix][:-1])
    contador_matrix += 1
    
print(matriz)



