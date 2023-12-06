def funct(p=10,q=20):
    p += q
    q += 1
    print(p,q)
funct(q=20,p=10)    #30 21


def test():
    x = 10
x = 11
test()
print(x)             #11