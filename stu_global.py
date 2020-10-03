num1 = 0
num2 = 1

print('未经过计算(函数外)：num1 = %d, num2 = %d' % (num1,num2))

def jisuan1():
    global num1
    print('第一次计算前(函数中)：num1 = %d, num2 = %d' % (num1,num2))
    num1 = num1 + 1
    print('第一次计算后(函数中)：num1 = %d, num2 = %d' % (num1,num2))
    return num1

def jisuan2():
    global num1
    num3 = 5
    print('第二次计算前(函数中)：num1 = %d, num2 = %d, num3 = %d' % (num1,num2,num3))
    num1 = num1 + num2 + num3
    print('第二次计算后(函数中)：num1 = %d, num2 = %d, num3 = %d' % (num1,num2,num3))
    return num1,num2,num3

result1 = jisuan1()
print('第一次计算后(函数外)：num1 = %d, num2 = %d,\n结果为：result1 = %d' % (num1,num2,result1))
result2,result3,result4 = jisuan2()
print('第二次计算后(函数外)：num1 = %d, num2 = %d, num3=%d,\n结果为：result2 = %d, result3 = %d' % (num1,num2,result2,result3,result4))