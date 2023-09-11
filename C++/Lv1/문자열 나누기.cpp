/* 문제 설명
 *문자열 s가 입력되었을 때 다음 규칙을 따라서 이 문자열을 여러 문자열로 분해하려고 합니다.
 *
 *  - 먼저 첫 글자를 읽습니다. 이 글자를 x라고 합시다.
 *  - 이제 이 문자열을 왼쪽에서 오른쪽으로 읽어나가면서, x와 x가 아닌 다른 글자들이 나온 횟수를 각각 셉니다.
 *    처음으로 두 횟수가 같아지는 순간 멈추고, 지금까지 읽은 문자열을 분리합니다.
 *  - s에서 분리한 문자열을 빼고 남은 부분에 대해서 이 과정을 반복합니다. 남은 부분이 없다면 종료합니다.
 *  - 만약 두 횟수가 다른 상태에서 더 이상 읽을 글자가 없다면, 역시 지금까지 읽은 문자열을 분리하고, 종료합니다.
 *
 *  문자열 s가 매개변수로 주어질 때, 위 과정과 같이 문자열들로 분해하고, 분해한 문자열의 개수를 return 하는
 *  함수 solution을 완성하세요.
 *
 * */

#include <string>
#include <vector>

using namespace std;

int solution(string s) {
    int answer = 0;
    int idx = 0; //비교할 문자 index 값 (초기값 0 대입)
    vector<string> an; //읽은 문자열 저장할 벡터
    while (idx < s.length()) { //비교할 문자 index가 마지막 문자 index와 비교할 때까지 반복
        int same = 1; // 같은 문자일 경우 횟수를 증가시킬 변수 (idx 에 초기값을 대입하여서 1로 시작)
        int diff = 0; // 다른 문자일 경우 횟수를 증가시킬 변수
        for (auto c = idx + 1; c < s.length(); c++) {
            s[idx] == s[c] ? same++ : diff++; //같은 / 다른 문자일경우 횟수 1증가
            if (same == diff) { //같은 문자와 다른 문자 횟수가 같을 경우
                break;
            }
        }
        an.push_back(s.substr(idx, same + diff)); //횟수가 같을경우 , 마지막까지 횟수가 같지 않을경우에 대한 문자열 저장
        idx += same + diff; // 저장된 문자열 위치까지 증가
    }
    answer = an.size(); // 저장된 문자열 개수 대입
    return answer;
}

void main() {
    string s = "banana";  //입력할 문자열
    int answer = solution(s);
}
