scores = {'语文':89, '数学':95, '英语':80}
sum_score = 0

def get_average(scores):
    global sum_score
    for subject, score in scores.items():
        sum_score += score
        print('现在的总分是%d'%sum_score)
    ave_score = sum_score/len(scores)
    print('平均分是%d'%ave_score)

get_average(scores)