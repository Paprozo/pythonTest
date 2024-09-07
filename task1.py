import sys

n, m = int(sys.argv[1]), int(sys.argv[2])
result = '1'
i = 1
flag = False
while flag == False:
    i += m - 1
    if i>n:
        i = i - n    
    if i == 1:
        flag = True
    else:
        result += str(i)   
print(result)    
