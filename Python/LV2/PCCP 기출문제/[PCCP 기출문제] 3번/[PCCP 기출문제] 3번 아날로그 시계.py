# 문제 설명
# 시침, 분침, 초침이 있는 아날로그시계가 있습니다. 시계의 시침은 12시간마다, 분침은 60분마다, 초침은 60초마다 시계를 한 바퀴 돕니다.
# 따라서 시침, 분침, 초침이 움직이는 속도는 일정하며 각각 다릅니다.
# 이 시계에는 초침이 시침/분침과 겹칠 때마다 알람이 울리는 기능이 있습니다.
# 당신은 특정 시간 동안 알람이 울린 횟수를 알고 싶습니다.

import sympy as sp
def solution(h1, m1, s1, h2, m2, s2):
    answer = 0
    H = 12
    M = 5
    S = sp.Symbol('S', real=True)
    theta_h = 0.5 * (60 * H + M + S / 60)
    theta_s = 6 * S
    eq1 = sp.Eq(theta_h, theta_s)
    solution_hs = sp.solve(eq1, S)

    # 분침과 초침이 같아지는 시간 계산
    M = 5
    theta_m = 6 * M + 0.1 * S
    eq2 = sp.Eq(theta_m, theta_s)
    solution_ms = sp.solve(eq2, S)

    # 유효 시간 범위 내의 해만 필터링
    valid_hs = [s.evalf() for s in solution_hs if 30 <= s.evalf() <= 60]
    valid_ms = [s.evalf() for s in solution_ms if 30 <= s.evalf() <= 60]

    print(valid_hs, valid_ms)
    # hour = 5 / 3600
    # minute = 1 / 60
    # start = h1 * 3600 + m1 * 60 + s1
    # end = h2 * 3600 + m2 * 60 + s2
    #
    # while start <= end:
    #     # print('start = ', start%60 if start % 60 > 0 else 60)
    #     # print('hour = ', start*hour)
    #     # print('minute = ', start%3600*minute)
    #
    #
    #     # if start%60 <= start*hour%60 <= ((start + 1)%60 if (start + 1) % 60 > 0 else 60):
    #     if start % 60 == start * hour % 60:
    #         print('hour')
    #         print('hour ', start % 60, ' <= ', start * hour % 60, ' <= ', (start + 1) % 60 if (start + 1) % 60 > 0 else 60)
    #         answer +=1
    #     if start%60 == start%3600*minute:
    #         print('minute')
    #         print('minute = ', start % 60, ' <= ', start % 3600 * minute, ' <= ',(start + 1) % 60 if (start + 1) % 60 > 0 else 60)
    #         answer += 1
    #     if start*hour%60 == start%3600*minute:
    #         answer -=1
    #     start += 1
    return answer

h1 = 0
m1 = 5
s1 = 30
h2 = 0
m2 = 7
s2 = 0
# h1 = 11
# m1 = 59
# s1 = 30
# h2 = 12
# m2 = 0
# s2 = 0
result = solution(h1, m1, s1, h2, m2, s2)
print("result = ", result)
