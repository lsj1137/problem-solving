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
function dfs(n, m, cx, cy, checked) {
  if (cx===n && cy===m) {
    return 1n;
  }
  for (let i=0; i<2; i++) {
    let nx = cx + dx[i];
    let ny = cy + dy[i];
    if (nx>-1 && nx<n+1 && ny>-1 && ny<m+1 && checked[cx][cy][i]!==-1n) {
      if (checked[nx][ny][2] === 0n) {
        checked[cx][cy][i] += dfs(n, m, nx, ny, checked);
      } else if (checked[nx][ny][2] > 0n) {
        checked[cx][cy][i] += checked[nx][ny][2];
      }
    }
    if (checked[cx][cy][i]===0n) {
      checked[cx][cy][i] = -1n;
    }
  }
  let up = checked[cx][cy][0]===-1n ? 0n : checked[cx][cy][0];
  let right = checked[cx][cy][1]===-1n ? 0n : checked[cx][cy][1];
  checked[cx][cy][2] = up + right;
  return checked[cx][cy][2];
}

rl.on("close", () => {
  let answer = 0;
  let [N,M] = inputs[0].split(' ').map((n)=>Number(n));
  let K = Number(inputs[1]);
  let broken = inputs.slice(2).map((roadInfo)=>{
    let infos = roadInfo.split(' ').map((n)=>Number(n));
    let arranged = [[infos[0],infos[1]], [infos[2], infos[3]]];
    arranged.sort((a,b)=>{if (a[0]!==b[0]){return a[0]-b[0]} else {return a[1]-b[1]}});
    return arranged;
  })
  let checked = Array.from({length:N+1}, ()=> Array.from({length:M+1}, ()=>[0n, 0n, 0n]));
  for (road of broken) {
    let [cx,cy] = road[0];
    let [nx,ny] = road[1];
    if (nx-cx===1) {
      checked[cx][cy][0] = -1n;
    } else {
      checked[cx][cy][1] = -1n;
    }
  }
  answer = dfs(N, M, 0, 0, checked);
  console.log(answer.toString());
  process.exit();
});
