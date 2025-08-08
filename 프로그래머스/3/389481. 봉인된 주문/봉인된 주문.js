function alphaToIndex(spell, dict) {
    let result = 0;
    for (let i=spell.length-1; i>-1; i--) {
        let m = spell.length-1 - i;
        result += dict[spell[i]] * (26**m);
    }
    return result;
}

function indexToAlpha(num, dict) {
    let result = '';
    while (num>0) {
        let remain = (num-1)%26;
        result += dict[remain];
        num = Math.floor((num-1)/26);
    }
    result = [...result].reduce((cur,acum)=> acum+cur,'');
    return result;
}

function solution(n, bans) {
    var answer = '';
    let dict1 = {a:1, b:2, c:3, d:4, e:5, f:6, g:7, h:8, i:9, j:10, k:11, l:12, m:13, n:14, o:15, p:16, q:17, r:18, s:19, t:20, u:21, v:22, w:23, x:24, y:25, z:26};
    let dict2 = {0:'a', 1:'b', 2:'c', 3:'d', 4:'e', 5:'f', 6:'g', 7:'h', 8:'i', 9:'j', 10:'k', 11:'l', 12:'m', 13:'n', 14:'o', 15:'p', 16:'q', 17:'r', 18:'s', 19:'t', 20:'u', 21:'v', 22:'w', 23:'x', 24:'y', 25:'z'};
    let banIndex = [];
    for (spell of bans) {
        banIndex.push(alphaToIndex(spell, dict1));
    }
    banIndex.sort((a,b)=>a-b);
    for (num of banIndex) {
        if (num<=n) {
            n += 1;
        }
    }
    answer = indexToAlpha(n, dict2);
    return answer;
}