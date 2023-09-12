/* 문제 설명
 *
 * 두 정수 X, Y의 임의의 자리에서 공통으로 나타나는 정수 k(0 ≤ k ≤ 9)들을 이용하여 만들 수 있는 가장 큰 정수를 두 수의 짝꿍이라 합니다
 * (단, 공통으로 나타나는 정수 중 서로 짝지을 수 있는 숫자만 사용합니다). X, Y의 짝꿍이 존재하지 않으면, 짝꿍은 -1입니다. X, Y의 짝꿍이 0으로만 구성되어 있다면, 짝꿍은 0입니다.
 * 예를 들어, X = 3403이고 Y = 13203이라면, X와 Y의 짝꿍은 X와 Y에서 공통으로 나타나는 3, 0, 3으로 만들 수 있는 가장 큰 정수인 330입니다.
 * 다른 예시로 X = 5525이고 Y = 1255이면 X와 Y의 짝꿍은 X와 Y에서 공통으로 나타나는 2, 5, 5로 만들 수 있는 가장 큰 정수인 552입니다
 * (X에는 5가 3개, Y에는 5가 2개 나타나므로 남는 5 한 개는 짝 지을 수 없습니다.)
 * 두 정수 X, Y가 주어졌을 때, X, Y의 짝꿍을 return하는 solution 함수를 완성해주세요.
 * */


#include <string>
#include <map>
using namespace std;

string solution(string X, string Y) {
    string answer = "";
    map<char, int> mX; // 문자열 X에 사용된 문자와 문자 개수 담을 map
    map<char, int> mY; // 문자열 Y에 사용된 문자와 문자 개수 담을 map
    for (auto x : X) mX[x]++; //사용된 문자와 사용된 개수 저장
    for (auto y : Y) mY[y]++;
    for (auto x = mX.rbegin(); x != mX.rend(); x++) { //가장 큰 수부터 insert 를 해야 만들 수 있는 가장 큰 정수이다.
        if (mY[x->first] > 0) answer.insert(answer.end(), min(x->second, mY[x->first]), x->first);
        // X에 사용된 문자가 y에 있는지 확인하여 있으면 X,Y에서 사용된 최소 개수만큼 insert
    }

    if (answer.empty()) return "-1"; // 없을경우 -1 리턴
    if (answer[0] == '0') return "0"; // "00..."으로만 되어있을경우 "0" 으로 리턴
    return answer;
}


void main() {
    String X = "12321";
    String Y = "42531";
    string answer = solution(x,y);
}