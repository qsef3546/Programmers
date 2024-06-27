# 문제 설명
# 앞뒤를 뒤집어도 똑같은 문자열을 팰린드롬(palindrome)이라고 합니다.
# 문자열 s가 주어질 때, s의 부분문자열(Substring)중 가장 긴 팰린드롬의 길이를 return 하는 solution 함수를 완성해 주세요.
#
# 예를들면, 문자열 s가 "abcdcba"이면 7을 return하고 "abacde"이면 3을 return합니다.
#
# 제한사항
# 문자열 s의 길이 : 2,500 이하의 자연수
# 문자열 s는 알파벳 소문자로만 구성
def solution(s):
    answer = 1
    #홀수
    #[1,2,3,4,5] 일 때,
    #가운데 기준은 2,3,4 밖에 할 수가 없기에, 각 가운데 기준으로 start = -1 end = +1 해서 같은 문자인지 확인한다.
    #ex: 가운데 기준이 2일 경우 start = 1 , end = 3 에서 시작
    for i in range(0,len(s)-2):
        start = i
        count = 0
        for j in range(i+2,len(s)):
            if s[start] == s[j]:
                count += 2
            if start == 0 or s[start] != s[j]: #start 위치가 첫번 째 위치거나 각 위치의 문자가 같지 않으면 break
                break
            start -= 1 # end 는 j for 문으로 +1씩 되고 있으므로 start는 따로 -1 해줘야함
        answer = max(answer, count+1) #현재까지 같은 문자 개수 + 가운데 문자 개수를 합하여 현재 저장된 개수보다 큰지 확인

    #짝수
    #[1,2,3,4,5] 일 때,
    # [start,end] = [1,2],[2,3],[3,4],[4,5] 순을 기준으로 확인한다.

    for i in range(0, len(s) - 1):
        start = i
        count = 0
        for j in range(i + 1, len(s)):
            if s[start] == s[j]:
                count += 2
            if start == 0 or s[start] != s[j]:
                break
            start -= 1
        answer = max(answer, count) #현재까지 같은 문자 개수를 합하여 현재 저장된 개수보다 큰지 확인
    return answer


s = "abacde"
# s = "abcdcba"
# s = 'abcddcbadddsbcacbs'
# s = 'babcbab'
# s = 'abbb'
result = solution(s)
print("result = ",result)