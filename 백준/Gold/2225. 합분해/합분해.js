const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let inputs = [];
rl.on("line", (line) => {
  inputs.push(line);
});

let dpArr = {};
function dp(n,k) {
  if (n===0 || k===1) {
    return 1;
  }
  if (dpArr[[n,k]]!==undefined) {
    return dpArr[[n,k]];
  }
  let result = 0;
  for (let i=n; i>-1; i--) {
    result += dp(i, k-1)
    result %= 1000000000;
  }
  dpArr[[n,k]] = result;
  return result;
}

rl.on("close", () => {
  let answer = 0;
  let [N,K] = inputs[0].split(' ').map((n)=>Number(n));
  answer = dp(N,K);
  console.log(answer);
  process.exit();
});
