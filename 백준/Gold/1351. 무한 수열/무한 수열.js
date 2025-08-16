const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let inputs = [];
rl.on("line", (line) => {
  inputs.push(line);
});

let arr = {'0':1};
function getNth(n, p, q) {
  if (arr[n]!==undefined) {
    return arr[n];
  }
  let nth = getNth(Math.floor(n/p), p, q) + getNth(Math.floor(n/q), p, q);
  arr[n] = nth;
  return nth;
}

rl.on("close", () => {
  let answer = 0;
  let [N, P, Q] = inputs[0].split(' ').map((n)=>Number(n));
  answer = getNth(N,P,Q);
  console.log(answer);
  process.exit();
});
