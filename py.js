function myfunc2(){
    const { spawn } = require('child_process');
    const process = spawn("python3", ["/Users/jaspergilley/Code/pylectron/main.py"])
}
myfunc2()