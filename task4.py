import sys

path = int(sys.argv[1])
path = input('Введите путь к файлу: ')
file = open(path, 'r')
array = list(map(int, file.read().split("\n")))
median = round(sum(array)/len(array))
result = 0
for element in array:
    if element > median:
        result += element - median
    else:
        result += median - element

print(result)