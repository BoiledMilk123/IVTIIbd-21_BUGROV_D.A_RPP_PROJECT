
def get_keyboard_elem(str_input = None, str_error = None): # функция для ввода элемента с клавиатуры. str_inpt - сообщение пользователю перед \
    x = None                                               # вводом, str_error - сообщение пользователю при ошибке ввода
    while x is None:
        try:
            print(str_input)
            x = int(input("Ввод: "))
            print('\n')
        except(ValueError):
            x = None
            print('\n')
            print(str_error)
    return x


def get_keyboard_elem_options(options, str_input = None, str_error = None): # функция для ввода элемента (дочерняя от get_keyboard_elem), \
    x = None                                                                # ограниченного значениями списка options, с клавиатуры
    while x is None:
        try:
            print(str_input)
            x = int(input("Ввод: "))
            if x not in options: raise ValueError
            print('\n')
        except(ValueError):
            x = None
            print('\n')
            print(str_error)
    return x


def get_keyboard_list(n): #функция для ввода элементов списка с клавиатуры
    a = []
    str2 = "Ошибка ввода! Пожалуйста, введите целочисленное значение элемента списка."
    for i in range(n):
        str1 = f"Введите значение [{i}-ого] элемента."
        a.append(get_keyboard_elem(str1, str2))
    return a#


def get_random_list(n): # функция для генерации списка размерностью n из случайных элементов
        import random

        str_random_elem_input = "Введите значение начала диапазона для генерации элементов списка."
        str_random_elem_error = "Ошибка ввода! Пожалуйста, введите целочисленное значение."
        start = get_keyboard_elem(str_random_elem_input, str_random_elem_error)

        str2_random_elem_input = "Введите значение конца диапазона для генерации элементов списка."
        str2_random_elem_error = str_random_elem_error
        end = None

        while end is None:
            try:
                end = get_keyboard_elem(str2_random_elem_input, str2_random_elem_error)
                if end < start: raise ValueError
            except(ValueError):
                end = None
                print("Ошибка ввода! Значение конца диапазона должно быть не меньше значения его начала.")
                print('\n')

        a = []
        for i in range(n):
            a.append(random.randint(start, end))
        return a


def find_max_chain(a, str_list_name): # функция для поиска самой длинной подцепочки в списке a.
    k=1                               # str_list_name - название массива для генерации сообщения об окончании работы функции
    k_max = -1                        # возвращает пару значений: ind_max - индекс последнего элемента самой длинной подцепочки и k_max - кол-во элементов в самой длинной подцепочке списка
    ind_max = -1

    flag_a = False
    for i in range(1, len(a)):
       if a[i] == a[i-1]:
           flag_a = True
           k += 1

           if k > k_max:
               k_max = k
           if flag_a is True and i + 1 == len(a):
               ind_max = i
       elif flag_a is True:
            ind_max = i-1
            k = 1
            flag_a = False

    if k_max == -1:
        print(f"В списке {str_list_name} подцепочка не существует. Задайте список ещё раз")
        raise SystemExit

    print(f"В списке {str_list_name} самая длинная цепочка:")
    for i in range(ind_max - k_max + 1, ind_max + 1):
        print(a[i], end=" ")
    print(f"(элементы с {ind_max - k_max + 2} по {ind_max + 1}).")
    return [ind_max, k_max]


def my_solve(): # функция, реализующая выданный по варианту алгоритм, без использования системных функций
    global a, b

    print(f"Список А[{len(a)}]:", end = " ") #вывод списков
    for i in a:
        print(i, end = " ")
    print()

    print(f"Список B[{len(b)}]:", end=" ")
    for i in b:
        print(i, end = " ")
    print()

    chain_a = find_max_chain(a, "A") # поиск индексов подцепочек в массивах
    chain_b = find_max_chain(b, "B")
    str_a = ""
    str_b = ""
    chain_a_str = ""
    chain_b_str = ""

    for i in range(chain_a[0] - chain_a[1] + 1, chain_a[0] + 1): # запись подцепочек списка в строковую переменную
        chain_a_str += str(a[i])

    for i in range(chain_b[0] - chain_b[1] + 1, chain_b[0] + 1):
        chain_b_str += str(b[i])

    flag = False # записываем в новый список значения вне подцепочки. значения старого списка, входящие в подцепочку, пропускаем. вместо них записываем значения подцепочки другого массива
    for i in range(len(a)):
        if (i >= chain_a[0] - chain_a[1] + 1) and (i <= chain_a[0]):
            if flag is True:
                continue
            str_a += chain_b_str
            flag = True
        else:
            str_a += str(a[i])

    flag = False
    for i in range(len(b)):
        if (i >= chain_b[0] - chain_b[1] + 1) and (i <= chain_b[0]):
            if flag is True:
                continue
            str_b += chain_a_str
            flag = True
        else:
            str_b += str(b[i])

    print("Список А после перестановки в него цепочки из списка B:") # вывод новых списков
    print(f"А[{len(str_a)}]:", end = " ")
    for i in str_a:
        print(i, end=" ")
    print()

    print("Список B после перестановки в него цепочки из списка A:")
    print(f"B[{len(str_b)}]:", end=" ")
    for i in str_b:
        print(i, end=" ")
    print()


def system_solve(): # функция, реализующая выданный по варианту алгоритм, с использованием системных функций
    global a, b

    str_a = ""
    str_b = ""

    print(f"Список А[{len(a)}]:", end=" ")
    for i in a:
        print(i, end=" ")
        str_a += str(i)
    print()

    print(f"Список B[{len(b)}]:", end=" ")
    for i in b:
        print(i, end=" ")
        str_b += str(i)
    print()

    chain_a = find_max_chain(a, "A")
    chain_b = find_max_chain(b, "B")

    chain_a_str = ""
    chain_b_str = ""

    for i in range(chain_a[0] - chain_a[1] + 1, chain_a[0] + 1):
        chain_a_str += str(a[i])

    for i in range(chain_b[0] - chain_b[1] + 1, chain_b[0] + 1):
        chain_b_str += str(b[i])

    str_a = str_a.replace(chain_a_str, chain_b_str) # используем системную функцию replace
    str_b = str_b.replace(chain_b_str, chain_a_str)

    print("Список А после перестановки в него цепочки из списка B:")
    print(f"А[{len(str_a)}]:", end=" ")
    for i in str_a:
        print(i, end=" ")
    print()

    print("Список B после перестановки в него цепочки из списка A:")
    print(f"B[{len(str_b)}]:", end=" ")
    for i in str_b:
        print(i, end=" ")
    print()



str_a_input = ("Выберите способ заполнения списка A (введите цифру соответствующего варианта):\n \
\t 1.Ввод с клавиатуры.\n \
\t 2.Автоматическая генерация.")

str_input_error = ("Ошибка ввода! Пожалуйста, введите ""1"" или ""2"". \n")

selectionA = get_keyboard_elem_options([1,2], str_a_input, str_input_error)

str1_a_n = ("Введите размерность списка:")

str2_a_n = ("Ошибка ввода! Пожалуйста, введите целочисленное значение размерности списка.")

N_A = get_keyboard_elem(str1_a_n, str2_a_n)

match selectionA:
    case 1:
        a = get_keyboard_list(N_A)
    case 2:
        a = get_random_list(N_A)

str_b_input = ("Выберите способ заполнения списка B (введите цифру соответствующего варианта):\n \
\t 1.Ввод с клавиатуры.\n \
\t 2.Автоматическая генерация.")

selectionB = get_keyboard_elem_options([1,2], str_b_input, str_input_error)

str1_b_n = str1_a_n

str2_b_n = str2_a_n

N_B = get_keyboard_elem(str1_b_n, str2_b_n)

match selectionB:
    case 1:
        b = get_keyboard_list(N_B)
    case 2:
        b = get_random_list(N_B)

my_solve()
print()
system_solve()
