# 문제 설명
# JadenCase란 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열입니다.
# 단, 첫 문자가 알파벳이 아닐 때에는 이어지는 알파벳은 소문자로 쓰면 됩니다. (첫 번째 입출력 예 참고)
# 문자열 s가 주어졌을 때, s를 JadenCase로 바꾼 문자열을 리턴하는 함수, solution을 완성해주세요.

def solution(s):
    return ' '.join([x[0].upper() + x[1:].lower() if x != '' else '' for x in s.split(' ')])
    #문자열을 ' ' 기준으로 분리 후 문자일 경우 첫문자는 대문자 + 소문자 , 공백일 경우 공백으로 표시

s = '3people  unFollowed me'

answer = solution(s)

