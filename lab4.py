
def is_max(array, index):
    return array[index] == max(array)

def is_min(array, index):
    return array[index] == min(array)

def circle_shift(array):
    result_array=[0]*(len(array))
    for i in range(len(array)):
        result_array[(i+1)%len(array)]=array[i]
    return result_array

def print_array(array):
    result_array = []
    for i in range(len(array)):
        if array[i] % 2 == 0:
            result_array.append(array[i])
    for i in range(len(array)):
        if array[i] % 2 != 0:
            result_array.append(array[i])
    return result_array

def task51(array):
    l1=list(set(array))
    l2=[]
    for i in l1:
        counter=0
        for j in array:
            if i==j:counter+=1
        l2.append(counter)
    return l1,l2

array = list(map(int, input("Введите массив через пробел (enter для прекращения ввода\n").split()))
while True:
    select_function=int(input("Введите номер функции (для выхода введите 0):"
                              "\n1: Проверка на локальный максимум\n"
                              "2: Проверка на локальный минимум\n"
                              "3: Измененный массив\n"
                              "4: Отсортированный массив\n"
                              "5: Уникальные элементы и количество повторов\n"
                              "6: Изменить массив\n"))
    if select_function==0:break
    elif select_function==1:print("Это локальный максимум" if is_max(array,int(input("Введите индекс: "))) else "Это не локальный максимум")
    elif select_function==2:print("Это локальный минимум" if is_min(array,int(input("Введите индекс: "))) else "Это не локальный минимум")
    elif select_function==3:print("Измененный массив:\t",circle_shift(array))
    elif select_function==4:print("Отсортированный массив:\t",print_array(array))
    elif select_function==5:print("Уникальные элементы и количество повторов\n"
                                  "l1: ",task51(array)[0],"\n"
                                  "l2: ",task51(array)[1])
    elif select_function==6: array = list(map(int, input("Введите массив через пробел (enter для прекращения ввода\n").split()))
    else: print("Такой функции нет")