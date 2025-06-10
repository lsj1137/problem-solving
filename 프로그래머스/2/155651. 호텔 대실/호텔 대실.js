function toMinutes(time) {
    let [hour,minute] = time.split(":").map((t)=>Number(t));
    minute += hour*60;
    return minute
}

function solution(book_time) {
    var answer = 0;
    let bs = toMinutes('00:00');
    let be = toMinutes('24:10');
    let check = Array.from(new Array(be), ()=>0);
    for (usingTime of book_time) {
        let start = toMinutes(usingTime[0]);
        let end = toMinutes(usingTime[1])+10;
        for (let i=start; i<end; i++) {
            check[i] += 1;
        }
    }
    answer = Math.max(...check);
    return answer;
}
