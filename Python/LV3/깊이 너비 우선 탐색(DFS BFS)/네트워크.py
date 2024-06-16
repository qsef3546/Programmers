# 문제 설명
# 네트워크란 컴퓨터 상호 간에 정보를 교환할 수 있도록 연결된 형태를 의미합니다. 예를 들어, 컴퓨터 A와 컴퓨터 B가 직접적으로 연결되어있고,
# 컴퓨터 B와 컴퓨터 C가 직접적으로 연결되어 있을 때 컴퓨터 A와 컴퓨터 C도 간접적으로 연결되어 정보를 교환할 수 있습니다.
# 따라서 컴퓨터 A, B, C는 모두 같은 네트워크 상에 있다고 할 수 있습니다.
#
# 컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers가 매개변수로 주어질 때, 네트워크의 개수를 return 하도록 solution 함수를 작성하시오.
#
# 제한사항
# 컴퓨터의 개수 n은 1 이상 200 이하인 자연수입니다.
# 각 컴퓨터는 0부터 n-1인 정수로 표현합니다.
# i번 컴퓨터와 j번 컴퓨터가 연결되어 있으면 computers[i][j]를 1로 표현합니다.
# computer[i][i]는 항상 1입니다.

def solution(n, computers):
    answer = 0
    visit = [False] * n #각 네트워크 연결 여부

    for i in range(n):
        if not visit[i]:  #0번 네트워크 부터 방문 한 곳인지 확인
            stack = [i] # 방문 안했을 경우 stack 네트워크 번호 넣기
            while stack: #방문 할 곳이 없을 때까지 반복
                node = stack.pop()
                for compi, comp in enumerate(computers[node]): # 연결된 곳의 네트워크 리스트 추출
                    if comp and visit[compi] == False: # 어떤 네트워크와 연결 돼있고 방문한 적이 없을 경우
                        visit[compi] = True #방문 했다고 표시
                        stack.append(compi) #방문 한 곳에서 또 다른 네트워크가 연결돼있는지 확인하기 위하여 스택에 추가
            answer += 1 # i번 네트워크 클라우드 개수 추가


    return answer



# computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
# computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
computers = [[1,1,1,0,1],[1,1,1,0,0],[1,1,1,1,1],[0,0,1,1,1],[1,0,1,1,1]]
n = len(computers)
result = solution(n, computers)
print("result = ", result)
