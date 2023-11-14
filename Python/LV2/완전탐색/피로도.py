# 문제 설명
# XX게임에는 피로도 시스템(0 이상의 정수로 표현합니다)이 있으며, 일정 피로도를 사용해서 던전을 탐험할 수 있습니다. 이때, 각 던전마다 탐험을 시작하기 위해 필요한 "최소 필요 피로도"와 던전 탐험을 마쳤을 때 소모되는 "소모 피로도"가 있습니다.
# "최소 필요 피로도"는 해당 던전을 탐험하기 위해 가지고 있어야 하는 최소한의 피로도를 나타내며, "소모 피로도"는 던전을 탐험한 후 소모되는 피로도를 나타냅니다.
# 예를 들어 "최소 필요 피로도"가 80, "소모 피로도"가 20인 던전을 탐험하기 위해서는 유저의 현재 남은 피로도는 80 이상 이어야 하며, 던전을 탐험한 후에는 피로도 20이 소모됩니다.
#
# 이 게임에는 하루에 한 번씩 탐험할 수 있는 던전이 여러개 있는데, 한 유저가 오늘 이 던전들을 최대한 많이 탐험하려 합니다.
# 유저의 현재 피로도 k와 각 던전별 "최소 필요 피로도", "소모 피로도"가 담긴 2차원 배열 dungeons 가 매개변수로 주어질 때,
# 유저가 탐험할수 있는 최대 던전 수를 return 하도록 solution 함수를 완성해주세요.

# k : 현재 피로도
# l : 다음 이용할 던전 리스트
# w : 들어간 던전 수
def requr(k, l, w):
    m = []
    if len(l) == 0: #이용할 던전이 없다.
        return w
    for i in range(len(l)):
        if k >= l[i][0]: #현재 피로도가 다음 던전 최소 필요 피로도 이상일경우
            m.append(requr(k-l[i][1], l[i + 1:] + l[:i], w + 1)) #그 다음 던전 탐색
    return max(m) if m else w

def solution(k, dungeons):
    answer = requr(k, dungeons, 0)
    return answer

k = 80
dungeons = [[80, 20], [50, 40], [30, 10]]

answer = solution(k, dungeons)
