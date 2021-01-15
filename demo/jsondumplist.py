import json
a = []
k={'a':1,'b':2}
l={'c':3,'d':4}
a.append(k)
a.append(l)
d = json.dumps(a)
print(d)