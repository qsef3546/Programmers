/* 문제 설명
 *
 * 수웅이는 매달 주어진 음식을 빨리 먹는 푸드 파이트 대회를 개최합니다.
 * 이 대회에서 선수들은 1대 1로 대결하며, 매 대결마다 음식의 종류와 양이 바뀝니다.
 * 대결은 준비된 음식들을 일렬로 배치한 뒤, 한 선수는 제일 왼쪽에 있는 음식부터 오른쪽으로, 다른 선수는 제일 오른쪽에 있는
 * 음식부터 왼쪽으로 순서대로 먹는 방식으로 진행됩니다. 중앙에는 물을 배치하고, 물을 먼저 먹는 선수가 승리하게 됩니다.
 * 이때, 대회의 공정성을 위해 두 선수가 먹는 음식의 종류와 양이 같아야 하며, 음식을 먹는 순서도 같아야 합니다. 또한, 이번 대회부터는
 * 칼로리가 낮은 음식을 먼저 먹을 수 있게 배치하여 선수들이 음식을 더 잘 먹을 수 있게 하려고 합니다. 이번 대회를 위해 수웅이는 음식을
 * 주문했는데, 대회의 조건을 고려하지 않고 음식을 주문하여 몇 개의 음식은 대회에 사용하지 못하게 되었습니다.
 * 예를 들어, 3가지의 음식이 준비되어 있으며, 칼로리가 적은 순서대로 1번 음식을 3개, 2번 음식을 4개, 3번 음식을 6개 준비했으며,
 * 물을 편의상 0번 음식이라고 칭한다면, 두 선수는 1번 음식 1개, 2번 음식 2개, 3번 음식 3개씩을 먹게 되므로 음식의 배치는
 * "1223330333221"이 됩니다. 따라서 1번 음식 1개는 대회에 사용하지 못합니다.
 *
 * 수웅이가 준비한 음식의 양을 칼로리가 적은 순서대로 나타내는 정수 배열 food가 주어졌을 때,
 * 대회를 위한 음식의 배치를 나타내는 문자열을 return 하는 solution 함수를 완성해주세요.
 * */
#include <string>
#include <vector>
#include <sstream>
using namespace std;

string solution(vector<int> food) {
    string answer = "";
    vector<int> front; // 선수1 음식 vector
    vector<int> back;  // 선수2 음식 vector
    stringstream ss;

    int count = 1; // 칼로리

    for (int i = 1; i < food.size(); i++) {
        front.insert(front.end(), food[i] / 2, count); // 선수1은 칼로리가 적은 음식을 오름차순으로 추가
        back.insert(back.begin(), food[i] / 2, count); // 선수2는 칼로리가 적은 음식을 내림차순으로 추가
        count++;
    }
    front.emplace_back(0);  // 종료를 나타내는 (0) 추가
    front.insert(front.end(), back.begin(), back.end()); //선수1과 선수2의 음식 순서 합치기
    for (auto i : front) ss << i; // 합친 음식 순서를 문자열로 만들기 위하여 stream에 대입

    answer = ss.str(); // 음식 순서 문자열화

    return answer;
}

void main(){
    vector<int> food = {1, 3, 4, 6};
    string answer = solution(food);
}