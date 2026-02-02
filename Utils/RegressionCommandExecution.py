import subprocess
import time

class RegressionCommandExecution:
    def __init__(self):
        pass

    def main(self, cmd):
        print("Regression Log [info]: Time sleep 5 for background maestro execution")
        time.sleep(5)
        print("Regression Log [info]: Time sleep complete for background maestro execution")
        print("Regression Log [info]: Executing Hardening Regression command")
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        try:
            stdout, stderr = process.communicate(timeout=300)
        except subprocess.TimeoutExpired:
            process.kill()
            stdout, stderr = process.communicate()
            print("Regression Log [timeout error]: Process timeout and was killed!")
        if process.returncode == 0:
            print("Regression Log [PASS]: Hardening Regression command successfully executed")
        else:
            print("Regression Log [ERROR]: Hardening Regression command failed!")
        return stdout, stderr, process.returncode
        
        

