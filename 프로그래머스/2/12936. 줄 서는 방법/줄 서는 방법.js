function factorialBig(n) {
  let res = 1n;
  for (let i = 1n; i <= BigInt(n); i++) res *= i;
  return res;
}

function solution(n, k) {
  let answer = [];
  let arr = Array.from({length: n}, (_, i) => i+1);
  let range = factorialBig(n);
  let K = BigInt(k) - 1n;       // 0-based
  for (let i = n; i > 0; i--) {
    range /= BigInt(i);
    const idx = K / range;     // BigInt division
    answer.push(arr[Number(idx)]);
    arr.splice(Number(idx), 1);
    K %= range;
  }
  return answer;
}