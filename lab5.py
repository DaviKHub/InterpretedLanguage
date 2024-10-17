N, M = map(int, input("Введите N, M: ").split())
colors_A = set(list(map(int, input("Введите номера цветов для N:\n").split()))[:N])
colors_B = set(list(map(int, input("Введите номера цветов для M:\n").split()))[:M])

common_colors = colors_A & colors_B
only_A_colors = colors_A - colors_B
only_B_colors = colors_B - colors_A

print ("Общие элементы\t", len(common_colors),"\t",sorted(common_colors))
print ("Только элементы A\t",len(only_A_colors),"\t",sorted(only_A_colors))
print ("Только элементы B\t",len(only_B_colors),"\t",sorted(only_B_colors))