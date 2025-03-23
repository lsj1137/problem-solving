const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});


let grades = [];
let scoreBoard = {
    "A+" : 4.5,
    "A0" : 4.0,
    "B+" : 3.5,
    "B0" : 3.0,
    "C+" : 2.5,
    "C0" : 2.0,
    "D+" : 1.5,
    "D0" : 1.0,
    "F" : 0,
}
rl.on('line', function(line) {
    grades.push(line);
}).on('close', function() {
    let totalTime = 0;
    let totalScore = 0;
    for (let i=0; i<grades.length; i++) {
        let row = grades[i].split(" ");
        if (row[2]!="P"){
            totalTime += parseInt(row[1]);
            totalScore += parseInt(row[1]) * scoreBoard[row[2]];
        }
    }
    console.log(totalScore/totalTime);
    process.exit();
})