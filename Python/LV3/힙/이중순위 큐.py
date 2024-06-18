# 이중 우선순위 큐는 다음 연산을 할 수 있는 자료구조를 말합니다.
#
# 명령어	수신 탑(높이)
# I 숫자	큐에 주어진 숫자를 삽입합니다.
# D 1	큐에서 최댓값을 삭제합니다.
# D -1	큐에서 최솟값을 삭제합니다.
# 이중 우선순위 큐가 할 연산 operations가 매개변수로 주어질 때, 모든 연산을 처리한 후 큐가 비어있으면 [0,0]
# 비어있지 않으면 [최댓값, 최솟값]을 return 하도록 solution 함수를 구현해주세요.

import heapq
def solution(operations):
    answer = []
    minheap = []  #최소힙
    maxheap = []  #최대힙

    for op in operations:
        c,v = op.split()
        if c == 'I': #값 추가
            heapq.heappush(minheap,int(v))
            heapq.heappush(maxheap, -int(v)) #최대힙은 최소힙에 들어갈 값들을 음수로 치환하면 최대힙으로 사용가능하다
        elif c == 'D': #값 삭제
            if v == '1': #최대값 삭제
                if maxheap: 
                    heapq.heappop(maxheap) 
            else: #최소값 삭제
                if minheap:
                    heapq.heappop(minheap)

    maxheap = list(map(lambda x: -x,maxheap)) #음수로 치환한 값을 양수로 변환
    inter = set(minheap).intersection(maxheap) #최소힙과 최대힙의 교집합은 삭제 연산 하지 않은 값

    answer = [max(inter),min(inter)] if inter and len(maxheap) > 1 else [0,0] #min 또는 max heap이 1개 이하라면 모두 삭제되었다는 것

    return answer

# operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
operations = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
result = solution(operations)
print("result = ", result)