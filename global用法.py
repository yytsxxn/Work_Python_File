a = 1
b = 2
print(a,b)
print('---------')
def f1():
    global a
    #print(a,b)
    #print('--------')
    a = 3
    b = 4
    print(a,b)
    print('-------')
f1()
print(a,b)