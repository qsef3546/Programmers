
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

    report_list = list(map(lambda x : x.split() ,list(set(report))))
    number_of_reported_cases = {x: 0 for x in id_list}
    user = {x:set() for x in id_list}
    
    for x in report_list :
        number_of_reported_cases[x[1]] +=1    
        user[x[0]].add(x[1])
    result = []
    for x in user :
       d = 0
       for index in user[x] :
           if number_of_reported_cases[index] >= k :
               d+=1
       result.append(d)
       
    return result



res = solution(id_list,report,k)

print('res = ', res)

