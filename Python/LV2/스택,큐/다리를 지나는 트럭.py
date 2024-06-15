# 문제 설명
# 트럭 여러 대가 강을 가로지르는 일차선 다리를 정해진 순으로 건너려 합니다. 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 알아내야 합니다.
# 다리에는 트럭이 최대 bridge_length대 올라갈 수 있으며, 다리는 weight 이하까지의 무게를 견딜 수 있습니다. 단, 다리에 완전히 오르지 않은 트럭의 무게는 무시합니다.
#
# 예를 들어, 트럭 2대가 올라갈 수 있고 무게를 10kg까지 견디는 다리가 있습니다. 무게가 [7, 4, 5, 6]kg인 트럭이 순서대로 최단 시간 안에 다리를 건너려면
# 다음과 같이 건너야 합니다.
#
# 경과 시간	다리를 지난 트럭	다리를 건너는 트럭	대기 트럭
# 0	[]	[]	[7,4,5,6]
# 1~2	[]	[7]	[4,5,6]
# 3	[7]	[4]	[5,6]
# 4	[7]	[4,5]	[6]
# 5	[7,4]	[5]	[6]
# 6~7	[7,4,5]	[6]	[]
# 8	[7,4,5,6]	[]	[]
# 따라서, 모든 트럭이 다리를 지나려면 최소 8초가 걸립니다.
#
# solution 함수의 매개변수로 다리에 올라갈 수 있는 트럭 수 bridge_length, 다리가 견딜 수 있는 무게 weight, 트럭 별 무게 truck_weights가 주어집니다.
# 이때 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 return 하도록 solution 함수를 완성하세요.
from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    tb = deque() #다리 이동칸에 트럭을 배치할 데크
    tb_sum = 0 #총 다리에 있는 트럭 무게 총합
    truck_weights = deque(truck_weights) #트럭 데크로 변경
    t = 0 #이동 시간
    while truck_weights: #남아 있는 트럭이 없을 때까지 반복

        if len(tb) == bridge_length: #다리에 올라갈 수 있는 트럭이 꽉 찼을경우
            tb_sum -= tb.popleft() #먼저 올라온 차량 통과 및 나간 차량 무게 빼기
        if tb_sum+truck_weights[0] <= weight: #다음 올라올 차량이 현재 견딜 수 있는 다리 무게이하인 경우에만 다리에 올리기
            tb.append(truck_weights.popleft())
            tb_sum += tb[-1] #다리에 올라온 차량 무게 더하기
        else:
            tb.append(0) #자릿수 맞추기 위하여 0으로 추가
        t += 1 # 1초 증가
    t += bridge_length #마지막엔 굳이 반복할 필요가 없기에 다리에서 빠져나왔을 때 걸린 시간 추가
    answer = t
    return answer


bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]

result = solution(bridge_length, weight, truck_weights)
print("result = ", result)