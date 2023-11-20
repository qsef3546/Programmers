# 문제 설명
# 전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
# 전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.
#
# 구조대 : 119
# 박준영 : 97 674 223
# 지영석 : 11 9552 4421
# 전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때,
# 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.

from collections import Counter
def solution(phone_book):
    pbs = Counter(phone_book) #번호 딕셔너리화
    pk = pbs.keys()
    for pb in pk:
        temp = ''
        for jd in pb: #각 번호 첫 글자부터 접두어인지 확인
            temp += jd
            print(temp)
            if pbs[temp] == 1 and temp != pb:
                return False
    return True


#phone_book = ["119", "97674223", "1195524421"]
phone_book = ["1195524421", "119", "97674223"]

answer = solution(phone_book)