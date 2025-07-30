const MOD = 1000000007n;

function fastDoublingMod(n) {
  if (n === 0n) {
    return [0n, 1n];
  }
  // n을 반으로 나눕니다.
  const half = n >> 1n;  
  const [fk, fk1] = fastDoublingMod(half);

  // F(2k) = F(k) * [2·F(k+1) − F(k)]
  const t = (2n * fk1 % MOD - fk + MOD) % MOD;
  const c = (fk * t) % MOD;

  // F(2k+1) = F(k)² + F(k+1)²
  const d = (fk * fk + fk1 * fk1) % MOD;

  if ((n & 1n) === 0n) {
    // n이 짝수
    return [c, d];
  } else {
    // n이 홀수
    return [d, (c + d) % MOD];
  }
}

function solution(n) {
    var answer = 0;
    n = BigInt(n+1);
    const result = fastDoublingMod(n)[0];
    // MOD 이하(BigInt) 이므로 안전하게 Number로 변환
    answer = Number(result);
    return answer;
}