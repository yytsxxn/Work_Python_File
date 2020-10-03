import math
choice=int(input('请选择计算类型：（1-人力计算，2-工时计算）'))
def estimated_time():
        number=int(input('请输入人力数量：（请输入整数）'))
        size=float(input('请输入项目大小：（1代表标准大小，可以输入小数）'))
        time=size*80/number
        print('项目大小为%.1f个标准项目，使用%d个人力完成，则需要工时数量为：%.1f个' %(size,number,time))
def estimated_number():
        size=float(input('请输入项目大小：（1代表标准大小，可以输入小数）'))
        time= float(input('请输入工时数量：（请输入小数）'))
        number=size*80/time
        print('项目大小为%.1f个标准项目，如果需要在%.1f个工时完成，则需要人力数量为：%d人' %(size,time,number))
if choice==1:
    estimated_time()
else:
    estimated_number()