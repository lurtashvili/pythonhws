var = set([1,2,3,4,5])
print(type(var), var)

var.add("word")
print(var)
z = {1,2,3,4,5}
print(z)

for i in z:
    print(i)

z.add("word")
print(z)

z.remove(2)
print(z)

var.pop()
print(var, z)
print(var.difference(z))
print(z.intersection(var))
a = var.union(z)
print(a)
b = set([2,2,3,4,3,5,6,5,6,7,8,9,9,10])
print(b)
var1 = frozenset([1, 2, 3, 4, 5])
print(type(var1),var1)

b.discard(z)
print(b)




