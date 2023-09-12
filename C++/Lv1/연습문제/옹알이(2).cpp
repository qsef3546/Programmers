/* 문제설명
 * 머쓱이는 태어난 지 11개월 된 조카를 돌보고 있습니다.
 * 조카는 아직 "aya", "ye", "woo", "ma" 네 가지 발음과 네 가지 발음을 조합해서 만들 수 있는 발음밖에 하지 못하고 연속해서 같은 발음을 하는 것을 어려워합니다.
 * 문자열 배열 babbling이 매개변수로 주어질 때, 머쓱이의 조카가 발음할 수 있는 단어의 개수를 return하도록 solution 함수를 완성해주세요.
 */

#include <string>
#include <vector>

using namespace std;
const vector<string> use = { "aya","ye","woo","ma" };

int solution(vector<string> babbling) {
    int answer = 0;
    auto babble = babbling.begin();
    string last_babble = ""; //추가된 옹알이 담을 변수
    while(babble != babbling.end()){
        int index = 0;  // 4가지 옹알이 배열 index
        int index2 = 0; //비교할 옹알이 현재 index
        while(index2 < babble->length()){
            if (use[index] == last_babble) { //현재 비교할 옹알이가 마지막으로 사용된 옹알이와 같다면 연속한 옹알이기 때문에 굳이 비교할 필요가 없다.
                index++;
            }
            else if (babble->substr(index2, use[index].size()) == use[index]) { // use[index] 에있는 옹알이와 비교할 옹알이과 같은지 확인
                last_babble = use[index]; //사용된 옹알이 대입
                index2 += use[index].size(); //다음 옹알이 위치까지 index2 변경
                index = 0; // 처음부터 다시 확인하기 위하여 0으로 초기화
            }
            else {
                index++; //옹알이가 다른경우
            }
            if (index == use.size()) break; //사용가능한 옹알이와 비교할 옹알이가 다른경우
        }
        if (index2 == babble->length()) { //index2가 현재 비교할 옹알이 길이와 같다면 4가지 발음으로 조합 가능한 옹알이 이다.
            answer++;
        }
        last_babble = "";
        babble++; //다음 옹알이를 비교하기 위하여 증가
    }
    return answer;
}

void main() {
    vector<string> babbling = {"aya", "yee", "u", "maa"};
}