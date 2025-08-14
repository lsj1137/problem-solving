const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let inputs = [];
rl.on("line", (line) => {
  inputs.push(line);
});

let arr = [
  [0, 0],
  [1, 0],
  [0, 1],
];
function fibonacci(n) {
  if (n < arr.length) {
    return arr[n];
  }
  let fibNmin1 = fibonacci(n - 1);
  let fibNmin2 = fibonacci(n - 2);
  let fibN = [fibNmin1[0] + fibNmin2[0], fibNmin1[1] + fibNmin2[1]];
  arr.push(fibN);
  return fibN;
}

rl.on("close", () => {
  let answer = [0, 0];
  let [D, K] = inputs[0].split(" ").map((n) => Number(n));
  let [a, b] = fibonacci(D);
  for (let i = 1; i * a < K + 1; i++) {
    if ((K - i * a) % b === 0) {
      answer[0] = i;
      answer[1] = (K - i * a) / b;
      if (answer[0] <= answer[1]) {
        break;
      }
    }
  }
  console.log(answer[0]);
  console.log(answer[1]);
  process.exit();
});
