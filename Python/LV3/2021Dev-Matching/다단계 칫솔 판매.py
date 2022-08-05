enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]


def solution(enroll, referral, seller, amount):
    answer = []

    tree = {enroll[x] : 'center' if referral[x] == '-' else referral[x] for x in range(0,len(referral))}
    benefit = {x : 0 for x in enroll}

    for x in range(0,len(seller)) :
        distribution = seller[x]
        profit = amount[x] * 100

        while True :
            
            tenper = int(profit * 0.1)
            benefit[distribution] +=  profit - tenper 
            profit = tenper
            if tree[distribution] == 'center' :
                break
            distribution = tree[distribution]
            


    
    return answer


# =============================================================================
# {enroll[x] : 'center'}
# =============================================================================
solution(enroll, referral, seller, amount)