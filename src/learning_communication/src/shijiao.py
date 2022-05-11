
def test1():
    global a
    a = 3
    test2()
def test2():
    # a = a+1
    a=a+1
    print(a)
test1()