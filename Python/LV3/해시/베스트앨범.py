# 문제 설명
# 스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다. 노래는 고유 번호로 구분하며, 노래를 수록하는 기준은 다음과 같습니다.
#
# 속한 노래가 많이 재생된 장르를 먼저 수록합니다.
# 장르 내에서 많이 재생된 노래를 먼저 수록합니다.
# 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
# 노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때,
# 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.
from collections import defaultdict
def solution(genres, plays):
    answer = []
    total_gp= defaultdict(int)  #각 장르별 총 재생 횟수를 저장하기 위한 딕셔너리
    gp = defaultdict(list) #각 장르별 고유번호,재생 횟수를 저장하기 위한 딕셔너리
    for n,g,p in zip(range(len(genres)),genres,plays): #고유번호,장르,재생횟수 반복
        total_gp[g] += p #각 장르 재생횟수 누적 저장
        gp[g].append([p,n]) #각 장르별 [고유번호,재생횟수] 저장

    total_gp = dict(sorted(total_gp.items(),key=lambda x:x[1],reverse=True)) # 총 재생 횟수 기준으로 정렬

    for g in gp: #각 장르별 재생횟수로 내림 차순 및 고유번호로 오름차순
        gp[g].sort(key=lambda x:(-x[0],x[1]))

    for g in total_gp: #속한 노래가 많이 재생된 장르 부터 각 장르 내 많이 재생된 노래 2곡 추출
        for gg in gp[g][:2]:
            answer.append(gg[1])

    return answer



genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
# genres = ["a","b","c","b","c","a","b","c"]
# plays =  [100,200,300,200,250,100,400,300]


result = solution(genres, plays)
print("result = ", result)