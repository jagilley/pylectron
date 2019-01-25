const { spawn } = require('child_process');
const process = spawn("python3", ["/Users/jaspergilley/Code/pylectron/setup.py"])

process.stdout.on('data', (data) => {
    console.log(`stdout: ${data}`);
  });
  
process.stderr.on('data', (data) => {
console.log(`stderr: ${data}`);
});
  
process.on('close', (code) => {
console.log(`child process exited with code ${code}`);
});