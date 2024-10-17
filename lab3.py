def sort_string_func1(strings_array):
    def char_frequency(string):
        dictionary = {}
        for char in string:
            dictionary[char] = dictionary.get(char, 0) + 1
        return dictionary
    sorted_strings = sorted(strings_array, key=lambda x: (lambda freq: max(freq.values()) - min(freq.values()))(char_frequency(x)))
    return sorted_strings

path = "text.txt"
text = open(path, 'r', encoding='UTF-8').read().splitlines()

print("Полученные строки\n", text)
print("Отсортированные строки\n", sort_string_func1([line for line in text if line.strip()]))