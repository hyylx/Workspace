import json
d = dict(name='Bob', age=20, score=88)
a = json.dumps(d)
print(a)
print(type(a))