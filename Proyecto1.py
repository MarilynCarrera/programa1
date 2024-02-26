#Programa1_Matriz Bidimensional

#Matriz_bidimensional_de_3x3
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

#Valor_específico_en_la_matriz
def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return True, (i, j)
    return False, None

#Valor_a_buscar_en_la_matriz
valor_buscado = 5

#Búsqueda_en_la_matriz
encontrado, posicion = buscar_valor(matrix, valor_buscado)

#Mostrar_el_resultado_de_la_búsqueda
if encontrado:
    print(f"El valor {valor_buscado} se encontró en la posición {posicion} de la matriz.")
else:
    print(f"El valor {valor_buscado} no se encontró en la matriz.")
