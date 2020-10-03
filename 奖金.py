gain = 0  
def bonus(month):
    global gain
    if month < 6:
        gain = 500
       
    elif 6 <= month <= 12:
        gain = 120 * month
        
    else:
        gain = 180 * month
        
        
def info(name, month):
    bonus(month)
    print('%s来了%s个月，获得奖金%s元' % (name, month, gain)) 

info('大聪',14)