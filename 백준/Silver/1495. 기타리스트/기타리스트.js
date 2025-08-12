const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let inputs = [];
rl.on("line", (line) => {
  inputs.push(line);
});

rl.on("close", () => {
  let [N, S, M] = inputs[0].split(" ").map((n) => Number(n));
  let vDelta = inputs[1].split(" ").map((n) => Number(n));
  let que = [S];
  let newQue = new Set([]);
  for (delta of vDelta) {
    for (curV of que) {
      if (curV - delta > -1) {
        newQue.add(curV - delta);
      }
      if (curV + delta <= M) {
        newQue.add(curV + delta);
      }
    }
    if (newQue.size === 0) {
      que = [-1];
      break;
    }
    que = [...newQue];
    newQue = new Set([]);
  }
  let answer = Math.max(...que);
  console.log(answer);
  process.exit();
});
