from collections import namedtuple


Person = namedtuple('Person', ['name', 'age'])


ali = Person('Ali',18)
vali = Person('Vali',20)

print(ali.name, ali.age)
print(vali.name, vali.age)
