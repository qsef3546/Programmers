# 문제 설명
# 매운 것을 좋아하는 Leo는 모든 음식의 스코빌 지수를 K 이상으로 만들고 싶습니다.
# 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 Leo는 스코빌 지수가 가장 낮은 두 개의 음식을 아래와 같이 특별한 방법으로 섞어 새로운 음식을 만듭니다.
#
# 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
# Leo는 모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복하여 섞습니다.
# Leo가 가진 음식의 스코빌 지수를 담은 배열 scoville과 원하는 스코빌 지수 K가 주어질 때,
# 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수를 return 하도록 solution 함수를 작성해주세요.
import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)  # 리스트 -> 최소힙구조로 변환
    while scoville[0] < K and len(scoville) >=2: #부모노드 (제일 작은 값) 이 K 이상이거나 스코빌 지수 리스트가 2개 미만이 될 때까지 반복
        heapq.heappush(scoville, heapq.heappop(scoville) + heapq.heappop(scoville)*2) # 제일 작은 스코빌 지수 + 그 다음 작은 스코빌 지수 * 2
        answer += 1 # 섞은 음식 스코빌 지수 증가
    if len(scoville) < 2 and scoville[0] < K: #남은 스코빌 지수가 1개면서 아무리 섞어도 K 이상을 만들 수 없다면 -1
        answer = -1
    return answer

scoville = [1, 2, 3, 9, 10, 12]
k = 7

result = solution(scoville, k)
print("result = ", result)