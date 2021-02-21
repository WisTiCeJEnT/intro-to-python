def fn():
    x = 10
    print(x)
    return x

def fn2():
    print(x)

x = 20
print(x)
a = fn()
print(x)
fn2()
print(a)
