
from Utils.ExcelTestcaseRetrival import ExcelTestcaseRetrival
from Utils.TestlistConstructor import TestlistConstructor
from Utils.HardeningCmdSetup import HardeningCmdSetup
from Utils.HardeningOutputFolderConstructor import HardeningOutputFolderConstructor
from Utils.RegressionCommandExecution import RegressionCommandExecution
from Utils.TestcaseArragement import TestcaseArragement

import os
import shutil
from datetime import datetime

def fetchdaytime():
    now = datetime.now()

    year = now.year
    month_num = now.month
    day_num = now.day
    hour = now.hour
    minute = now.minute
    second = now.second
    month_abbr = now.strftime("%b") 
    day_abbr = now.strftime("%a") 

    return year, month_num, day_num, hour, minute, second, month_abbr, day_abbr

def runid_extraction(output_regression_log_file):
    with open(output_regression_log_file, 'r') as f:
        for line in f:
            if "Run ID  :" in line:
                # Split on "Run ID  :" and take the part after it, then strip whitespace
                return line.split("Run ID  :")[1].strip()
    # If not found, return None or raise an error
    return None

def VolumeHardeningOutputFolderConstructor(advanced_testcase_execute_list, home_dir):
        function_output_folder = HardeningOutputFolderConstructor()
        for validation_framework in advanced_testcase_execute_list:
            for feature_testcase in advanced_testcase_execute_list[validation_framework][0]:
                #Create folder to store regression execution
                temporary_output_folder_path = function_output_folder.main(validation_framework, feature_testcase, home_dir)
                #Set the output testlist pyfile directory to output folder
                testlist_output_file = os.path.join(temporary_output_folder_path, 'testlist.py')
                #Set output regression log file directory to output foler
                output_regression_log_file = os.path.join(temporary_output_folder_path, "regression_log.txt")
                #Saved all file directory behind the list
                advanced_testcase_execute_list[validation_framework][0][feature_testcase].append(temporary_output_folder_path)
                advanced_testcase_execute_list[validation_framework][0][feature_testcase].append(testlist_output_file)
                advanced_testcase_execute_list[validation_framework][0][feature_testcase].append(output_regression_log_file)
        return advanced_testcase_execute_list

def format_info_line(label, value, content_width):
    # Format: | Label : Value [spaces to fill up to content_width] |
    return f"| {label:<20}: {str(value):<{content_width - 23}}|"

def format_status_line(label, status):
    padding = max(40 - len(f"{label} [{status}]: "), 0)
    return f"{label}{' ' * padding}[{status}]"

if __name__ == "__main__":

    home_dir = os.getcwd()

    # Input file 
    testlist_excel = os.path.join(home_dir, 'ace_testlist_ttlhg4_v1.xlsx')
    config_perspec_maestro_file = "ace_config_qual_ttlhg4.py"
    config_pytest_file = "ace_pytest_qual_config_ttlhg4.py"
    
    ## Main Flow ##
    
    #Extract testcase
    excel_function = ExcelTestcaseRetrival(testlist_excel)
    testcase_execute_list = excel_function.main()

    function_testcase = TestcaseArragement()
    advanced_testcase_execute_list = function_testcase.main(testcase_execute_list)
    advanced_testcase_execute_list = VolumeHardeningOutputFolderConstructor(advanced_testcase_execute_list,home_dir)
    
    #Iterate based on feature for testlist.py construction and command generation and regression trigger
    function_testlist = TestlistConstructor(home_dir)
    function_hardening_cmd = HardeningCmdSetup(home_dir)
    for validation_framework in advanced_testcase_execute_list:
        #Feature Level
        for feature_testcase in advanced_testcase_execute_list[validation_framework][0]:

            year, month_num, day_num, hour, minute, second, month_abbr, day_abbr = fetchdaytime()
            #Simplified to only containing testcase
            simpliflied_testcase_execute_list = advanced_testcase_execute_list[validation_framework][0][feature_testcase][:-3]

            content_width = 60
            print(f"+{'-' * content_width}+")
            print(format_info_line("Validation Framework", validation_framework, content_width))
            print(format_info_line("Feature Testcase", feature_testcase, content_width))
            print(format_info_line("Starting time",f"{day_abbr} {month_abbr} {day_num} {hour:02d}:{minute:02d}:{second:02d} {year}", content_width))
            for testcase_data in simpliflied_testcase_execute_list:
                print(format_info_line("Testcase", testcase_data[2], content_width))
            print(f"+{'-' * content_width}+")

            #Extract Testlist output file directory
            temporary_output_folder_path = advanced_testcase_execute_list[validation_framework][0][feature_testcase][-3]
            testlist_output_file = advanced_testcase_execute_list[validation_framework][0][feature_testcase][-2]
            output_regression_log_file = advanced_testcase_execute_list[validation_framework][0][feature_testcase][-1]
            function_testlist.main(validation_framework, simpliflied_testcase_execute_list, testlist_output_file)
            
            #### CONFIG FILE
            #Copy the default config file to output folder
            if validation_framework == "perspec_maestro":
                config_file = config_perspec_maestro_file 
                config_output_file = os.path.join(temporary_output_folder_path, config_perspec_maestro_file)
            elif validation_framework == "pytest":
                config_file = config_pytest_file
                config_output_file = os.path.join(temporary_output_folder_path, config_pytest_file)
            shutil.copy(os.path.join(home_dir, 'Hardening_Testlist_Directory', config_file) , config_output_file)

            #Construct Command
            hardening_cmd = function_hardening_cmd.main(len(simpliflied_testcase_execute_list), testlist_output_file, config_output_file)

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
            final_output_folder_path = os.path.join(os.path.dirname(temporary_output_folder_path), hardening_runid)
            os.rename(temporary_output_folder_path, final_output_folder_path)
            print(f"{format_status_line('Main', 'info')}: RUN ID: {hardening_runid}")
            print(f"{format_status_line('Main', 'info')}: Regression log results are saved in {final_output_folder_path}")
            
            if returncode == 0:
                content_width = 70
                print(f"+{'#' * content_width}+")
                print(f"{' ' * 33}PASS{' ' * 33}")
                print(f"+{'#' * content_width}+")
            else:
                print(f"+{'#' * content_width}+")
                print(f"{' ' * 33}FAIL{' ' * 33}")
                print(f"+{'#' * content_width}+")
                
