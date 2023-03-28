function solution(d, budget) {
    let answer = 0;
    
    d.sort((a,b)=> a-b) 
    
    for(let i =0;i<d.length;i++){
        if(budget-d[i]>=0){
            budget -= d[i]
            answer++
        }
        else{
            return answer
        }
    }
    return answer;
}

console.log(solution([1,3,2,1,5], 9))
// console.log(solution([2,2,3,3], 5))


//budget - 해당 d를 빼주기














function solution1(n, m) {
    var answer = [];
    let smallerNum = Math.min(n,m)
    let a,b;
    let isValid=true
    while(isValid){
        for(let i =2;i<smallerNum;i++){
            if(n%i==0&&m%i==0){
                n=n/i //2
                m=m/i //4
            }
        }
    }
    return answer;
}

// console.log(solution(6,12))

//7:05
/*
3:6 12
2:2 4
 :1 2
*/