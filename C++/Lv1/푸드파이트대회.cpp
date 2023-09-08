#include <string>
#include <vector>
#include <sstream>
using namespace std;

string solution(vector<int> food) {
    string answer = "";
    vector<int> front;
    vector<int> back;
    stringstream ss;

    int count = 1;

    for (int i = 1; i < food.size(); i++) {
        front.insert(front.end(), food[i] / 2, count);
        back.insert(back.begin(), food[i] / 2, count);
        count++;
    }
    front.emplace_back(0);
    front.insert(front.end(), back.begin(), back.end());
    for (auto i : front) ss << i;

    answer = ss.str();

    return answer;
}