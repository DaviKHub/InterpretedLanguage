state=int(input("Введите количество штатов: "))
var={}
for _ in range(state):
    (surname, count_calls)=map(str,input().split())
    var[surname]=var.get(surname,0)+int(count_calls)
for surname, count_calls in sorted(var.items()):
    print(f"{surname} {count_calls}")
