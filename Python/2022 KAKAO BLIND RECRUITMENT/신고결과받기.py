
#example 1

# =============================================================================
# id_list = ["muzi", "frodo", "apeach", "neo"]
# report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
# k = 2
# =============================================================================


#example 2

# =============================================================================
# id_list = ["con", "ryan"]
# report = ["ryan con", "ryan con", "ryan con", "ryan con"]
# k = 3
# =============================================================================



def solution(id_list, report, k):

    # 중복된 신고 제거 및 각 신고자-신고유저 분리하여 리스트에 저장
    report_list = list(map(lambda x : x.split() ,list(set(report))))
    
    # 각 유저의 신고 당한 횟수를 저장하기 위한 딕셔너리 생성
    number_of_reported_cases = {x: 0 for x in id_list}
    
    # 각 유저가 신고한 유저 목록을 저장하기 위한 딕셔너리 생성
    user = {x:set() for x in id_list}
    
    # 유저가 신고 처리결과를 받야할 메일 건수
    result = []
    
    #신고 당한 유저 횟수 증가 및 신고한 유저 목록에 추가
    for x in report_list :
        number_of_reported_cases[x[1]] +=1    
        user[x[0]].add(x[1])
    
    
    #정지 기준 (k) 이상인 유저들은 이용 제한해야 한다.
    #따라서 신고자에게 메일보내야하므로 보낼 건수를 result 에 저장한다.
    for x in user :
       d = 0
       for index in user[x] :
           if number_of_reported_cases[index] >= k :
               d+=1
       result.append(d)
       
       
    return result



res = solution(id_list,report,k)

print('res = ', res)

