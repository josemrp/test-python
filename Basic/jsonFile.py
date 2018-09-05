import json

x = [55, 'joe', 'romero']

f = open('test.json', 'w')
json.dump(x, f)
f.close()
