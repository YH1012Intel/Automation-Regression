from Utils.ExcelTestcaseRetrival import ExcelTestcaseRetrival
from Utils.TestlistConstructor import TestlistConstructor
from Utils.HardeningCmdSetup import HardeningCmdSetup
from Utils.RegressionCommandExecution import RegressionCommandExecution

if __name__ == "__main__":

    # Input file 
    testlist_excel = 'ace_testlist_ttlhg4_v1.xlsx'
    presetup_argument_json_file = '/nfs/png/disks/png_viceipr_disk001/FalconRun/users/QUAL/Hardening_test/Automation-Regression/Library/argument_presetup.json'
    testline_template_txt = '/nfs/png/disks/png_viceipr_disk001/FalconRun/users/QUAL/Hardening_test/Automation-Regression/Library/ace_testlist_ttlhg4_template.txt'
    regression_command_json = '/nfs/png/disks/png_viceipr_disk001/FalconRun/users/QUAL/Hardening_test/Automation-Regression/Library/regression_command.json'
    config_file = "ace_config_qual_ttlhg4.py"

    # Output file
    testlist_output_file = 'testlist.py'

    ## Main Flow ##
    #Extract testcase
    excel_function = ExcelTestcaseRetrival(testlist_excel)
    testcase_execute_list = excel_function.main()
    #print(testcase_execute_list)

    #Construct Testlist
    function = TestlistConstructor( presetup_argument_json_file, testline_template_txt, testlist_output_file)
    function.main(testcase_execute_list)

    #Construct Command
    function_hardening_cmd = HardeningCmdSetup(testlist_output_file, regression_command_json, config_file)
    hardening_cmd = function_hardening_cmd.main(len(testcase_execute_list))
    # print(hardening_cmd)

    #Run Command
    # function_regression_trigger = RegressionCommandExecution()
    # stdout, stderr, returncode = function_regression_trigger.main(hardening_cmd)
    # print("Regression Log [info]:")
    # print(stdout)
    # print("Regression Log [error]:")
    # print(stderr)
    # print("Regression Log [errorcode]:", returncode)

