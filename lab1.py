def dividers(n):
    dividers=[]
    for i in range(1, n+1):
        if n % i == 0: dividers.append(i)
    return dividers
def is_prime(x):
    for i in range(2, (x//2)+1):
        if x % i == 0:
            return False
    return True

def func_1(n):
    max_prime = None
    for i in dividers(n):
        if is_prime(i):
            if max_prime is None or i > max_prime:
                max_prime = i
    return max_prime
def func_2(n):
    numbers = []
    answer = 1
    while n > 0:
        numbers.append(n % 10)
        n //= 10
    for i in numbers:
        if i % 5 != 0:
            answer *= i
    return answer
def func_3(n):
    max_comp=None
    for i in dividers(n):
        if is_prime(i)==False and i%2!=0 and (max_comp is None or i > max_comp): max_comp=i
    if max_comp==None: return "Не существует"
    gcd=max(dividers(max_comp))
    n=gcd
    mul_gcd = 1
    while n > 0:
        mul_gcd *= n % 10
        n //= 10
    return gcd, mul_gcd

print("Текущее число N:",N,\
      "\n Функция 1: ",func_1(N),
      "\n Функция 2: ",func_2(N),
      "\n Функция 3: ",func_3(N))
