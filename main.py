
from Utils.ExcelTestcaseRetrival import ExcelTestcaseRetrival
from Utils.TestlistConstructor import TestlistConstructor
from Utils.HardeningCmdSetup import HardeningCmdSetup
from Utils.HardeningOutputFolderConstructor import HardeningOutputFolderConstructor
from Utils.RegressionCommandExecution import RegressionCommandExecution
from Utils.TestcaseArragement import TestcaseArragement
from Utils.ConfigFileGenerator import ConfigFileGenerator

import argparse
from datetime import datetime
import os
import shutil
import sys
import pandas as pd


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

def VolumeHardeningOutputFolderConstructor(advanced_testcase_execute_list, home_dir, validation_framework_sp=None, platform=None):
        function_output_folder = HardeningOutputFolderConstructor()
        for feature_testcase in advanced_testcase_execute_list:
            #Create folder to store regression execution
            temporary_output_folder_path = function_output_folder.main(validation_framework, feature_testcase, home_dir, validation_framework_sp, platform)
            #Set the output testlist pyfile directory to output folder
            testlist_output_file = os.path.join(temporary_output_folder_path, 'testlist.py')
            #Set output regression log file directory to output foler
            output_regression_log_file = os.path.join(temporary_output_folder_path, "regression_log.txt")
            #Saved all file directory behind the list
            advanced_testcase_execute_list[feature_testcase].append(temporary_output_folder_path)
            advanced_testcase_execute_list[feature_testcase].append(testlist_output_file)
            advanced_testcase_execute_list[feature_testcase].append(output_regression_log_file)
        return advanced_testcase_execute_list

def format_info_line(label, value, content_width):
    # Format: | Label : Value [spaces to fill up to content_width] |
    return f"| {label:<20}: {str(value):<{content_width - 23}}|"

def format_status_line(label, status):
    padding = max(40 - len(f"{label} [{status}]: "), 0)
    return f"{label}{' ' * padding}[{status}]"

def regression_function(testcase_execute_list, validation_framework, config_testcycle, config_fpga_image, config_system_provisioning, config_maestro, config_maestro_branch, platform=None):
    summary_result = []
    
    for feature_testcase in testcase_execute_list:
        testlist = []
        year, month_num, day_num, hour, minute, second, month_abbr, day_abbr = fetchdaytime() 
        #Simplified to only containing testcase
        simpliflied_testcase_execute_list = testcase_execute_list[feature_testcase][:-3]

        content_width = 60
        print(f"+{'-' * content_width}+")
        print(format_info_line("Validation Framework", validation_framework, content_width))
        print(format_info_line("Feature Testcase", feature_testcase, content_width))
        if platform != None:
            print(format_info_line("Special Platform", platform, content_width))
        print(format_info_line("Starting time",f"{day_abbr} {month_abbr} {day_num} {hour:02d}:{minute:02d}:{second:02d} {year}", content_width))
        for testcase_data in simpliflied_testcase_execute_list:
            print(format_info_line("Testcase", testcase_data[2], content_width))
            testlist.append(testcase_data[2])

        print(f"+{'-' * content_width}+")

        temporary_output_folder_path = testcase_execute_list[feature_testcase][-3]
        testlist_output_file = testcase_execute_list[feature_testcase][-2]
        output_regression_log_file = testcase_execute_list[feature_testcase][-1]
        function_testlist.main(validation_framework, simpliflied_testcase_execute_list, testlist_output_file)

        #### CONFIG FILE
        #Copy the default config file to output folder
        if validation_framework == "perspec_maestro":
            
            config_file = config_perspec_maestro_file 
            config_output_file = os.path.join(temporary_output_folder_path, config_perspec_maestro_file)
            
        elif validation_framework == "pytest":
            config_file = config_pytest_file
            config_output_file = os.path.join(temporary_output_folder_path, config_pytest_file)
        function_config_file = ConfigFileGenerator()
        function_config_file.main(validation_framework, config_output_file, config_testcycle[0], config_fpga_image[0], config_system_provisioning[0], config_maestro[0], config_maestro_branch[0])
        #shutil.copy(os.path.join(home_dir, 'Hardening_Testlist_Directory', config_file) , config_output_file)

        # #Construct Command
        hardening_cmd = function_hardening_cmd.main(len(simpliflied_testcase_execute_list), testlist_output_file, config_output_file, platform)

        # # Run Command
        function_regression_trigger = RegressionCommandExecution()
        stdout, stderr, returncode = function_regression_trigger.main(hardening_cmd, output_regression_log_file)

        # Extract the Runid and rename the output folder to Runid
        hardening_runid = runid_extraction(output_regression_log_file)
        print(f"{format_status_line('Main', 'info')}: RUN ID: {hardening_runid}")
        final_output_folder_path = os.path.join(os.path.dirname(temporary_output_folder_path), hardening_runid)
        os.rename(temporary_output_folder_path, final_output_folder_path)
        
        print(f"{format_status_line('Main', 'info')}: Regression log results are saved in {final_output_folder_path}")

        content_width = 70
        if returncode == 0:
            regression_runid_record(hardening_runid)
            print(f"+{'#' * content_width}+")
            print(f"{' ' * 33}PASS{' ' * 33}")
            print(f"+{'#' * content_width}+")
        else:
            print(f"+{'#' * content_width}+")
            print(f"{' ' * 33}FAIL{' ' * 33}")
            print(f"+{'#' * content_width}+")
        
        if platform == None:
            summary_result.append([None, validation_framework, feature_testcase, testlist, hardening_runid, returncode])
        else:
            summary_result.append([platform, validation_framework, feature_testcase, testlist, hardening_runid, returncode])
    
    return summary_result

def parse_filter_arg(filter_args, parser):

    val_error_flag = True
    filters = {}
    validation_framework_history = ""
    filters["perspec_maestro"] = {}
    filters["perspec_maestro"]["tag"] = []
    filters["perspec_maestro"]["testcase"] = []
    filters["pytest"] = {}
    filters["pytest"]["tag"] = []
    filters["pytest"]["testcase"] = []
    tag_list_pytest = []
    tag_list_perspec_maestro = []
    testcase_list_pytest = []
    testcase_list_perspec_maestro = []
    #Check for items in filter
    for item in filter_args:
        #For item key=value given
        if '=' in item:
            #Split key and value with =
            key, value = item.split('=', 1)
            #Raise error if key= , not given value
            if value == "":
                parser.error(f'--filter {item} is not a valid, key=value pair.')
            #Raise error if key=valuekey=value, no splitting between key=value
            elif '=' in value:
                parser.error(f'--filter {item} is not a valid, space needed between key=value key=value.')
            #Perfect Condition
            else:
                if key=="val" or key == "tag" or key == "config_location":
                    #Raise error if validation framework is not in command
                    if key=="val" and value  not in ["perspec_maestro", "pm", "pytest", "pt"]:
                        parser.error(f'--filter {item} is not a valid, validation_framework "val" only recognise [perspec_maestro, pm, pytest, pt].')
                    else:
                        ## Gold Condition
                        ## Store data
                        if key == "val": 
                            val_error_flag=False
                            if value == "pm": value = "perspec_maestro"
                            elif value == "pt": value = "pytest"
                            validation_framework_history = value
                        else:
                            if validation_framework_history == "pytest":
                                if key == "tag":
                                    if value not in tag_list_pytest:
                                        tag_list_pytest.append(value)
                                elif key == "config_location":
                                    if value not in testcase_list_pytest:
                                        testcase_list_pytest.append(value)
                            elif validation_framework_history == "perspec_maestro":
                                if key == "tag":
                                    if value not in tag_list_perspec_maestro:
                                        tag_list_perspec_maestro.append(value)
                                elif key == "config_location":
                                    if value not in testcase_list_perspec_maestro:
                                        testcase_list_perspec_maestro.append(value)
                #Raise error if key not tag or config_location
                else:
                    parser.error(f'--filter {item} is not a valid, key only recognise [val, tag, config_location].')
        #Raise error if no format of key=value given after --filter
        else:
            parser.error(f'--filter {item} is not a valid, key=value pair.')   
    #Raise error if validation framework is not given
    if val_error_flag == True:
        parser.error(f'--filter val is not a given, validation_framework "val" only recognise [perspec_maestro, pm, pytest, pt]')
    filters["perspec_maestro"]["tag"] = tag_list_perspec_maestro
    filters["perspec_maestro"]["testcase"] = testcase_list_perspec_maestro
    filters["pytest"]["tag"] = tag_list_pytest
    filters["pytest"]["testcase"] = testcase_list_pytest
    return filters

def regression_runid_record(runid):
    home_dir = os.getcwd()
    csv_file = os.path.join(os.path.dirname(home_dir),'Regression_Result','Running_Regression_RUNID.csv')
    new_row = pd.DataFrame({'runid': [runid]})
    new_row.to_csv(csv_file, mode='a', header=False, index=False)


if __name__ == "__main__":

    content_width = 78
    print(f"#{'=' * content_width}#")
    print(f"|{' ' * content_width}|")
    print("|", " "*27, "AUTOMATION REGRESSION", " "*26, "|")
    print(f"|{' ' * content_width}|")
    print(f"|{'=' * content_width}|")
    
    home_dir = os.getcwd()

    #Input file 
    testlist_excel = os.path.join(home_dir, 'ace_testlist_ttlhg4_v1_1.xlsx')
    config_perspec_maestro_file = "ace_config_qual_ttlhg4.py"
    config_pytest_file = "ace_pytest_qual_config_ttlhg4.py"

    testcycle = "uv2VVD"
    fpga_image = "drop3build0v62021"
    #system_provisioning = "sonora_fec"
    system_provisioning = "default"

    #Argument Parsing section
    parser = argparse.ArgumentParser(description="Automation Hardening Regression Script")

    parser.add_argument(
                        '--filter',
                        nargs='+',
                        help='Filter (required if trigger is "argument"): "val=..." and ("tag=..." and/or "config_location=...")'
                        )
    parser.add_argument(
                        '-tc', '--testcycle',
                        nargs='+',
                        help='Testcycle (required if trigger is "argument"): "-tc <<testcycle>> (uv2VVD, uv2IPC, fvVVD, fvIPC)"'
                        )
    parser.add_argument(
                        '-fi', '--fpga_image',
                        nargs='+',
                        help='FPGA image (required if trigger is "argument"): "-fi <<fpga image>> (Can refer to libs/config_file.json for more info)"'
                        )
    parser.add_argument(
                        '-sp', '--system_provisioning',
                        nargs='+',
                        help='System Provisioning (can be ignored if no extra system provisioning to set): "-sp <<system provisioning>> (Can refer to libs/config_file.json for more info)"'
                        )
    parser.add_argument(
                        '--maestro',
                        nargs='+',
                        help='System Provisioning (only be used for perspec maestro for choosing maestro side branch or maestro repo): "--maestro <<maestro side branch or maestro repo>> (Can refer to libs/config_file.json for more info)"'
                        )
    parser.add_argument(
                        '--maestro_branch',
                        nargs='+',
                        help='System Provisioning (only be used for perspec maestro branch or repo name): "--maestro_branch <<maestro branch>> (Can refer to libs/config_file.json for more info)"'
                        )
    args = parser.parse_args()
    
    ## Main Flow ##

    #Inputs processing
    #Argument Parsing Input
    if args.testcycle:
        config_testcycle = args.testcycle
    else:
        parser.error(f'--tc val is not a given, testcycle needed (uv2VVD, uv2IPC, fvVVD, fvIPC)')
    if args.fpga_image:
        config_fpga_image = args.fpga_image
    else:
        config_fpga_image = ["default"]
    if args.system_provisioning:
        config_system_provisioning = args.system_provisioning
    else:
        config_system_provisioning = ["default"]
    if args.maestro:
        config_maestro = args.maestro
    else:
        config_maestro = ["maestro_github_remote_side_branch"]
    if args.maestro_branch:
        config_maestro_branch = args.maestro_branch

    else:
        config_maestro_branch = ["default"]
    if args.filter:
        print(f"{format_status_line('Main', 'info')}: Accepted argument parsing inputs")
        argument_filtered_testcase = parse_filter_arg(args.filter, parser)
        excel_function = ExcelTestcaseRetrival(testlist_excel)
        testcase_execute_list = excel_function.main_argument(argument_filtered_testcase)
    #Excel Checkbox Input
    else:
        print(f"{format_status_line('Main', 'info')}: No argument parsing inputs detected, proceeds with checking for excel checkbox inputs")
        #Extract testcase
        excel_function = ExcelTestcaseRetrival(testlist_excel)
        testcase_execute_list = excel_function.main_excel()

    #Raise error and exit system if no argument and excel checkbox detected
    if len(testcase_execute_list) == 0:
        print(f"{format_status_line('Main', 'FAIL')}: No argument parsing inputs detected, No excel checkbox inputs detected")
        print(f"{format_status_line('Main', 'info')}: Exiting Automation Regression Script")
        sys.exit()

    function_testcase = TestcaseArragement()
    advanced_testcase_execute_list = function_testcase.main(testcase_execute_list)

    function_testlist = TestlistConstructor(home_dir)
    function_hardening_cmd = HardeningCmdSetup(home_dir)

    summarize_list = []

    #Feature Level
    for validation_framework in advanced_testcase_execute_list:

        #Perspec Maestro and Pytest
        if validation_framework == "perspec_maestro" or validation_framework == "pytest":

            #Testcase
            for feature_testcase in advanced_testcase_execute_list[validation_framework]:
                
                advanced_testcase_execute_list[validation_framework][0] = VolumeHardeningOutputFolderConstructor(advanced_testcase_execute_list[validation_framework][0], home_dir)
            
            summary_result = regression_function(advanced_testcase_execute_list[validation_framework][0], validation_framework, config_testcycle, config_fpga_image, config_system_provisioning, config_maestro, config_maestro_branch)
            for summary_data in summary_result: summarize_list.append(summary_data)
            

        #Special Platform
        elif validation_framework == "special_platform":

            #Platform Number
            for platform in advanced_testcase_execute_list[validation_framework][0]:

                #Perspec Maestro and Pytest
                for validation_framework_sp in advanced_testcase_execute_list[validation_framework][0][platform]:

                    #Testcase
                    advanced_testcase_execute_list[validation_framework][0][platform][validation_framework_sp] = VolumeHardeningOutputFolderConstructor(advanced_testcase_execute_list[validation_framework][0][platform][validation_framework_sp], home_dir, validation_framework_sp, platform)

                    summary_result = regression_function(advanced_testcase_execute_list[validation_framework][0][platform][validation_framework_sp], validation_framework_sp, config_testcycle, config_fpga_image, config_system_provisioning, config_maestro, config_maestro_branch, platform=platform)
                    for summary_data in summary_result: summarize_list.append(summary_data)
            

    #Summary
    content_width = 78
    print(f"#{'=' * content_width}#")
    print(f"|{' ' * content_width}|")
    print("|", " "*27, "Summarize_regression", " "*27, "|")
    print("|", " "*20, "="*34, " "*20, "|")
    print("|", " "*30, "              ", " "*30, "|")
    count = 1
    for summary_data in summarize_list:
        #print("summary_Data" , summary_data)
        print(format_info_line("Regression Number", count, content_width))
        if summary_data[0] != None:
            print(format_info_line("Special Platform", summary_data[0], content_width))
        print(format_info_line("Validation Framework", summary_data[1], content_width))
        print(format_info_line("Feature", summary_data[2], content_width))
        for testcase in summary_data[3]:
            print(format_info_line("Testcase", testcase, content_width))
        if summary_data[4] != None:
            print(format_info_line("RUNID", summary_data[4], content_width))
        else:
            print(format_info_line("RUNID", "None", content_width))
        print(format_info_line("Regression Result", "PASS" if summary_data[5] == 0 else "FAIL", content_width))
        print("|",  "="*76, "|")
        print("|",  " "*76, "|")
        count += 1
    print(f"|{' ' * content_width}|")
    print(f"|{'=' * content_width}|")
        