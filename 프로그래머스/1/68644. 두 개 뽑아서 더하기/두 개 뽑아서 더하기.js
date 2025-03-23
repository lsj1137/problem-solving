function solution(numbers) {
    var answer = [];
    let sums = new Set();
    for (let i=0; i<numbers.length-1; i++) {
        for (let j=i+1; j<numbers.length; j++) {
            sums.add(numbers[i]+numbers[j])
        }
    }
    answer = [...sums];
    answer.sort((a,b)=>{
      if (a>b){
          return 1;
      }   else {
          return -1;
      }
    });
    return answer;
}