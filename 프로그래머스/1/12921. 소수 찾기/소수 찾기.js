function solution(n) {
    var answer = 0;
    let eratos = Array.from(new Array(n+1),() => true);
    for (let i=2; i<n+1; i++) {
        if (eratos[i]) {
            for (let j=i*2; j<n+1; j+=i) {
                eratos[j] = false;
            }
        }
    }
    answer = eratos.filter((val)=>val).length-2;
    return answer;
}