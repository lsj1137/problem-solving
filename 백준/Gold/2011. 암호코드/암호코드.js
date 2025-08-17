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
function dp(code) {
  if (dpArr[code] !== undefined){
    return dpArr[code];
  }
  if (code[0]==='0') {
    dpArr[code]=0;
    return 0;
  }
  if (code.length===1) {
    dpArr[code]=1;
    return 1;
  } else if (code.length===2) {
    if (Number(code)<=26) {
      if (code==='10'|| code==='20') {
        dpArr[code]=1;
        return 1;
      } else {
        dpArr[code]=2;
        return 2;
      }
    } else {
      return dp(code.slice(1));
    }
  }
  let result = dp(code.slice(1));
  if (Number(code.slice(0,2))<=26) {
    result += dp(code.slice(2));
  }
  result %= 1000000;
  dpArr[code] = result;
  return result;
}

rl.on("close", () => {
  let answer = 0;
  let code = inputs[0];
  answer = dp(code);
  console.log(answer);
  process.exit();
});
