function solution(keymap, targets) {
    var answer = [];
    let guide = {};
    for (let i=0; i<100; i++) {
        for (key of keymap) {
            if (i < key.length) {
                if (!guide[key[i]]) {
                    guide[key[i]] = i+1;
                }
            }
        }
    }
    for (t of targets) {
        let count = 0;
        for (c of t) {
            if (guide[c]) {
                count += guide[c];
            } else {
                count = -1;
                break;
            }
        }
        answer.push(count);
    }
    return answer;
}