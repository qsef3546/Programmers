enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]


def solution(enroll, referral, seller, amount):
    
    #다단계 조직 트리 구조 생성
    tree = {enroll[x] : 'center' if referral[x] == '-' else referral[x] for x in range(0,len(referral))}

    #각 조직원 이익 저장 딕셔너리
    benefit = {x : 0 for x in enroll}

    #이익 배분
    for x in range(0,len(seller)) :
        # x 번째 이익 배분자    
        distribution = seller[x]
        # x 번째 조직원의 이익
        profit = amount[x] * 100

        while True :
            #추천인 10% 이익 저장
            tenper = int(profit * 0.1)
            #x 번째 조직원 이익 = 추천인 10% 이익 제외한 나머지 금액
            benefit[distribution] +=  profit - tenper 

            # 10% 이익이 0원일 경우 이익 분배를 할 수 없다.
            if tenper == 0 :
                break
            profit = tenper
            # 현재 조직원의 추천인이 center 면 최상위 조직원이므로 이익 배분 끝
            if tree[distribution] == 'center' :
                break
            # 현재 조직원의 추천인으로 변경
            distribution = tree[distribution]
            

    # 조직원의 이익 리스트 저장
    answer = [x for x in benefit.values()]
    return answer


# =============================================================================
# {enroll[x] : 'center'}
# =============================================================================
solution(enroll, referral, seller, amount)