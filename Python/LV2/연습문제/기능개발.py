# 문제설명
# 프로그래머스 팀에서는 기능 개선 작업을 수행 중입니다. 각 기능은 진도가 100%일 때 서비스에 반영할 수 있습니다.
#
# 또, 각 기능의 개발속도는 모두 다르기 때문에 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있고, 이때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포됩니다.
#
# 먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와 각 작업의 개발 속도가 적힌 정수 배열 speeds가 주어질 때
# 각 배포마다 몇 개의 기능이 배포되는지를 return 하도록 solution 함수를 완성하세요.


import numpy as np
import math


def solution(progresses, speeds):
    answer = []
    pro = np.array([math.ceil((100 - progresses[i]) / speeds[i]) for i in
                    range(0, len(progresses))])  # 각 배포되는 시간(남은 작업 진도 / 작업 개수 (소수점 있으면 올림)) array 생성
    idx = 0
    while idx < len(pro): # 남은 작업 개수만큼 반복
        index = 0
        pro -= min(pro[np.where(pro > 0)]) #각 배포되는 시간에서 배포되는 시간이 제일 짧은 날만큼 차감
        if pro[idx] == 0:  #먼저 배포되어야하는 기능이개발이 배포 준비가 되었을 경우
            while pro[idx] <= 0: #배포 시간이 남은 순서까지 배포 가능한 기능 개수 구하기.
                index += 1
                idx += 1
                if idx >= len(pro): break
            answer.append(index) # 배포 가능한 기능 수 append
    return answer


progresses = [93, 30, 55]
speeds = [1, 30, 5]

answer = solution(progresses, speeds)