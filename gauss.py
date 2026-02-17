def gaussian_elimination(mat):
    n = len(mat)
    # Прямой ход с пивотированием (обнуление всех элементов строки или столбца, кроме одного)
    for i in range(n):
        # Находим строку с максимальным элементом в i-м столбце
        max_row = i
        for k in range(i + 1, n):
            if abs(mat[k][i]) > abs(mat[max_row][i]):
                max_row = k
        # Меняем строки
        mat[i], mat[max_row] = mat[max_row], mat[i]
        # Проверяем, нет ли деления на ноль
        if abs(mat[i][i]) < 1e-10:
            return None  # Система не имеет единственного решения
        # Делаем ведущий элемент равным 1
        pivot = mat[i][i]
        for j in range(i, n + 1):
            mat[i][j] /= pivot
        # Обнуляем элементы ниже ведущего
        for k in range(n):
            if k != i:
                factor = mat[k][i]
                for j in range(i, n + 1):
                    mat[k][j] -= factor * mat[i][j]
    
    # Извлекаем решение
    x = [mat[i][n] for i in range(n)]
    return x

# Пример использования
matrix = [
    [2, 3, 6],
    [1, -1, 0.5]
]
result = gaussian_elimination(matrix)
print("Решение:", result)  

# Вывод: [1.5, 1.0]