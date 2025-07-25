function solution(phone_book) {
    var answer = true;
    let maps = {};
    phone_book.sort((a,b)=>a.length-b.length);
    for (phone_num of phone_book) {
        let curMap = maps;
        [...phone_num].forEach((num, idx)=>{
            if (curMap[num] === 0) {
                answer = false;
                curMap[num] = {};
            }
            if (!curMap[num]) {
                curMap[num] = {}
            }
            if (idx === phone_num.length-1) {
                curMap[num] = 0;
            }
            curMap = curMap[num];
        })
    }
    return answer;
}