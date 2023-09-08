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