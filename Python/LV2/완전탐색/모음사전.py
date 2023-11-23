# 문제 설명
# 사전에 알파벳 모음 'A', 'E', 'I', 'O', 'U'만을 사용하여 만들 수 있는, 길이 5 이하의 모든 단어가 수록되어 있습니다.
# 사전에서 첫 번째 단어는 "A"이고, 그다음은 "AA"이며, 마지막 단어는 "UUUUU"입니다.
#
# 단어 하나 word가 매개변수로 주어질 때, 이 단어가 사전에서 몇 번째 단어인지 return 하도록 solution 함수를 완성해주세요.
#
# 제한사항
# word의 길이는 1 이상 5 이하입니다.
# word는 알파벳 대문자 'A', 'E', 'I', 'O', 'U'로만 이루어져 있습니다.
from functools import reduce

def solution(word):
    idx ={'A': 1, 'E': 2, 'I': 3, 'O': 4, 'U': 5} #사전에 사용되는 글자
    nD = [len(idx)] #한 글자인 경우의 수 초기 대입
    for x in range(1, len(idx)):
        nD.append(nD[x-1] + pow(5, x + 1)) # 1~2글자 , 1~3글자... , 1~5글자까지 사용되는 글자 합
    nD = list(map(lambda x: x//5, nD)) #첫 알파벳 고정으로 1~2글자 ,,, 1~5글자까지 사용되는 글자 합
    return reduce(lambda x, y: x + (nD[-1 - y] * (idx[word[y]] - 1) + 1), range(len(word)), 0) #각 자리 알파벳 까지의 번호 누적 합



word = "EIO"

answer = solution(word)

print('answer = ', answer)