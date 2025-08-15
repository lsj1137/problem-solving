const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let inputs = [];
rl.on("line", (line) => {
  inputs.push(line);
});

function calculate(arr) {
  let result = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
  for (let i = 0; i < 10; i++) {
    for (let j = 0; j <= i; j++) {
      result[i] += arr[j];
    }
  }
  return result;
}

rl.on("close", () => {
  let answer = [];
  let T = Number(inputs[0]);
  let arrs = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]];
  for (let i = 1; i < 64; i++) {
    arrs.push(calculate(arrs[i - 1]));
  }
  for (let i = 1; i < T + 1; i++) {
    answer.push(
      arrs[Number(inputs[i]) - 1].reduce((acc, curr) => acc + curr, 0)
    );
  }
  console.log(answer.join("\n"));
  process.exit();
});
