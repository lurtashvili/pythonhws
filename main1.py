var = (1,)

print(type(var), var)


var1, var2, *var3 = 1,2,3,4 

print(type(var1), var1)
print(type(var2), var2)
print(type(var3), var3)


z = tuple([1,2,3])
for i in z:
    print(i)


y = (1,2,3,4,[2,3,4,5,6,7,8])
print(f'y 0={y[0]}')

print(y[1:5])
print(y.count(3))
print(y.index(4))
print(len(z+y))
print(z==y)
print(z>=y)