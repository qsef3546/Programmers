# 1. solution 함수에 parameter가 자동으로 넘어옵니다.
# solution 함수만 작성하시면 됩니다. (추가 함수 정의 가능)
# 춘식이의 파티 준비
# 춘식이는 이번 생일 파티에 오는 친구들을 위해 쿠키를 만들기로 했습니다.
# 춘식이네 집에는 다양한 크기의 직사각형 쿠키판이 있습니다. 이번에 초대한 친구 K 명에게 가능한 가장 큰 크기의 쿠키를 나누어 주려 합니다. 이 때, 쿠키커터의 모양이 정사각형이라면,
# 춘식이가 사야 하는 쿠키커터의 변의 길이를 구해 주세요.
# 단 쿠키판의 가로와 세로, 쿠키커터의 변의 길이는 모두 자연수이며, 쿠키판과 쿠키커터는 회전시킬 수 없습니다. 또한, 쿠키커터의 각 변은 쿠키판의 변 한 개 이상과 평행합니다.
# K 개 보다 많은수의 쿠키를 만드는 것도 K 개를 만드는 것에 속합니다.
# 입력:
# friendsCnt: 춘식이가 초대한 친구 K명 (1 <= K <= 10,000, 정수)
# cookiePanDims: 춘식이가 가지고 있는 쿠키판의 너비 및 높이의 배열,
#   (1 <= 너비, 높이 <= 1,000,000이고,  쿠키판 종류 갯수는 1이상 1000개 이하)
# 출력:
# 사야하는 쿠키 커터의 너비 출력
# 예시:
# friendsCnt = 3;
# cookiePanDims = [[2,2],[4,2]];
# 초대한 친구 수: 3 명
# 쿠키판이 총 2 개가 주어졌다.
#   쿠키판의 [너비x높이] 조합이 [2x2], [4x2] 일 때,
# 정사각형의 너비가 2 인 쿠키 커터 1개를 사서
# [2x2] 쿠키판에서 1개의 쿠키 제작
# [4x2] 쿠키판에서 2개의 쿠키 제작
# 3명에게 모두 같고 최대 크키의 쿠키를 나눠 줄 수있다.
# 따라서 정답은 2

from functools import reduce
from math import sqrt
def solution(friendsCnt, cookiePanDims):
    answer = 0
    sd = [x[0] * x[1] for x in cookiePanDims]
    s = int(sqrt(reduce(lambda x, y: x + y[0]*y[1], cookiePanDims, 0) // friendsCnt))
    w = min(list(filter(lambda x: x <= s, sum(cookiePandims, []))))
    return w


friendsCnt = 3
#cookiePandims = [[2, 2], [4, 2]]
cookiePandims = [[2,7],[3,5]]

answer = solution(friendsCnt, cookiePandims)

print('answer = ',answer)