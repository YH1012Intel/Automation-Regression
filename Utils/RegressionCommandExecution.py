import subprocess
import time

class RegressionCommandExecution:
    def __init__(self):
        pass

    def format_status_line(self, label, status):
        padding = max(40 - len(f"{label} [{status}]: "), 0)
        return f"{label}{' ' * padding}[{status}]"

    def main(self, cmd, output_regression_log_file):
        print(f"{self.format_status_line('Regression Log', 'info')}: Time sleep 5 for background maestro execution")
        time.sleep(5)
        print(f"{self.format_status_line('Regression Log', 'info')}: Time sleep complete for background maestro execution")
        print(f"{self.format_status_line('Regression Log', 'info')}: Executing Hardening Regression command")
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        try:
            stdout, stderr = process.communicate(timeout=300)
        except subprocess.TimeoutExpired:
            process.kill()
            stdout, stderr = process.communicate()
            print("Regression Log [timeout error]: Process timeout and was killed!")
            print(f"{self.format_status_line('Regression Log', 'info')}: Regression log saved to regression_log.txt")
        if process.returncode == 0:
            print(f"{self.format_status_line('Regression Log', 'PASS')}: Hardening Regression command successfully executed")
            print(f"{self.format_status_line('Regression Log', 'info')}: Regression log saved to regression_log.txt")
        else:
            print("Regression Log [ERROR]: Hardening Regression command failed!")
            print(f"{self.format_status_line('Regression Log', 'info')}: Regression log saved to regression_log.txt")

        with open(output_regression_log_file, 'w') as f:
            f.write("STDOUT:\n")
            f.write(stdout)
            f.write("\n\nSTDERR:\n")
            f.write(stderr)
            f.write(f"\n\nRETURNCODE:\n{process.returncode}\n")

        return stdout, stderr, process.returncode
        
        

