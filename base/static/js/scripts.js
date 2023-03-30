function solution(n, arr1, arr2) {
    let answer=[];
    var firstArrToBinary = [];
    var secondArrToBinary = [];
    let firstArr = []
    let secondArr = []
    let prf = "0"
    let word;
    //arr1,2 2진수로 변환
    for(let i =0;i<arr1.length;i++){
        arr1[i]= arr1[i].toString(2)
        arr2[i] = arr2[i].toString(2)
        
        while(arr1[i].length<n)
        arr1[i] = prf + arr1[i]

        while(arr2[i].length<n)
        arr2[i] = prf + arr2[i]
        
        firstArrToBinary.push(arr1[i])
        secondArrToBinary.push(arr2[i])
    }

    //arr1 변환  
    for(let i =0;i<arr1.length;i++){
        word = ""
        for(let str of arr1[i]){
            if( str == "0")
            word+=" "
            else word+="#"
        }
        firstArr.push(word)
    }
    //arr2 변환
    for(let j =0;j<arr2.length;j++){
        word = ""
        for(let str of arr2[j]){
            if( str == "0")
            word+=" "
            else word+="#"
        }
        secondArr.push(word)
    }
    
    //두 arr 을 보며 정리
    for(let k=0;k<firstArr.length;k++){
        word=""
        for(let t =0;t<firstArr[k].length;t++){
            if(firstArr[k].charAt(t) != "#" && secondArr[k].charAt(t) != "#" )
            word+=" "
            else word+="#"
        }
        answer.push(word)
    }
   
    return answer;
}

console.log(solution(5,[9, 20, 28, 18, 11],[30, 1, 21, 17, 28]))
// console.log(solution(6,[46, 33, 33 ,22, 31, 50],[27 ,56, 19, 14, 14, 10]))
    


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