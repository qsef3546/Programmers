/* 문제 설명
*  괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 한다는 뜻입니다.
*  예를 들어
*  "()()" 또는 "(())()" 는 올바른 괄호입니다.
*  ")()(" 또는 "(()(" 는 올바르지 않은 괄호입니다.
*  '(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 true를 return 하고,
*  올바르지 않은 괄호이면 false를 return 하는 solution 함수를 완성해 주세요.
* */

function solution(s){
    w = s.split('');
    if(w[-1] == '(' || w[0] == ')') return false; //처음과 끝이 닫히고 열린 괄호면 굳이 올바른 괄호로 짝지어진 것이 아니다.
    if(w.length % 2 == 1) return false; //올바른 괄호는 무조건 짝수이기에 홀수가 나온 다는 것은 올바른 괄호가 아니다.

    let count = 0 ;
    for(let word of w) {
        if(word == '(') count++; //열린 괄호 만큼 count 증가
        else {
            if(count < 1) return false; //닫힌 괄호만큼 count 감소 ( 단 count가 0 일경우, 이전에 열린 괄호가 없다)
            count--;

        }
    }

    return  count == 0 ? true : false;
}


var s = "(())()";

var answer = solution(s);