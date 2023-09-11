# 연습문제
# 점심시간에 도둑이 들어, 일부 학생이 체육복을 도난당했습니다. 다행히 여벌 체육복이 있는 학생이 이들에게 체육복을 빌려주려 합니다.
# 학생들의 번호는 체격 순으로 매겨져 있어, 바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있습니다.
# 예를 들어, 4번 학생은 3번 학생이나 5번 학생에게만 체육복을 빌려줄 수 있습니다. 체육복이 없으면 수업을 들을 수 없기 때문에
# 체육복을 적절히 빌려 최대한 많은 학생이 체육수업을 들어야 합니다.
#
# 전체 학생의 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost,
# 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve가 매개변수로 주어질 때,
# 체육수업을 들을 수 있는 학생의 최댓값을 return 하도록 solution 함수를 작성해주세요.


def cal(stu,repeat,value) : #체육복을 잃어버린 사람, 여벌이 있는 사람 계산하는 함수
    for i in repeat :
        stu[i-1] = stu[i-1] + value
def solution(n, lost, reserve):
    if n < 2 or n > 30 : return

    student = [1]*n  #학생수가 다 체육복이 있다고 가정해서 대입
    cal(student,lost,-1) #없는 학생 체크
    cal(student,reserve,1) #여벌 있는 학생 체크

    for i in range(len(student)) :
        if student[i] >= 1 : continue #자기 입을 체육복만 있는 학생들은 비교할 필요가 없다.
        if student[i] != 0 and student[i-1] == 2 : #현재 학생이 없고 이전 번호 학생이 여벌 있는 학생일 경우
            student[i] = student[i] +1 #이전 학생에게 여벌 주기
            student[i-1] = student[i-1] -1
        elif i != len(student)-1 and student[i+1] == 2 : #마지막 학생이 아니면서 다음 학생이 여벌이 있을경우
            student[i] = student[i] +1 #여벌 주기
            student[i+1] = student[i+1] -1

    answer = len(list(filter(lambda x : x > 0,student))) #체육 들을 수 있는 학생 수

    return answer


n = 5
lost = [2,4]
reserve = [1,3,5]

solution(n, lost, reserve)