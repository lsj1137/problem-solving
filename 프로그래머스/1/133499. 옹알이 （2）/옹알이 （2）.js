function solution(babbling) {
    var answer = 0;
    let can = ['aya', 'ye', 'woo','ma'];
    for (word of babbling) {
        let checkWord = word;
        let lastWord = '';
        let index = 0;
        while (index < 4) {
            let w = can[index];
            if (checkWord.substring(0, w.length) === w){
                if (lastWord === w) {
                    break;
                }
                checkWord = checkWord.substring(w.length);
                if (checkWord === '') {
                    answer += 1;
                    break;
                }
                lastWord = w;
                index = 0;
                continue;
            }
            index += 1;
        }
    }
    return answer;
}