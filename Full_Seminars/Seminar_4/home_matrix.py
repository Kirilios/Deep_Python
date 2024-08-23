'''
Напишите функцию для транспонирования матрицы transposed_matrix,
принимает в аргументы matrix, и возвращает транспонированную матрицу.
Пример использования На входе:
matrix = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
transposed_matrix = transpose(matrix)
На выходе:
[[1, 4, 7], [2, 5, 8], [3, 6, 9]]
'''

matrix = [[1, 2],
[4, 5]]

def transpose(matrix):
    new_matrix = []
    for i in range(len(matrix[0])):
        new_row = []
        for row in matrix:
            new_row.append(row[i])
        new_matrix.append(new_row)
    return new_matrix

#transposed_matrix = transpose(matrix)
print(transpose(matrix))