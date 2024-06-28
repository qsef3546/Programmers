# 문제 설명
# N개의 아파트가 일렬로 쭉 늘어서 있습니다. 이 중에서 일부 아파트 옥상에는 4g 기지국이 설치되어 있습니다. 기술이 발전해 5g 수요가 높아져 4g 기지국을 5g 기지국으로 바꾸려 합니다.
# 그런데 5g 기지국은 4g 기지국보다 전달 범위가 좁아, 4g 기지국을 5g 기지국으로 바꾸면 어떤 아파트에는 전파가 도달하지 않습니다.
# 예를 들어 11개의 아파트가 쭉 늘어서 있고, [4, 11] 번째 아파트 옥상에는 4g 기지국이 설치되어 있습니다.
# 만약 이 4g 기지국이 전파 도달 거리가 1인 5g 기지국으로 바뀔 경우 모든 아파트에 전파를 전달할 수 없습니다.
# (전파의 도달 거리가 W일 땐, 기지국이 설치된 아파트를 기준으로 전파를 양쪽으로 W만큼 전달할 수 있습니다.)
# 이때, 우리는 5g 기지국을 최소로 설치하면서 모든 아파트에 전파를 전달하려고 합니다. 위의 예시에선 최소 3개의 아파트 옥상에 기지국을 설치해야 모든 아파트에 전파를 전달할 수 있습니다.
# 아파트의 개수 N, 현재 기지국이 설치된 아파트의 번호가 담긴 1차원 배열 stations, 전파의 도달 거리 W가 매개변수로 주어질 때,
# 모든 아파트에 전파를 전달하기 위해 증설해야 할 기지국 개수의 최솟값을 리턴하는 solution 함수를 완성해주세요
import math
def solution(n, stations, w):
    answer = 0 
    way = 0 #현재 기지국 설치된 위치
    for s in stations:
        need = s-w-way-1  #s 기지국의 범위 앞쪽에서 현재 기지국 설치된 위치 마지막 범위 위치 사이에 아파트가 있는지 확인 (있다면 전파가 안되는 아파트)
        if need > 0:
            answer += math.ceil(need/(w*2+1)) #아파트 수를 보며 필요한 기지국 수를 추가
        way = s+w
    if way < n:
        answer += math.ceil((n-way)/(w*2+1)) #마지막 기지국이 아파트 끝까지 전파를 보내지 못할 경우

    return answer

n = 11
stations = [4,11]
w = 1

# n = 16
# stations = [9]
# w = 2

result = solution(n, stations, w)
print("result = ",result)