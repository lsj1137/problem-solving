function calTime(time) {
    let newTime = time+10;
    if (newTime%100 >= 60) {
        newTime += 40;  // +100-60
    }
    return newTime;
}

function solution(schedules, timelogs, startday) {
    var answer = 0;
    let due = [];
    for (schedule of schedules) {
        due.push(calTime(schedule));
    }
    for (let i=0; i<due.length; i++) {
        for (let j=0; j<7; j++) {
            let day = (startday-1+j) % 7;
            if (day<5 && timelogs[i][j]>due[i]) break;
            if (j===6) answer += 1;
        }
    }
    return answer;
}