function solution(picks, minerals) {
    var answer = 0;
    let estTired = [];
    let diaTired = 0;
    let ironTired = 0;
    let stoneTired = 0;
    for (i in minerals) {
        if (minerals[i] === "diamond") {
            diaTired += 1;
            ironTired += 5;
            stoneTired += 25;
        } else if (minerals[i] === "iron") {
            diaTired += 1;
            ironTired += 1;
            stoneTired += 5;
        } else {
            diaTired += 1;
            ironTired += 1;
            stoneTired += 1;
        }
        if (i%5 === 4 || Number(i)===minerals.length-1) {
            estTired.push([diaTired, ironTired, stoneTired]);
            diaTired = 0;
            ironTired = 0;
            stoneTired = 0;
        }
    }
    let picksSum = picks.reduce((cur, acum) => cur + acum, 0);
    let sortedEstTired = estTired.slice(0, picksSum).sort((a,b)=>b[2]-a[2])
    for (let i = 0; i<3; i++) {        
        for (let j=0; j<picks[i]; j++) {
            if (sortedEstTired.length===0) {
                break;
            }
            let curEstTired = sortedEstTired.shift();
            answer += curEstTired[i];
        }
    }
    return answer;
}