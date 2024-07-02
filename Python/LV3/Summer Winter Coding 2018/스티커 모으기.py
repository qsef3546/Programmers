# 문제 설명
# N개의 스티커가 원형으로 연결되어 있습니다. 다음 그림은 N = 8인 경우의 예시입니다.
# 스티커_hb1jty.jpg
# 원형으로 연결된 스티커에서 몇 장의 스티커를 뜯어내어 뜯어낸 스티커에 적힌 숫자의 합이 최대가 되도록 하고 싶습니다.
# 단 스티커 한 장을 뜯어내면 양쪽으로 인접해있는 스티커는 찢어져서 사용할 수 없게 됩니다.
#
# 예를 들어 위 그림에서 14가 적힌 스티커를 뜯으면 인접해있는 10, 6이 적힌 스티커는 사용할 수 없습니다.
# 스티커에 적힌 숫자가 배열 형태로 주어질 때, 스티커를 뜯어내어 얻을 수 있는 숫자의 합의 최댓값을 return 하는 solution 함수를 완성해 주세요.
# 원형의 스티커 모양을 위해 배열의 첫 번째 원소와 마지막 원소가 서로 연결되어 있다고 간주합니다.
def max_score(nums):

    incl = nums[0] #첫번 째 원소 저장
    excl = 0 #현재 까지 최대합 저장할 변수

    for num in nums[1:]: #다음 원소 부터 
        new_excl = max(excl, incl) #전 최대합과 현재 최대합 중 max 값 저장
        incl = excl + num #전 최대합에 현재 원소 추가하여 현재 최대합을 가진 변수에 저장
        excl = new_excl #비교한 max 값 저장

    return max(incl, excl) #현재 최대합과 전 최대합 max 값


def solution(sticker):
    answer = 0
    if len(sticker) == 1:
        return sticker[0]

    # 첫 번째 요소를 포함하지 않는 부분 배열의 최대 합
    first = max_score(sticker[1:])

    # 마지막 요소를 포함하지 않는 부분 배열의 최대 합
    last = max_score(sticker[:-1])

    answer = max(first, last)
    return answer


sticker = [14, 6, 5, 11, 3, 9, 2, 10]
# sticker = [1,3,2,5,4]
# sticker = [1, 2, 3, 4, 5]
result = solution(sticker)
print("result = ", result)
