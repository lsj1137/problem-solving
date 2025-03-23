const readline = require('readline');
const rl = readline.createInterface({ 
    input: process.stdin,
    output: process.stdout 
});

rl.on('line', function(line) {

    var [a,b] = line.split(" ").map(a => parseInt(a));
    console.log(a+b);

    rl.close();
}).on("close", function(){
    process.exit();
});