import numpy as np

# Функция из предоставленного файла для ввода целых чисел с клавиатуры
def get_keyboard_elem(str_input=None, str_error=None):
    """
    Функция для ввода целого числа с клавиатуры с обработкой ошибок.
    str_input - сообщение перед вводом, str_error - сообщение при ошибке.
    """
    x = None
    while x is None:
        try:
            print(str_input)
            x = int(input("Ввод: "))
            print('\n')
        except ValueError:
            x = None
            print('\n')
            print(str_error)
    return x

def generate_matrix(N, M, start, end):
    """
    Генерирует матрицу размером N x M со случайными целыми числами в диапазоне [start, end).
    """
    return np.random.randint(start, end, size=(N, M))

def calculate_total_sum(matrix):
    """
    Вычисляет общую сумму всех элементов матрицы.
    """
    return np.sum(matrix)

def calculate_row_sums(matrix):
    """
    Вычисляет сумму элементов каждой строки матрицы.
    """
    return np.sum(matrix, axis=1)

def calculate_fractions(row_sums, total_sum):
    """
    Вычисляет долю суммы каждой строки в общей сумме матрицы.
    """
    return row_sums / total_sum

def create_result_matrix(original_matrix, fractions):
    """
    Создаёт результирующую матрицу, добавляя к исходной матрице столбец с долями.
    """
    fractions_column = fractions.reshape(-1, 1)  # Преобразуем массив долей в столбец
    return np.hstack((original_matrix, fractions_column))

def save_matrices(original_matrix, result_matrix):
    """
    Сохраняет исходную и результирующую матрицы в текстовые файлы.
    """
    np.savetxt('original_matrix.txt', original_matrix, fmt='%d')  # Целые числа для исходной матрицы
    np.savetxt('result_matrix.txt', result_matrix, fmt='%.6f')   # Дроби с 6 знаками после запятой

def main():
    """
    Основная функция программы: управляет вводом данных, обработкой матрицы и выводом результатов.
    """
    # Ввод количества строк N
    str_n_input = "Введите количество строк N:"
    str_n_error = "Ошибка ввода! Пожалуйста, введите целочисленное значение для N."
    N = get_keyboard_elem(str_n_input, str_n_error)

    # Ввод количества столбцов M
    str_m_input = "Введите количество столбцов M:"
    str_m_error = "Ошибка ввода! Пожалуйста, введите целочисленное значение для M."
    M = get_keyboard_elem(str_m_input, str_m_error)

    # Ввод начала диапазона для генерации элементов
    str_start_input = "Введите начало диапазона для генерации элементов матрицы:"
    str_start_error = "Ошибка ввода! Пожалуйста, введите целочисленное значение."
    start = get_keyboard_elem(str_start_input, str_start_error)

    # Ввод конца диапазона с проверкой корректности
    str_end_input = "Введите конец диапазона для генерации элементов матрицы:"
    str_end_error = "Ошибка ввода! Пожалуйста, введите целочисленное значение."
    end = None
    while end is None:
        try:
            end = get_keyboard_elem(str_end_input, str_end_error)
            if end < start:
                raise ValueError
        except ValueError:
            end = None
            print("Ошибка ввода! Конец диапазона должен быть не меньше начала.")
            print('\n')

    # Генерация матрицы A
    A = generate_matrix(N, M, start, end)

    # Вычисление общей суммы элементов матрицы
    total_sum = calculate_total_sum(A)
    if total_sum == 0:
        print("Сумма всех элементов матрицы равна нулю. Невозможно вычислить доли.")
        return

    # Вычисление сумм по строкам
    row_sums = calculate_row_sums(A)

    # Вычисление долей
    fractions = calculate_fractions(row_sums, total_sum)

    # Создание результирующей матрицы
    result_matrix = create_result_matrix(A, fractions)

    # Сохранение матриц в файлы
    save_matrices(A, result_matrix)

    # Вывод матриц на экран для проверки
    print("Исходная матрица A:")
    print(A)
    print("Результирующая матрица:")
    print(result_matrix)

if __name__ == "__main__":
    main()