import numpy as np

# numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
# hand = "right"

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
hand = "left"

# 1 ~ 12 키패드 딕셔너리
# key : 키패드 문자
# value : 키패드 위치 3*4행렬 index 
rec = {x+1 : np.array([x//3,x%3]) for x in range(0,12)} 

# 10 ~ 12 key를 키패드 문자에 맞게 각각 '*' '0' '#' 로 변경
rec['*'] = rec.pop(10)
rec[0] = rec.pop(11)
rec['#'] = rec.pop(12)

L_position = [1,4,7] # 왼손 엄지손가락만 사용하는 번호
R_position = [3,6,9] # 오른손 엄지손가락만 사용하는 번호

#이동할 위치를 누르는 손가락 선택 함수
def distance(LR_position,num,cur,hand):
    # '0' 키패드 문자를 제외한 번호가 왼/오른손 손가락만 사용하는 번호인지 확인
    if num in L_position + R_position :
        return [cur,'L'] if num in L_position else [cur, 'R']

    # 이동해야하는 거리 계산 (이동거리 =  이동할 위치 - 현재 왼/오른손 엄지손가락 위치)
    Ltonum = sum(abs(LR_position['L']-cur))
    Rtonum = sum(abs(LR_position['R']-cur))

    #이동거리가 같다면 주로사용되는 손의 엄지손가락으로 이동
    if Ltonum - Rtonum == 0 :
        return [cur,'L'] if hand == 'left' else [cur,'R']

    #이동거리가 짧은 손의 엄지손가락으로 이동
    return [cur,'L'] if Ltonum < Rtonum else [cur,'R']



def solution(numbers, hand):
    answer = ''
    #현재 왼손/오른손 엄지손가락 위치 설정
    LR_position={'L' : rec['*'] , 'R' : rec['#']}

    #이동하려는 위치 반복
    for num in numbers:

        # distance() : 이동할 손가락 확인 함수
        # res = 이동할 위치
        # move = 이동할 엄지손가락
        res, move = distance(LR_position, num, rec[num], hand)
        # 이동할 엄지손가락에 이동할 위치 대입
        LR_position[move] = res
        answer += move
    return answer

anw = solution(numbers,hand)

print('answer = ', anw)