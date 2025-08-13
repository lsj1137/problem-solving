const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let inputs = [];
rl.on("line", (line) => {
  inputs.push(line);
});

let dx = [1, 0];
let dy = [0, 1];
function dfs(cx, cy, board, checked) {
  let N = board.length;
  if (cx === N - 1 && cy === N - 1) {
    return 1n;
  }
  let result = 0n;
  let jump = board[cx][cy];
  if (jump !== 0) {
    for (let i = 0; i < 2; i++) {
      let nx = cx + dx[i] * jump;
      let ny = cy + dy[i] * jump;
      if (nx < N && ny < N) {
        if (checked[nx][ny] === 0n) {
          checked[cx][cy] += dfs(nx, ny, board, checked);
        } else if (checked[nx][ny] > 0n) {
          checked[cx][cy] += checked[nx][ny];
        }
      }
    }
    if (checked[cx][cy] === 0n) {
      checked[cx][cy] = -1n;
    }
  }
  result = checked[cx][cy] === -1n ? 0n : checked[cx][cy];
  return result;
}

rl.on("close", () => {
  let answer = 0n;
  let N = Number(inputs[0]);
  let board = inputs
    .slice(1)
    .map((line) => line.split(" ").map((n) => Number(n)));
  let checked = Array.from({ length: N }, () =>
    Array.from({ length: N }, () => 0n)
  );
  answer = dfs(0, 0, board, checked).toString();
  console.log(answer);
  process.exit();
});
