const readline = require('readline');
const rl = readline.createInterface({ 
    input: process.stdin,
    output: process.stdout 
});

rl.on('line', function(line) {

    var id = line;
    console.log(id+"??!");

    rl.close();
}).on("close", function(){
    process.exit();
});