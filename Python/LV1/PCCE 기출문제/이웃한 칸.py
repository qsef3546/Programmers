# 문제 설명
# 각 칸마다 색이 칠해진 2차원 격자 보드판이 있습니다. 그중 한 칸을 골랐을 때, 위, 아래, 왼쪽, 오른쪽 칸 중 같은 색깔로 칠해진 칸의 개수를 구하려고 합니다.

# 보드의 각 칸에 칠해진 색깔 이름이 담긴 이차원 문자열 리스트 board와 고른 칸의 위치를 나타내는 두 정수 h, w가 주어질 때
# board[h][w]와 이웃한 칸들 중 같은 색으로 칠해져 있는 칸의 개수를 return 하도록 solution 함수를 완성해 주세요.

# 이웃한 칸들 중 몇 개의 칸이 같은 색으로 색칠되어 있는지 확인하는 과정은 다음과 같습니다.

"""
1. 정수를 저장할 변수 n을 만들고 board의 길이를 저장합니다.
2. 같은 색으로 색칠된 칸의 개수를 저장할 변수 count를 만들고 0을 저장합니다.
3. h와 w의 변화량을 저장할 정수 리스트 dh, dw를 만들고 각각 [0, 1, -1, 0], [1, 0, 0, -1]을 저장합니다.
4. 반복문을 이용해 i 값을 0부터 3까지 1 씩 증가시키며 아래 작업을 반복합니다.
    4-1. 체크할 칸의 h, w 좌표를 나타내는 변수 h_check, w_check를 만들고 각각 h + dh[i], w + dw[i]를 저장합니다.
    4-2. h_check가 0 이상 n 미만이고 w_check가 0 이상 n 미만이라면 다음을 수행합니다.
        4-2-a. board[h][w]와 board[h_check][w_check]의 값이 동일하다면 count의 값을 1 증가시킵니다.
5. count의 값을 return합니다.
"""


def solution(board, h, w):
    s = sum(board, []) # 2차원을 1차원으로 변환
    length = len(board) # 한 변의 길이
    one_h = h * length  # 고른 칸의 열의 위치를 1차원으로 변한했을 때의 위치
    index = w + one_h # 고른 칸의 위치 (1차원 변환)
    answer = 0
    #고른 칸의 윗쪽이 음수라면 고른 칸은 첫 번째 열에 있으므로 윗쪽은 없다.
    if (index - length) >= 0:
        if s[index - length] == s[index]:
            answer += 1
    #고른 칸의 아랫쪽이 마지막 위치 보다 크다면 고른 칸은 마지막 열에 있으므로 아랫쪽은 없다.
    if (index + length) < len(s):
        if s[index + length] == s[index]:
            answer += 1
    #고른 칸이 한 변의 길이값*h 와 같다면 (0번부터 시작하니 한 변의 길이*h 은 2차원 기준 맨 왼쪽에 위치한 칸이다.), 고른 칸은 맨 왼쪽에 위치한 것이다.
    if index % length != 0:
        if s[index - 1] == s[index]:
            answer += 1
    # 고른 칸의 오른쪽이 한 변의 길이 (0번부터 시작하니 한 변의 길이*h 은 2차원 기준 맨 왼쪽에 위치한 칸이다.)와 같은 위치라면 고른 칸은 맨 오른쪽에 위치한 것이다.
    if (index + 1) % length != 0:
        if s[index + 1] == s[index]:
            answer += 1

    return answer


board = [["blue", "red", "orange", "red"], ["red", "red", "blue", "orange"], ["blue", "orange", "red", "red"],
         ["orange", "orange", "red", "blue"]]
h = 1
w = 1

result = solution(board, h, w)
print("result = ", result)
