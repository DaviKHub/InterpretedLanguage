import random
def task3(string):
    if string == None:
        return "Ошибка"
    array_string = string.split(" ")
    random.shuffle(array_string)
    return " ".join(array_string)
def task8(string):
    if string == None:
        return "Ошибка"
    count=0
    for i in string.split(" "):
        if len(i)%2==0:
            count+=1
    return count
def task16(array_string):
    array_string.sort(key=lambda x: ["белый", "синий", "красный"].index(x))
    return array_string
print(task16(['синий','белый','красный']))
print(task8("hello world python"))
print(task3("hello world python"))