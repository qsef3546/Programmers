# 5.숫자 만들기
# 해당 문제는 main 부터 입/출력, 알고리즘 풀이를 모두 작성하는 문제입니다.
# 숫자(정수) A를 B로 바꿔야 한다.
# 사용 가능한 연산은 다음과 같은 두 가지이다.
# 2를 곱한다.
# 1 을 수의 가장 오른쪽에 추가한다.
# A를 B로 바꾸는데 필요한 연산의 최솟값을 구해보자.
# 예시)
# 2 162
# 2 → 4 → 8 → 81 → 162
# 입력
# 첫째 줄에 A, B (1 ≤ A < B ≤ 109)가 주어진다.
# 출력
# A를 B로 바꾸는데 필요한 연산의 최솟값에 1을 더한 값을 출력한다. 만들 수 없는 경우에는 -1을 출력한다.

def req(a, b, c):
    r = []
    if a > b:
        return -1
    elif a == b:
        return c
    else:
        r.append(req(a * 10 + 1, b, c + 1))
        r.append(req(a * 2, b, c + 1))
    res = list(filter(lambda x: x > 0, r))
    return min(res) if res else -1


def solution(a, b):
    return req(a, b, 0)


A = 2
B = 82

answer = solution(A, B)
print('answer = ', answer)
