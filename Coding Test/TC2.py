# 2.solution 함수에 parameter가 자동으로 넘어옵니다.
# solution 함수만 작성하시면 됩니다. (추가 함수 정의 가능)
# 종량제 봉투 가장 적게 사용하기
# 철수네 회사에 있는 쓰레기를 모두 공터에 모았더니 X 리터의 쓰레기 더미가 생겼습니다.
# 철수는 종량제 봉투를 사러 마트에 갔습니다. 마트에서 파는 종량제 봉투는 총 두 종류로, 각각 Y 리터와 Z 리터의 쓰레기를 담을 수 있으며, 가격은 모두 1000원 입니다.
# 가장 적은 돈으로 쓰레기를 버리려면 총 얼마가 필요한지 반환해 주세요.
# 단 쓰레기 봉투는 다 채워야 합니다. 만약 쓰레기 봉투를 모두 채울 수 없다면 -1을
# 반환해 주세요.
# 입력
# - trash: 쓰레기 더미의 총 량 X , 1 <=trash <=100000
# - bagY: 한 종량제 봉투의 용량, 1<=bagY<=1000000
# - bagZ: 다른 종량제 봉투의 용량, 1<=bagZ<=1000000
# 출력
# 필요한 봉투의 가격  , 모두 채울 수 없으면 -1
# 예시
# 120, 50, 20
# 50리터 봉투 2개, 20리터 봉투 1개 총 3000 원

def solution(trash, bagY, bagZ):

    res = []
    for i in [x for x in range(trash//bagY+1)]:
        if (trash - bagY*i) % bagZ == 0:
            res.append((trash - bagY * i)//bagZ + i)
    return min(res)*1000 if res else -1


trash = 150
bagY = 40
bagZ = 30

answer = solution(trash, bagY, bagZ)
print('answer = ', answer)