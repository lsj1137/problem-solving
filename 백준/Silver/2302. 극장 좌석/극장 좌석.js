const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let inputs = [];
rl.on("line", (line) => {
  inputs.push(line);
});

let arr = [1, 1, 2];
function fibonacci(n) {
  if (n < arr.length) {
    return arr[n];
  }
  let a = fibonacci(n - 1);
  let b = fibonacci(n - 2);
  arr.push(a + b);
  return a + b;
}

rl.on("close", () => {
  let answer = 1;
  let N = Number(inputs[0]);
  let M = Number(inputs[1]);
  inputs.push(N + 1);
  let mvps = [0];
  for (let i = 0; i < M + 1; i++) {
    let mvp = inputs[2 + i];
    let gap = mvp - mvps[mvps.length - 1];
    answer *= fibonacci(gap - 1);
    mvps.push(mvp);
  }
  console.log(answer);
  process.exit();
});
