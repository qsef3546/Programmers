# 문제 설명
# 두 개의 단어 begin, target과 단어의 집합 words가 있습니다. 아래와 같은 규칙을 이용하여 begin에서 target으로 변환하는 가장 짧은 변환 과정을 찾으려고 합니다.
#
# 1. 한 번에 한 개의 알파벳만 바꿀 수 있습니다.
# 2. words에 있는 단어로만 변환할 수 있습니다.
# 예를 들어 begin이 "hit", target가 "cog", words가 ["hot","dot","dog","lot","log","cog"]라면 "hit" -> "hot" -> "dot" -> "dog" -> "cog"와 같이 4단계를 거쳐 변환할 수 있습니다.
#
# 두 개의 단어 begin, target과 단어의 집합 words가 매개변수로 주어질 때, 최소 몇 단계의 과정을 거쳐 begin을 target으로 변환할 수 있는지 return 하도록 solution 함수를 작성해주세요.
from collections import Counter
def solution(begin, target, words):
    answer = 0
    if target not in words: #변경할 문자열이 words 안에 무조건 있어야 변경 가능하다
        return 0

    w = Counter(words) #변경된 문자열이 있는지 확인
    stack = [begin]
    idx = 0
    while stack and stack[-1] != target: #stack안에 문자열이 있거나 마지막 문자열이 변경하려는 문자열과 같지 않을 때까지 반복
        st = stack.pop() #현재 위치의 문자열 가져오기
        c = [] #words 안에 있는 문자열로 변경할 수 있는 문자열을 저장할 스택
        for i in range(len(words)):
            if st != words[i] and st[idx] != words[i][idx]: #현재 위치 문자열, idx위치의 문자가 비교할 문자열, idx위치의 문자가 같은지 확인
                conv = st[:idx]+words[i][idx]+st[idx+1:] #같다면 바꾼 문자열 conv에 저장
                if w[conv] == 1: # 바꾼 문자열이 words에 있는지 확인
                    c.append(conv) #있다면 c에 추가
                    if conv == target: #그 문자가 바꿀 문자열과 같다면 break
                        break
        if c : #변경할 수 있는 문자열이 있을 때
            stack += c # stack 에 추가
            answer +=1 #변경한 횟수 증가
        if not stack: #아무것도 없을경우 처음 문자열 추가
            stack.append(begin)
        idx = (idx + 1) % len(words[0]) # 0 번째 부터 문자열 길이까지 계속 반복해서 돌아야 한다.

    return answer



begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]

result = solution(begin, target, words)
print("result = ",result)