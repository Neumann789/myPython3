__author__ = 'fanghuabao'

X = set('spam')
Y = {'h', 'a', 'm'}

print(X, Y)
print((X, Y))

print(X & Y)
print(X | Y)
print(X - Y)

Z = {x**2 for x in [1, 2, 3]}
print(Z)
