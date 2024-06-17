# 계속되는 폭우로 일부 지역이 물에 잠겼습니다. 물에 잠기지 않은 지역을 통해 학교를 가려고 합니다. 집에서 학교까지 가는 길은 m x n 크기의 격자모양으로 나타낼 수 있습니다
# 가장 왼쪽 위, 즉 집이 있는 곳의 좌표는 (1, 1)로 나타내고 가장 오른쪽 아래, 즉 학교가 있는 곳의 좌표는 (m, n)으로 나타냅니다.
#격자의 크기 m, n과 물이 잠긴 지역의 좌표를 담은 2차원 배열 puddles이 매개변수로 주어집니다.
# 오른쪽과 아래쪽으로만 움직여 집에서 학교까지 갈 수 있는 최단경로의 개수를 1,000,000,007로 나눈 나머지를 return 하도록 solution 함수를 작성해주세요.

def solution(m, n, puddles):
    school = [[1] * m for _ in range(n)] #칸마다 최단거리 저장할 2차원 리스트
    for x, y in puddles: #물 웅덩이 처리하기 위한 반복문
        if x == 1:  #좌표가 최상위 좌표라면 포함한 좌표 다음 부터는 갈 수가 없기에 0으로 처리
            for yy in range(y-1,n):  # (2,1)가 물 웅덩이 -> (3,1),(4,1), ... ,(n-1,1) 까지 갈 수없다
                school[yy][x-1] = 0
        elif y == 1:  #(1,2)가 물 웅덩이 -> (1,3),(1,4),(1,5), ... , (1,m-1) 까지 갈 수 없다.
            for xx in range(x - 1, m):
                school[y-1][xx] = 0
        else: #해당 물웅덩이만 0으로 처리
            school[y-1][x-1] = 0
    for y in range(1, n):
        for x in range(1, m):
            if school[y][x] != 0:
                school[y][x] = school[y - 1][x] + school[y][x - 1] # 최단거리 공식 (x,y) => (x-1,y) + (x,y-1)

    answer = school[-1][-1] % 1000000007
    return answer
#
#
# m = 4
# n = 3
# puddles = [[2,2]]
m = 2
n = 3
puddles = [[1,2]]


result = solution(m, n, puddles)
print("result = ", result)