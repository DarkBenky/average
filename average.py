l = [0,1,2]


def test():
    c = 0
    for i in l:
        c = c + 1
        if c == 5:
            l.pop(0)
    x = int(input("value :"))
    l.append(x)
    print(l)
test()
test()
test()
test()
test()
test()
