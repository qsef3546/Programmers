// 문제 설명
//정수로 이루어진 배열 numbers가 있습니다. 배열 의 각 원소들에 대해 자신보다 뒤에 있는 숫자 중에서 자신보다 크면서 가장 가까이 있는 수를 뒷 큰수라고 합니다.
//정수 배열 numbers가 매개변수로 주어질 때, 모든 원소에 대한 뒷 큰수들을 차례로 담은 배열을 return 하도록 solution 함수를 완성해주세요. 
//단, 뒷 큰수가 존재하지 않는 원소는 -1을 담습니다.



function solution(numbers) {
    var answer = []; //정답 배열
    var stack = []; // 뒷 큰수들이 저장된 배열
    //numbers 의 마지막 원소부터 접근
    for(var i = numbers.length-1 ; i >= 0; i--){
        //현재 위치 있는 값이 스택에 마지막에 있는 값(현재 위치에서 가장 가까운 위치에 있는 값) 크면 스택을 계속 pop 시킨다.
        while(stack.length >0 && stack.at(-1) <= numbers[i]){
                stack.pop()
        }
        //스택이 비어있지 않다면 스택 마지막 값이 현재 위치에 있는 값보다 가장 가까운 큰 수
        //스택이 비어있다면 현재 위치에 있는 값이 가장 큰수
        stack.length > 0 ? answer.push(stack.at(-1)) : answer.push(-1)
        stack.push(numbers[i])

    }
    return answer.reverse(); //거꾸로 삽입했기에 reverse 해준다.
}

numbers = [9, 1, 5, 3, 6, 2]//[2, 3, 3, 5]
result = solution(numbers)
console.log("result = ", result)