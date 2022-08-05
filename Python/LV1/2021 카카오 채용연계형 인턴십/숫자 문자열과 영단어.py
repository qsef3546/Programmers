example1 = "one4seveneight"

#숫자 사전
digit = {'zero':'0','one':'1','two':'2','three':'3','four':'4',
         'five':'5','six':'6','seven':'7','eight':'8','nine':'9'}


def solution(s):
    res = s

    #영문자는 숫자(string)으로 변경
    for i in digit.keys():
        res= res.replace(i,digit[i])
        
    #convert string to int
    answer = int(res)
    return answer


print('result = ', solution(example1))