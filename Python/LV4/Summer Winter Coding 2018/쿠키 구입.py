# 문제 설명
# 과자를 바구니 단위로 파는 가게가 있습니다. 이 가게는 1번부터 N번까지 차례로 번호가 붙은 바구니 N개가 일렬로 나열해 놨습니다.
#
# 철수는 두 아들에게 줄 과자를 사려합니다. 첫째 아들에게는 l번 바구니부터 m번 바구니까지, 둘째 아들에게는 m+1번 바구니부터 r번 바구니까지를 주려합니다.
# 단, 두 아들이 받을 과자 수는 같아야 합니다(1 <= l <= m, m+1 <= r <= N). 즉, A[i] 를 i번 바구니에 들어있는 과자 수라고 했을 때, A[l]+..+A[m] = A[m+1]+..+A[r] 를 만족해야 합니다.
# 각 바구니 안에 들은 과자 수가 차례로 들은 배열 cookie가 주어질 때, 조건에 맞게 과자를 살 경우 한 명의 아들에게 줄 수 있는 가장 많은 과자 수를 return 하는 solution 함수를 완성해주세요.
# (단, 조건에 맞게 과자를 구매할 수 없다면 0을 return 합니다)

def solution(cookie):
    answer = 0
    max_fruit = 0 #나누어 가질 수 있는 최대 과자 수
    length = len(cookie)
    for m in range(length-1):
        A = cookie[m]
        B = cookie[m+1]

        left = m # m위치에서 시작
        right = m+1 # m+1 위치에서 시작
        while True:
            if A == B: #과자 수가 같을 경우 max 값으로 저장
                max_fruit = max(max_fruit,A)
            if left > 0 and A < B: #첫 번째 위치보다 뒷단이면서 A가 B보다 과자 수가 작다면
                left -= 1 # 전 위치 (왼쪽) 으로 이동
                A += cookie[left] #이동한 위치의 쿠키 누적 저장
            elif right < length - 1 and A >= B: # 반대일 경우 B에 저장
                right += 1
                B += cookie[right]
            else: # 나눌 수 없는 상황
                break
    answer = max_fruit
    return answer


cookie = [1,1,2,3]
result = solution(cookie)
print("result = ",result)