# 문제 설명
# ROR 게임은 두 팀으로 나누어서 진행하며, 상대 팀 진영을 먼저 파괴하면 이기는 게임입니다. 따라서, 각 팀은 상대 팀 진영에 최대한 빨리 도착하는 것이 유리합니다.
#
# 게임 맵의 상태 maps가 매개변수로 주어질 때, 캐릭터가 상대 팀 진영에 도착하기 위해서 지나가야 하는 칸의 개수의 최솟값을 return 하도록 solution 함수를 완성해주세요.
# 단, 상대 팀 진영에 도착할 수 없을 때는 -1을 return 해주세요.
# 제한사항
# maps는 n x m 크기의 게임 맵의 상태가 들어있는 2차원 배열로, n과 m은 각각 1 이상 100 이하의 자연수입니다.
# n과 m은 서로 같을 수도, 다를 수도 있지만, n과 m이 모두 1인 경우는 입력으로 주어지지 않습니다.
# maps는 0과 1로만 이루어져 있으며, 0은 벽이 있는 자리, 1은 벽이 없는 자리를 나타냅니다.
# 처음에 캐릭터는 게임 맵의 좌측 상단인 (1, 1) 위치에 있으며, 상대방 진영은 게임 맵의 우측 하단인 (n, m) 위치에 있습니다.
from collections import deque

def solution(maps):
    width = len(maps[0]) #열
    height = len(maps)   #행
    way = deque()  #방문한 곳과 총 방문횟수 저장할 데크
    depth = -1 #최소 방문횟수 저장할 변수
    way.append([0,0,1]) #시작지점
    position = [[1,0],[0,1],[-1,0],[0,-1]] # x,y 축 4분면 리스트
    visit = [[False]* width for _ in range(height)] #방문 여부 리스트
    visit[0][0]=True #시작지점 방문함으로 표시

    while(way): #남아있는 방문한 리스트가 있다면 계속 반복

        w= way.popleft() #FIFO 로 먼저 방문 한 곳부터 확인
        if w[0] == height -1 and w[1] == width -1: #방문 한 곳이 마지막 도착지점일 경우 방문횟수 depth 에 저장
            depth = w[2]

        for x,y in position: 
            if 0<= w[0]+x < height and 0<= w[1]+y < width: # 각 4분면 리스트를 현재 방문한 곳에서 이동했을 때 방문한 곳 내의 지점일 경우만 확인
                if maps[w[0]+x][w[1]+y] == 1 and visit[w[0]+x][w[1]+y] == False: #방문 할 곳이 방문 가능한 곳이며, 처음 방문했을 경우
                    way.append([w[0]+x,w[1]+y,w[2]+1]) #다음 방문지와 방문 횟수 1추가
                    visit[w[0]+x][w[1]+y] = True #다음 방문을 하니 방문함으로 표시

    answer = depth
    return answer


# maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
maps = [[1,0,0],[1,0,0],[1,0,0],[1,1,1],[0,0,1]]
result = solution(maps)

print("result = ", result)