# 문제 설명
# 2차원 행렬 arr1과 arr2를 입력받아, arr1에 arr2를 곱한 결과를 반환하는 함수, solution을 완성해주세요.
import numpy as np
def solution(arr1, arr2):
    return (np.array(arr1)@np.array(arr2)).tolist() #ndarray to list 변환하여 리턴


arr1 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
arr2 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]

answer = solution(arr1, arr2)


