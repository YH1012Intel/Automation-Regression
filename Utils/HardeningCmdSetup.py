# from ExcelTestcaseRetrival import ExcelTestcaseRetrival
# from TestlistConstructor import TestlistConstructor
import json
import os

class HardeningCmdSetup():
    def __init__(self, home_dir):
        self.regression_command_json = os.path.join(home_dir, 'Library', 'regression_command.json') 

    def format_status_line(self, label, status):
        padding = max(40 - len(f"{label} [{status}]: "), 0)
        return f"{label}{' ' * padding}[{status}]"

    def main(self, testcase_amount, testlist_output_file, config_file, platform=None):

        print(f"{self.format_status_line('Hardening Regression CMD Log', 'info')}: Constructing Hardening Regression Command")
        # Read regresison cmd json file data
        with open(self.regression_command_json, 'r') as file:
            json_data_regression = json.load(file)

        # Extract for hardening cmd data
        hardening_regression_cmd_data = json_data_regression['hardening']
        # Extract runci py file path
        runci_pyfile = hardening_regression_cmd_data['runci_pyfile']

        #Normal Condition
        if platform == None:
            # Set for platform amount to be used in this regression max to 8
            platform_amount = testcase_amount if testcase_amount <= 8 else 8
            # Extract excluded platform
            platform_exclude = hardening_regression_cmd_data['platform_exclude']

            platform_cmd = f"-n{platform_amount} --exclude {' '.join(platform_exclude)}"

        #Special Platform condition
        else:
            platform_cmd = f"-s {platform}"

        hardening_cmd = f"python3.11.1 {runci_pyfile} -m hardening -c {config_file} -t {testlist_output_file} {platform_cmd}"

        print(f"{self.format_status_line('Hardening Regression CMD Log', 'CMD')}: {hardening_cmd}")
        print(f"{self.format_status_line('Hardening Regression CMD Log', 'PASS')}: Hardening Regression Command successfully constructed")
        return hardening_cmd.split(" ")



# if __name__ == "__main__":

#     # Input file 
#     testlist_excel = 'ace_testlist_ttlhg4.xlsx'
#     presetup_argument_json_file = 'argument_presetup.json'
#     testline_template_txt = 'ace_testlist_ttlhg4_template.txt'
#     regression_command_json = 'regression_command.json'
#     config_file = "ace_config_qual_TTLHG4.py"

#     # Output file
#     testlist_output_file = 'testlist_2.py'

#     ## Main Flow ##
#     #Extract testcase
#     excel_function = ExcelTestcaseRetrival(testlist_excel)
#     testcase_execute_list = excel_function.main()

#     #Construct Testlist
#     function = TestlistConstructor( presetup_argument_json_file, testline_template_txt, testlist_output_file)
#     function.main(testcase_execute_list)

#     #Construct Command
#     function_hardening_cmd = HardeningCmdSetup(testlist_output_file, regression_command_json, config_file)
#     hardening_cmd = function_hardening_cmd.main(len(testcase_execute_list))
#     print(hardening_cmd)
