function solution(sequence, k) {
    var answer = [];
    let first = 0;
    let last = 0;
    let partSum = sequence[0];
    while (true){
        if (partSum <= k) {
            if (partSum === k) {
                answer.push([first, last, last-first])
            }
            if (last < sequence.length-1) {
                last += 1;
                partSum += sequence[last];  
            } else {
                break;
            }
        } else {
            if (first === last) {
                if (last < sequence.length-1) {
                    last += 1;
                    partSum += sequence[last]; 
                } else {
                    break;
                }
            }
            partSum -= sequence[first];
            first += 1;
        }
    }
    answer.sort((a,b)=>a[2]-b[2]);
    return answer[0].splice(0,2);
}