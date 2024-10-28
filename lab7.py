def find_min_product(arr:list, K:int):
    N = len(arr)
    if N < 3 * K:
        return None
    min_from_start = [float('inf')] * N
    min_from_end = [float('inf')] * N

    for i in range(N - 2 * K):
        min_from_start[i] = min(arr[i], min_from_start[i - 1] if i > 0 else float('inf'))

    for i in range(N - 1, 2 * K - 1, -1):
        min_from_end[i] = min(arr[i], min_from_end[i + 1] if i < N - 1 else float('inf'))

    min_product = float('inf')
    for j in range(K, N - K):
        left_min = min_from_start[j - K]
        right_min = min_from_end[j + K]
        product = left_min * arr[j] * right_min
        if product < min_product:
            min_product = product

    return min_product % 10 ** 6


array_from_file_A = list(map(int, open('27-167a.txt', 'r', encoding='UTF-8').read().split()))
array_from_file_B = list(map(int, open('27-167b.txt', 'r', encoding='UTF-8').read().split()))
a_delay = array_from_file_A[1]
b_delay = array_from_file_B[1]

array_a = array_from_file_A[2:array_from_file_A[0] + 2]
array_b = array_from_file_B[2:array_from_file_B[0] + 2]

print("Минимальное произведение для массива из файла 27-167a.txt:", find_min_product(array_a, a_delay))
print("Минимальное произведение для массива из файла 27-167b.txt:", find_min_product(array_b, b_delay))
