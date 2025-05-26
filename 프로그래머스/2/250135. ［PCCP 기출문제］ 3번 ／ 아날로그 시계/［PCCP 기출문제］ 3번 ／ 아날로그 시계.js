function solution(h1, m1, s1, h2, m2, s2) {
    var answer = 0;
    let [curH, curM, curS] = [h1, m1, s1];
    let [hAngle, mAngle, sAngle] = [0, 0, 0];
    let [hInc, mInc, sInc] = [360/12/60/60, 360/60/60, 360/60];
    hAngle = (h1 * 3600 + m1 * 60 + s1) * hInc % 360;
    mAngle = (m1 * 60 + s1) * mInc % 360;
    sAngle = s1 * sInc % 360;
    while (curH<h2 || curM<m2 || curS<s2) {
        let alarm = true;
        curS += 1;
        if (curS % 60 == 0) {
            curS -= 60;
            curM += 1;
            if (curM % 60 === 0) {
                curM -= 60;
                curH += 1;
            }
        }
        if (sAngle<=mAngle && sAngle+sInc>=mAngle+mInc) {
            answer += 1;
            alarm = true;
        }
        if (sAngle<=hAngle && sAngle+sInc>=hAngle+hInc) {
            answer += 1;
            alarm = true;
        }
        if (alarm && mAngle===hAngle) {
            answer -= 1;
        }
        hAngle = (curH * 3600 + curM * 60 + curS) * hInc % 360;
        mAngle = (curM * 60 + curS) * mInc % 360;
        sAngle = curS * sInc % 360;
    }
    if (h1<12 && h2>=12 && s2>0) {
        answer -= 1;
    }
    return answer;
}