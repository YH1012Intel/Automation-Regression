from Utils.ExcelTestcaseRetrival import ExcelTestcaseRetrival
from Utils.TestlistConstructor import TestlistConstructor
from Utils.HardeningCmdSetup import HardeningCmdSetup
from Utils.HardeningOutputFolderConstructor import HardeningOutputFolderConstructor
from Utils.RegressionCommandExecution import RegressionCommandExecution

import os
import shutil

def runid_extraction(output_regression_log_file):
    with open(output_regression_log_file, 'r') as f:
        for line in f:
            if "Run ID  :" in line:
                # Split on "Run ID  :" and take the part after it, then strip whitespace
                return line.split("Run ID  :")[1].strip()
    # If not found, return None or raise an error
    return None


if __name__ == "__main__":

    home_dir = os.getcwd()

    # Input file 
    testlist_excel = os.path.join(home_dir, 'ace_testlist_ttlhg4_v1.xlsx')
    presetup_argument_json_file = os.path.join(home_dir, 'Library', 'argument_presetup.json')
    testline_template_txt = os.path.join(home_dir, 'Library', 'ace_testlist_ttlhg4_template.txt') 
    regression_command_json = os.path.join(home_dir, 'Library', 'regression_command.json') 
    config_file = "ace_config_qual_ttlhg4.py"

    # Output file
    testlist_output_file = 'testlist.py'

    ## Main Flow ##
    #Create folder to store regression execution
    function_output_folder = HardeningOutputFolderConstructor()
    temporary_output_folder_path = function_output_folder.main(home_dir)
    #Set the output testlist pyfile directory to output folder
    testlist_output_file = os.path.join(temporary_output_folder_path, testlist_output_file)
    #Copy the default config file to output folder
    config_output_file = os.path.join(temporary_output_folder_path, config_file)
    shutil.copy(os.path.join(home_dir, 'Hardening_Testlist_Directory', config_file) , config_output_file)
    #Set output regression log file directory to output foler
    output_regression_log_file = os.path.join(temporary_output_folder_path, "regression_log.txt")

    #Extract testcase
    excel_function = ExcelTestcaseRetrival(testlist_excel)
    testcase_execute_list = excel_function.main()
    #print(testcase_execute_list)

    #Construct Testlist
    function = TestlistConstructor( presetup_argument_json_file, testline_template_txt, testlist_output_file)
    function.main(testcase_execute_list)

    #Construct Command
    function_hardening_cmd = HardeningCmdSetup(testlist_output_file, regression_command_json, config_output_file)
    hardening_cmd = function_hardening_cmd.main(len(testcase_execute_list))
    # print(hardening_cmd)

    #Run Command
    function_regression_trigger = RegressionCommandExecution()
    stdout, stderr, returncode = function_regression_trigger.main(hardening_cmd, output_regression_log_file) 
    # print("Regression Log [info]:")
    # print(stdout)
    # print("Regression Log [error]:")
    # print(stderr)
    # print("Regression Log [errorcode]:", returncode)

    #Extract the Runid and rename the output folder to Runid
    hardening_runid = runid_extraction(output_regression_log_file)
    os.rename(temporary_output_folder_path, hardening_runid)
    final_output_folder_path = os.path.join(os.path.dirname(temporary_output_folder_path), hardening_runid)
    print(f"Main [info]: Overall results are saved in {final_output_folder_path}")

