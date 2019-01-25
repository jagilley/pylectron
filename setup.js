const { spawn } = require('child_process');
const process = spawn("python3", ["/Users/jaspergilley/Code/pylectron/setup.py"])

process.stdout.on('data', (data) => {
    outputText = `stdout: ${data}`;
    console.log(outputText);
    document.getElementById("outElement").innerHTML = outputText;
  });
  
process.stderr.on('data', (data) => {
console.log(`stderr: ${data}`);
});
  
process.on('close', (code) => {
console.log(`child process exited with code ${code}`);
});