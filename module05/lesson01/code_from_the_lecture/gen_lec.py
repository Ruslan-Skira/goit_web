def g_m():
    print('before first yield')
    yield 1
    print('after first yield')
    yield 2
    print('End')

g = g_m()

print(next(g))
print(next(g))
print(next(g))