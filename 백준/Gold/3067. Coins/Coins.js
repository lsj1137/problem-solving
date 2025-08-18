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
  let T = Number(inputs[0]);
  for (let i=0; i<T; i++) {
    let N = Number(inputs[1+i*3]);
    let coins = inputs[2+i*3].split(' ').map((n) => Number(n));
    let M = Number(inputs[(i+1)*3]);
    let dpArr = Array.from({length: M+1}, ()=>0);
    for (coin of coins) {
      dpArr[coin] += 1;
      for (let i=coin; i<M+1; i++) {
        dpArr[i] = dpArr[i] + dpArr[i-coin];
      }
    }
    console.log(dpArr[M]);
  }
  process.exit();
});
