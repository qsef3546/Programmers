# 문제 설명
# 초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때,
# 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.


def solution(price):
    answer = []
    price.reverse()

    while (price):
        ele = price.pop()
        for idx in range(0, len(price)):
            if price[-1 - idx] < ele: #현재 시점에 있는 주식가격이 idx초 후에 떨어지는지 확인
                answer.append(idx + 1) #떨어진 시점 answer 저장
                break
        else:
            answer.append(len(price))

    return answer


price = [1, 2, 3, 2, 3]

answer = solution(price)