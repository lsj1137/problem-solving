function check(ref, skill) {
    let curStep = 0;
    for (c of skill) {
        if (ref[c] !== undefined && ref[c] === curStep) {
            curStep += 1;
        } else if (ref[c] !== undefined && ref[c] !== curStep) {
            return false;
        }
    }
    return true;
}

function solution(skill, skill_trees) {
    var answer = 0;
    let ref = {};
    let index = 0;
    for (s of skill) {
        ref[s] = index++;
    }
    for (skillTree of skill_trees) {
        if (check(ref, skillTree)) {
            answer += 1;
        }
    }
    return answer;
}