function skipOp (curPos, op_start, op_end) {
    let [min, sec] = curPos.split(':').map((v)=>parseInt(v));
    let [opStMin, opStSec] = op_start.split(':').map((v)=>parseInt(v));
    let [opEndMin, opEndSec] = op_end.split(':').map((v)=>parseInt(v));
    if (min>opStMin && min<opEndMin) {
        return true;
    } else if (opStMin!==opEndMin && min===opStMin && sec>=opStSec) {
        return true;
    } else if (opStMin!==opEndMin && min===opEndMin && sec<=opEndSec) {
        return true;
    } else if (opStMin===opEndMin && min===opStMin && sec>=opStSec && sec<=opEndSec) {
        return true;
    }
    return false;
}

function solution(video_len, pos, op_start, op_end, commands) {
    var answer = '';
    let [maxMin, maxSec] = video_len.split(':').map((v)=>parseInt(v));
    let curPos = pos;
    if (skipOp(curPos, op_start, op_end)) {
        curPos = op_end;
    }
    for (c of commands) {
        let [min, sec] = curPos.split(':').map((v)=>parseInt(v));
        switch (c) {
            case "next":
                sec += 10;
                if (sec>=60) {
                    sec -= 60;
                    min += 1;
                }
                if (min>maxMin || (min===maxMin && sec>maxSec)) {
                    min = maxMin;
                    sec = maxSec;
                }
                break;
            case "prev":
                sec -= 10;
                if (sec<0) {
                    sec += 60;
                    min -= 1;
                }
                if (min<0) {
                    min = 0;
                    sec = 0;
                }
                break;
        }
        curPos = min.toString().padStart(2,'0')+':'+sec.toString().padStart(2,'0');
        if (skipOp(curPos, op_start, op_end)) {
            curPos = op_end;
        }
    }
    answer = curPos;
    return answer;
}