# 문제 설명
# 게임 캐릭터를 4가지 명령어를 통해 움직이려 합니다. 명령어는 다음과 같습니다.
# U: 위쪽으로 한 칸 가기
# D: 아래쪽으로 한 칸 가기
# R: 오른쪽으로 한 칸 가기
# L: 왼쪽으로 한 칸 가기
# 캐릭터는 좌표평면의 (0, 0) 위치에서 시작합니다. 좌표평면의 경계는 왼쪽 위(-5, 5), 왼쪽 아래(-5, -5), 오른쪽 위(5, 5), 오른쪽 아래(5, -5)로 이루어져 있습니다.
# 우리는 게임 캐릭터가 지나간 길 중 캐릭터가 처음 걸어본 길의 길이를 구하려고 합니다
# 명령어가 매개변수 dirs로 주어질 때, 게임 캐릭터가 처음 걸어본 길의 길이를 구하여 return 하는 solution 함수를 완성해 주세요.
import math


def solution(dirs):
    answer = 0
    m = 5  #좌표 맥스값
    matrix = [] #이동한 위치넣을 리스트  원소 : '현재위치이동위치' => U일경우, matrix.append('0001')
    x, y = 0, 0 #현재 위치
    for dir in dirs:
        mx,my = 0, 0
        if dir == "U" and y < m:
            my += 1
        elif dir == "D" and y > -m:
            my -= 1
        elif dir == "R" and x < m:
            mx += 1
        elif dir == "L" and x > -m:
            mx -= 1
        else:
            continue
        way = [f'{x}{y}{x+mx}{y+my}', f'{x+mx}{y+my}{x}{y}'] #현재->이동위치 , 이동위치 -> 현재위치 는 이동하는 곳만 다를 뿐 같은 길이다.
        if all(w not in matrix for w in way): #이동한 길이 matrix 에 없다면 처음 가본 길이다.
            matrix.append(way[0])
            answer += 1
        x += mx
        y += my

    # answer = len(matrix)
    return answer


# dirs = "ULURRDLLU"
dirs ="RL"
result = solution(dirs)
print("result = ", result)
