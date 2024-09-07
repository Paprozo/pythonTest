import json
import sys

def findValue(id, values):
    for value in values:
        if value['id'] == id:
            return value['value']        
    return False

def find(tests, values):
    result = []
    for test in tests:
        value = findValue(test['id'], values)
        if value != False:
            test['value'] = value
        if 'values' in test:
            test['values'] = find(test['values'], values)
        result.append(test)
    return result


path1, path2, path3 = sys.argv[1], sys.argv[2], sys.argv[3]
file1 = open(path1, 'r')
file2 = open(path2, 'r')
file3 = open(path3, 'w')
tests = json.load(file1)
values = json.load(file2)
res = find(tests['tests'], values['values'])
result = {'tests':[]}
result['tests'] = res
json.dump(result, file3, indent=4)
