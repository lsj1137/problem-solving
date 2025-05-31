function gcd(a, b) {
  while (b !== 0) {
    let t = b;
    b = a % b;
    a = t;
  }
  return a;
}

function gcdMultiple(numbers) {
  return numbers.reduce((a, b) => gcd(a, b));
}

function solution(arrayA, arrayB) {
    var answer = 0;
    let gcdA = gcdMultiple(arrayA);
    let gcdB = gcdMultiple(arrayB);
    for (a of arrayA) {
        if (a % gcdB===0) {
            gcdB = 0;
            break;
        }
    }
    for (b of arrayB) {
        if (b % gcdA===0) {
            gcdA = 0;
            break;
        }
    }
    answer = Math.max(gcdA, gcdB);
    return answer;
}