import json


fname = 'file3_again.py'
jname = 'jfile1_8.json'
with open(fname, 'r') as f, open(jname, 'w') as j:
    mydict = {}
    for line in f:
        key, value = line.split(':')
        print(key, value)
        mydict[key.title()] = float(value)
    json.dump(mydict, j, separators=(',\n', ':'), ensure_ascii=False)