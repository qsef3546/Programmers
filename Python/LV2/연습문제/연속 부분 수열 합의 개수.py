# 문제 설명
# 철호는 수열을 가지고 놀기 좋아합니다. 어느 날 철호는 어떤 자연수로 이루어진 원형 수열의 연속하는 부분 수열의 합으로 만들 수 있는 수가 모두 몇 가지인지 알아보고 싶어졌습니다.
# 원형 수열이란 일반적인 수열에서 처음과 끝이 연결된 형태의 수열을 말합니다. 예를 들어 수열 [7, 9, 1, 1, 4] 로 원형 수열을 만들면 다음과 같습니다.

# 원형 수열은 처음과 끝이 연결되어 끊기는 부분이 없기 때문에 연속하는 부분 수열도 일반적인 수열보다 많아집니다.
# 원형 수열의 모든 원소 elements가 순서대로 주어질 때, 원형 수열의 연속 부분 수열 합으로 만들 수 있는 수의 개수를 return 하도록 solution 함수를 완성해주세요.

def solution(elements):
    d = set(elements)
    for i in range(1,len(elements)-1): #전체 수열 합은 굳이 반복문을 돌려서 여러번 구할 필요 없다.
        c = elements + elements[:i] # n 개의 연속된 수열의 합을 구하기 위하여 list 뒤에 n개 만큼 추가
        d.update([sum(c[x:x+1+i]) for x in range(len(c)-i)]) # [x ~ x+i] 의 수열의 합 update
    else:
        d.add(sum(elements))
    return len(d)


elements = [7, 9, 1, 1, 4]
answer = solution(elements)
