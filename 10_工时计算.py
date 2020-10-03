import math
# 采集信息的函数，即采集项目大小size，工时time，人力number
def myinput(): 
    choice = input('请选择计算类型：（1-工时计算，2-人力计算）')
    if choice == '1':
        size = float(input('请输入项目大小：（1代表标准大小，请输入小数）'))
        number = int(input('请输入人力数量：（请输入整数）'))
        time = None #由于计算的是工时，所以time赋值空值
        return size,number,time
        # 这里返回的数据是元组(size，number，time)
    if choice == '2':
        size = float(input('请输入项目大小：（1代表标准大小，请输入小数）'))
        number = None
        #由于计算的是人力，所以number赋值空值
        time = float(input('请输入工时数量：（请输入小数）'))
        return size,number,time
        # 这里返回的是一个元组(size，number，time)
# 完成计算的函数
def estimated(my_input):
    # 把元组(size，number，time)中的数据取出来
    size = my_input[0]
    number = my_input[1]
    time = my_input[2]
    # 人力计算
    if (number == None) and (time != None):
    #当人力number为空值，工时time非空值时执行以下代码 
        number = math.ceil(size * 80 / time)
        print(number)
        print('项目大小为%.1f个标准项目，如果需要在%.1f个工时完成，则需要人力数量为：%d人' %(size,time,number)) 
    # 工时计算
    elif (number != None) and (time == None):
    #当人力 number非空值，时间time为空值时，执行以下代码
        time = size * 80 / number
        print(time)
        print('项目大小为%.1f个标准项目，使用%d个人力完成，则需要工时数量为：%.1f个' %(size,number,time))  
# 主函数
def main():
#调用函数myinput，并将返回值元组(size，number，time)赋值给my_input
    my_input = myinput()
#将元组(size，number，time)作为参数传递给函数estimated
    estimated(my_input)
# 调用主函数
main()