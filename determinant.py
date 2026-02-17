def get_minor(matrix, row, col):
    """
    Получает минор матрицы - матрицу без указанной строки и столбца
    """
    return [
        [matrix[i][j] for j in range(len(matrix)) if j != col]
        for i in range(len(matrix)) if i != row
    ]

def determinant_recursive(matrix):
    """
    Вычисляет определитель матрицы рекурсивным методом (разложение по строке)
    """
    n = len(matrix)
    
    # Проверка на квадратность матрицы
    if any(len(row) != n for row in matrix):
        raise ValueError("Матрица должна быть квадратной")
    
    # Базовый случай: матрица 1×1
    if n == 1:
        return matrix[0][0]
    
    # Базовый случай: матрица 2×2
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    det = 0
    
    # Разложение по первой строке
    for col in range(n):
        # Получаем минор
        minor = get_minor(matrix, 0, col)
        
        # Вычисляем определитель минора рекурсивно
        # (-1)^col - знак алгебраического дополнения
        det += ((-1) ** col) * matrix[0][col] * determinant_recursive(minor)
    
    return det


def determinant_gauss(matrix):
    """
    Вычисляет определитель методом Гаусса (приведение к треугольному виду)
    Более эффективен для больших матриц
    """
    n = len(matrix)
    
    # Создаем копию матрицы, чтобы не изменять оригинал
    mat = [row[:] for row in matrix]
    
    # Проверка на квадратность
    if any(len(row) != n for row in mat):
        raise ValueError("Матрица должна быть квадратной")
    
    det = 1
    
    for i in range(n):
        # Поиск ведущего элемента (для численной стабильности)
        max_row = i
        for k in range(i + 1, n):
            if abs(mat[k][i]) > abs(mat[max_row][i]):
                max_row = k
        
        # Если максимальный элемент 0, определитель = 0
        if abs(mat[max_row][i]) < 1e-10:
            return 0
        
        # Обмен строк (меняет знак определителя)
        if max_row != i:
            mat[i], mat[max_row] = mat[max_row], mat[i]
            det *= -1
        
        # Умножаем определитель на диагональный элемент
        det *= mat[i][i]
        
        # Обнуляем элементы ниже диагонали
        for k in range(i + 1, n):
            factor = mat[k][i] / mat[i][i]
            for j in range(i, n):
                mat[k][j] -= factor * mat[i][j]
    
    return det



# --- Пример использования ---
print("=" * 50)
print("МЕТОД 1: Рекурсивный расчет определителя")
print("=" * 50)

# Матрица 2×2
matrix_2x2 = [
    [4, 3],
    [2, 1]
]
det_2x2 = determinant_recursive(matrix_2x2)
print(f"\nМатрица 2×2: {matrix_2x2}")
print(f"Определитель = {det_2x2}")
print(f"Проверка: 4*1 - 3*2 = {4*1 - 3*2}")

# Матрица 3×3
matrix_3x3 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
det_3x3 = determinant_recursive(matrix_3x3)
print(f"\nМатрица 3×3: {matrix_3x3}")
print(f"Определитель = {det_3x3}")
print("(Эта матрица вырожденная, определитель = 0)")

# Матрица 3×3 с ненулевым определителем
matrix_3x3_nonzero = [
    [6, 1, 1],
    [4, -2, 5],
    [2, 8, 7]
]
det_3x3_nz = determinant_recursive(matrix_3x3_nonzero)
print(f"\nМатрица 3×3: {matrix_3x3_nonzero}")
print(f"Определитель = {det_3x3_nz}")

# --- Пример использования ---
print("\n" + "=" * 50)
print("МЕТОД 2: Метод Гаусса")
print("=" * 50)

matrix_test = [
    [2, 1, 1],
    [4, -6, 0],
    [-2, 7, 2]
]

det_gauss = determinant_gauss(matrix_test)
print(f"\nМатрица: {matrix_test}")
print(f"Определитель (Гаусс) = {det_gauss}")