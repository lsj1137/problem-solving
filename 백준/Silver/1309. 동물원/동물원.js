const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.on("line", (line) => {
  let n = line;
  let answer = 0;
  let count = [1, 0];
  for (let i = 0; i < n; i++) {
    let temp = [...count];
    count[0] = (temp[0] + temp[1]) % 9901;
    count[1] = (temp[0] * 2 + temp[1]) % 9901;
  }
  answer = (count[0] + count[1]) % 9901;
  console.log(answer);
  rl.close();
});
rl.on("close", () => {});
