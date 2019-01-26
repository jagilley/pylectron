const { spawn } = require('child_process');
const process = spawn("python3", ["-u", "/Users/jaspergilley/Code/pylectron/setup.py"])
/*
process.stdout.on('data', (data) => {
    outputText = `stdout: ${data}`;
    console.log(outputText);
    document.getElementById("outElement").innerHTML = outputText;
  });*/

process.stdout.on('data', function(data) {
    console.log(data.toString());
    document.getElementById("outElement").innerHTML = document.getElementById("outElement").innerHTML + data.toString() + "<br>";
});
  
process.stderr.on('data', (data) => {
    console.log(`stderr: ${data}`);
});
  
process.on('close', (code) => {
    console.log(`child process exited with code ${code}`);
});