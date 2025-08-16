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
function getNth(n, p, q, x, y) {
  if (n<=0) {
    return 1;
  }
  if (arr[n]!==undefined) {
    return arr[n];
  }
  let nth = getNth(Math.floor(n/p)-x, p, q, x, y) + getNth(Math.floor(n/q)-y, p, q, x, y);
  arr[n] = nth;
  return nth;
}

rl.on("close", () => {
  let answer = 0;
  let [N, P, Q, X, Y] = inputs[0].split(' ').map((n)=>Number(n));
  answer = getNth(N,P,Q,X,Y);
  console.log(answer);
  process.exit();
});
