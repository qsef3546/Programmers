example1 = "one4seveneight"


digit = {'zero':'0','one':'1','two':'2','three':'3','four':'4',
         'five':'5','six':'6','seven':'7','eight':'8','nine':'9'}


def solution(s):
    res = s
    for i in digit.keys():
        res= res.replace(i,digit[i])
    answer = int(res)
    return answer


print('result = ', solution(example1))