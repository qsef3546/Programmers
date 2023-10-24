# 다음 규칙을 지키는 문자열을 올바른 괄호 문자열이라고 정의합니다.
#
# (), [], {} 는 모두 올바른 괄호 문자열입니다.
# 만약 A가 올바른 괄호 문자열이라면, (A), [A], {A} 도 올바른 괄호 문자열입니다. 예를 들어, [] 가 올바른 괄호 문자열이므로, ([]) 도 올바른 괄호 문자열입니다.
# 만약 A, B가 올바른 괄호 문자열이라면, AB 도 올바른 괄호 문자열입니다. 예를 들어, {} 와 ([]) 가 올바른 괄호 문자열이므로, {}([]) 도 올바른 괄호 문자열입니다.
# 대괄호, 중괄호, 그리고 소괄호로 이루어진 문자열 s가 매개변수로 주어집니다.
# 이 s를 왼쪽으로 x (0 ≤ x < (s의 길이)) 칸만큼 회전시켰을 때 s가 올바른 괄호 문자열이 되게 하는 x의 개수를 return 하도록 solution 함수를 완성해주세요.
from collections import Counter
def solution(s):
    answer = 0
    dic = {'(': 0, '[': 0, '{': 0}   # 각 여는 괄호 개수를 저장하는 딕셔너리
    odic = {')': '(', ']': '[', '}': '{'}  #각 닫는 괄호가 나오면 맞는 열린 괄호가 이전에 사용됐는지 확인하기 위한 딕셔너리
    ds = Counter(s)
    if (ds['('] + ds[')']) % 2 == 1 or (ds['['] + ds[']']) % 2 == 1 or (ds['{'] + ds['}']) % 2 == 1: #각 괄호쌍이 홀수면 올바른 괄호가 될 수 없다.
        return 0
    for i in range(len(s)):
        if s[i] in odic.keys() or s[-1+i] in odic.values(): #첫 문자가 여는 괄호가 아니거나 마지막 문자가 닫히는 괄호가 아니면 올바른 괄호가 될 수 없다.
            continue
        for j in range(len(s)):
            w = s[(j + i) % len(s)] # i만큼 회전
            if w in odic.values(): # 여는 괄호
                dic[w] += 1
            else: #닫는 괄호
                if dic[odic[w]] < 1: #여는 괄호가 없다면 올바른 괄호가 아니다
                    break
                if s[(j + i - 1) % len(s)] not in list(odic.keys()) + [odic[w]]: #이전에 나온 괄호가 자기에 맞는 여는괄호 or 각 닫히는 괄호가 아니면 올바른 괄호가 될 수 없다.
                    break
                dic[odic[w]] -= 1 # 여는괄호 + 닫히는 괄고 쌍이 되었으므로 제거한다. 
        else:
            answer += 1
        for key in dic.keys(): # 다음 괄호 비교를 위하여 초기화
            dic[key] = 0
    return answer


s = "}]()[{"

answer = solution(s)
