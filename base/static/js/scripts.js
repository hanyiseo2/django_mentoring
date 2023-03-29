function solution(sizes) {
    var answer = 0;
    let long,short
    
    let width=[]
    let height=[]
    for(let arr of sizes){
        if(arr[0]>arr[1]){ 
            long=arr[0]
            short=arr[1]
        }
        else{
            long=arr[1]
            short=arr[0]
        }
        width.push(long)
        height.push(short)
    }
    width = Math.max(...width)
    height = Math.max(...height)
    answer = width*height
    
    return answer;
}
console.log(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))


//9:27 => 9:47

/*
60, 50 / 80, 60
1첫번째와 2첫번째 체크 => 1첫번째와 2두번째체크 
1두번째와 2두번째 체크
근ㅔ 안ㅚ면 첫번째 바꾸기 두번째도 두ㄴㅐ랑 비했ㅡㄹ때 안ㅚㅕㄴ 두번째 바꾸기

*/






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