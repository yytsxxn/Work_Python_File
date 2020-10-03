import math
# 工时计算
def estimated_time(size,number):
    time = size*80/number
    return time

# 人力计算
def estimated_number(size,time):
    number = math.ceil(size*80/time)
    return number
print('项目大小为1.5个标准项目，使用2个人力完成，需要工时数为：'+str(estimated_time(1.5,2)))
print('项目大小为0.5个标准项目，如果需要在20.0个工时完成，则需要人力数为：'+str(estimated_number(0.5,20)))

# 调用工时计算函数
estimated_time(1.5,2)
# 调用人力计算函数
estimated_number(0.5,20)