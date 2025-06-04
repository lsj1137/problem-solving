function makeDictionary(word, depth, goal) {
    if (depth===goal) {
        return [word];
    }
    let result = [];
    let letter = 'AEIOU';
    for (l of letter) {
        result.push(...makeDictionary(word+l, depth+1, goal));
    }
    return result;
}

function solution(word) {
    var answer = 0;
    let dictionary = [];
    for (let i=1; i<6; i++) {
        dictionary.push(...makeDictionary('',0,i));
    }
    dictionary.sort();
    answer = dictionary.indexOf(word)+1;
    return answer;
}