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
  let answer = 0;
  let N = Number(inputs[0]);
  let numArr = inputs[1].split(" ").map((n) => Number(n));
  let limit = Number(inputs[2]);
  let MAX_NUM = Math.max(...numArr) * limit;
  let countArr = Array.from({ length: MAX_NUM }, () => Infinity);
  countArr[0] = 0;
  for (let i = 1; i < MAX_NUM + 1; i++) {
    for (n of numArr) {
      if (i - n >= 0 && countArr[i - n] + 1 <= limit) {
        countArr[i] = Math.min(countArr[i], countArr[i - n] + 1);
      }
    }
    if (countArr[i] === Infinity) {
      answer = i;
      break;
    }
  }
  if (answer % 2 === 0) {
    console.log(`holsoon win at ${answer}`);
  } else {
    console.log(`jjaksoon win at ${answer}`);
  }
  process.exit();
});
