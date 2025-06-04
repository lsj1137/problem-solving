function solution(numbers) {
    var answer = [];
    for (n of numbers) {
        let bitN = n.toString(2);
        let lastOne = -1;
        let lastZero = -1;
        for (i in bitN) {
            if (bitN[i]==='1') {
                lastOne = Math.max(Number(i), lastOne);
            } else {
                lastZero = Math.max(Number(i), lastZero);
            }
        }
        if (lastOne === -1) {
            bitN = '1';
        } else if (lastZero === -1) {
            bitN = '0' + bitN.substring(1);
            bitN = '1' + bitN;
        } else if (lastOne<lastZero) {
            bitN = bitN.substring(0,lastZero) + '1' + bitN.substring(lastZero+1);
        } else {
            bitN = bitN.substring(0,lastZero) + '10' + bitN.substring(lastZero+2);
        }
        answer.push(parseInt(bitN, 2))
    }
    return answer;
}