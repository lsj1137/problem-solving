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
  let [N, D] = inputs[0].split(" ").map((n) => Number(n));
  let shortCuts = inputs
    .slice(1)
    .map((i) => i.split(" ").map((n) => Number(n)));
  shortCuts.sort((a, b) => a[0] - b[0]);
  let distance = Array.from({ length: D + 1 }, (_, i) => i);
  for (cut of shortCuts) {
    let [start, goal, len] = cut;
    if (goal > D) continue;
    if (distance[goal] > distance[start] + len) {
      for (let i = goal; i < D + 1; i++) {
        distance[i] = Math.min(distance[i], distance[start] + len + i - goal);
      }
    }
  }
  console.log(distance[D]);
  process.exit();
});
