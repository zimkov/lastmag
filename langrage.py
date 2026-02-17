def lagrange_interpolation(x_points, y_points, x_target):
    """
    Вычисляет значение интерполяционного полинома Лагранжа в точке x_target.
    
    :param x_points: Список координат X известных точек
    :param y_points: Список координат Y известных точек
    :param x_target: Точка X, в которой нужно найти значение Y
    :return: Приближенное значение Y в точке x_target
    """
    
    # Проверка, что количество точек совпадает
    if len(x_points) != len(y_points):
        raise ValueError("Количество координат X и Y должно совпадать")

    n = len(x_points)
    result = 0.0

    # Основной цикл по формуле Лагранжа: сумма (y_j * l_j(x))
    for j in range(n):
        # Вычисляем j-й базисный полином l_j(x)
        term = y_points[j]
        
        for i in range(n):
            if i != j:
                # Формула произведения: (x - x_i) / (x_j - x_i)
                term *= (x_target - x_points[i]) / (x_points[j] - x_points[i])
        
        # Добавляем полученное слагаемое к общему результату
        result += term

    return result

# --- Пример использования ---

# 1. Задаем известные точки (например, параболу y = x^2)
# Точки: (1, 1), (2, 4), (3, 9)
x_data = [1, 2, 3]
y_data = [1, 4, 9]

# 2. Точка, в которой хотим найти значение (интерполируем)
x_query = 2.5

# 3. Вычисляем
y_result = lagrange_interpolation(x_data, y_data, x_query)

# 4. Вывод результата
print(f"Известные точки: {list(zip(x_data, y_data))}")
print(f"Ищем значение в точке X = {x_query}")
print(f"Результат интерполяции Y = {y_result}")
print(f"Реальное значение (2.5^2) = {2.5**2}")

# --- Дополнительный пример с визуализацией (если установлен matplotlib) ---
try:
    import matplotlib.pyplot as plt
    import numpy as np

    # Генерируем много точек для красивой линии графика
    x_range = np.linspace(min(x_data) - 1, max(x_data) + 1, 100)
    y_range = [lagrange_interpolation(x_data, y_data, x) for x in x_range]

    plt.figure(figsize=(8, 6))
    plt.plot(x_range, y_range, label='Полином Лагранжа', color='blue')
    plt.scatter(x_data, y_data, color='red', s=100, label='Исходные точки', zorder=5)
    plt.scatter(x_query, y_result, color='green', s=100, label=f'Результат ({x_query}, {y_result:.2f})', zorder=5)
    
    plt.title('Интерполяция Лагранжа')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.grid(True)
    plt.show()

except ImportError:
    print("\nБиблиотека matplotlib не найдена. График не будет построен, но расчет выполнен верно.")