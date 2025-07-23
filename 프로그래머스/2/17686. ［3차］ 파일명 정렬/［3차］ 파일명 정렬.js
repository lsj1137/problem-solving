function divide(fileName) {
    let [h, n, t] = ['','',''];
    let process = 0;
    let nLen = 0;
    for (c of fileName) {
        let isChar = c===' ' || isNaN(c);
        if (isChar && process === 0) {
            h += c;
        } else if (!isChar && process === 0) {
            process += 1;
            n += c;
            nLen += 1;
        } else if (nLen<5 && !isChar && process === 1) {
            n += c;
            nLen += 1;
        } else if ((nLen===5 || isChar) && process === 1) {
            process += 1;
            t += c;
        } else {
            t += c;
        }
    }
    return [h,n,t];
}

function solution(files) {
    var answer = [];
    let newFiles = [];
    for (file of files){
        newFiles.push(divide(file));
    }
    newFiles = newFiles.sort((a,b)=>{
        let [f,s] = [a[0].toUpperCase(), b[0].toUpperCase()];
        if (f !== s){
            if (f > s) {
                return 1;
            }
            if (f < s) {
                return -1;
            }
                return 0;
        } else if (parseInt(a[1]) !== parseInt(b[1])) {
            return parseInt(a[1]) - parseInt(b[1]);
        } else {
            return 1;
        }
    });
    newFiles.map((file)=> answer.push(file[0]+file[1]+file[2]));
    return answer;
}