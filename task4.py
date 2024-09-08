import sys

path = sys.argv[1]
file = open(path, 'r')
array = []
for line in file:
    if line.strip():
        array.append(int(line))
median = round(sum(array)/len(array))
result = 0
for element in array:
    if element > median:
        result += element - median
    else:
        result += median - element
print(result)