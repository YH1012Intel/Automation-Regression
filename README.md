# Automation-Regression

This automation project streamlines regression testing in hardening, mock, and qualification modes, significantly reducing manual intervention. The solution leverages Excel-based test selection and automated scripting to organize, trigger, and track regression runs efficiently.



Available Feature
--------------------
->Excel-driven test case selection and automated regression triggering

->Automated categorization by validation framework (Pytest or Perspec Maestro) and feature

->Comprehensive test coverage for Pytest and Perspec Maestro

->Semi-automated Python environment setup

->Special platform selection for individual test cases via Excel dropdown

->Summarized regression trigger results by framework, platform, feature, test case, run ID, and result

->Argument parsing to trigger automation by feature tag, test case list, or both



## NEW RELEASED VERSION

#### Version 1.3.2

#### • Argument Parsing Mechanism:

Introduced an argument parsing mechanism that allows users to trigger the automation script by specifying a feature tag, a list of test cases, or both as input arguments. This enhancement streamlines the workflow by reducing the manual effort of selecting test cases via checkboxes in Excel, especially when dealing with a large number of test cases. The automation script will automatically identify and execute all relevant test cases based on the provided feature tag. For scenarios involving a small number of test cases, argument parsing offers a more efficient alternative to manual selection, further minimizing repetitive tasks. Combining feature tags and specific test cases as arguments provides greater flexibility and efficiency compared to the traditional checkbox method.

## Steps to Trigger
AS there are some required external python libraries and different python libraries versions, would required to setup python evironment before executing the automation regression. Please follow the detailed guidelines for python environment setup below. To deactivate the python environment, detailed steps provided at end of the section.

There are two methods of execution: Excel Checkbox and Argument Parsing:

Excel Checkbox prefered for user which would need to search for the testcase naming to be executed, or large number of separated feature's testcases

Argument Parsing prefered for user which have their testcase's naming ready or full feature testcase execution
## Python Environment Setup
1. CD to Automation Regression home directory
   
          cd /nfs/png/disks/png_viceipr_disk001/FalconRun/users/QUAL/Hardening_test/Automation-Regression
   
2. Setup python environment and download required libraries

          python3.11.1 libs/setup_env.py
3. Source python environement and make sure (py_env) shown at terminal

          source pyenv/bin/activate.csh
4. Can try pip list and check the library version :

          pip list


          Package         Version
          --------------- -----------
          numpy           2.2.0
          openpyxl        3.1.5
          pandas          2.3.0
          xlsxwriter      3.2.9

## Excel CheckBox
1. Open ace_testlist_ttlhg4_v1.xlsx in your laptop for better gui view
2. Tick for the testcase which required to be triggered in hardening
3. Dont forget to SAVE YOUR FILE
4. Run  main.py

          python3.11.1 main.py
5. Only regression trigger log result will be saved at /nfs/png/disks/png_viceipr_disk001/FalconRun/users/QUAL/Hardening_test/Hardening/{runid}

## Argument Parsing
#### • Argument format :
Run the python main file with arguments input and regression trigger log result will be saved at /nfs/png/disks/png_viceipr_disk001/FalconRun/users/QUAL/Hardening_test/Hardening/{runid}. 

More information of argument parsing format can refer examples given below.

         python3.11.1 main.py --filter val=validation_framework tag=feature_tag config_location=testcase_name


#### • Inputs required for argument parsing:

Validation_framework -> perspec_maestro or pm for perspec maestro, pytest or py for pytest

Feature_tag -> feature tag's naming of testcase 

Config_location -> testcase naming


#### • Example method of argument parsing:

Example 1 (basic method tag input) [takes in 1 validation_framework and 1 tag]: Will triger all the testcase under feature_tag_1 with validation_framework_1

      python3.11.1 main.py --filter val=validation_framework_1 tag=feature_tag_1 
Example 2 (basic method testcase input) [takes in 1 validation_framework and 1 testcase]: Will triger testcase_name_1 with validation_framework_1

      python3.11.1 main.py --filter val=validation_framework_1 config_location=testcase_name_1 
Example 3 (multiple tag inputs) [takes in 1 validation_framework and 2 tag]: Will triger all the testcase under feature_tag_1 and feature_tag_2 with validation_framework_1

      python3.11.1 main.py --filter val=validation_framework_1 tag=feature_tag_1 tag=feature_tag_2
Example 4 (multiple testcase inputs) [takes in 1 validation_framework and 1 testcase]: Will triger testcase_name_1 and testcase_name_2 with validation_framework_1

      python3.11.1 main.py --filter val=validation_framework_1 config_location=testcase_name_1 config_location=testcase_name_2
Example 5 (dual method inputs) [takes in 1 validation_framework and 1 testcase and 1 tag]: Will triger testcase_name_1 and all the testcase under feature_tag_1 with validation_framework_1

      python3.11.1 main.py --filter val=validation_framework_1 config_location=testcase_name_1 tag=feature_tag_1
Example 6 (dual method inputs with different validation framework) [takes in 2 validation_framework and 2 testcase and 2 tag]: Will triger testcase_name_1 and all the testcase under feature_tag_1 with validation_framework_1, and testcase_name_2 and all the testcase under feature_tag_2 with validation_framework_2

      python3.11.1 main.py --filter val=validation_framework_1 config_location=testcase_name_1 tag=feature_tag_1 val=validation_framework_2 config_location=testcase_name_2 tag=feature_tag_2

## Deactivate the Python Environment
10. To deactivate the python environment whenever not to be use
    
         deactivate

## !!!Precaution!!! 
Excel Refresh is disable for now as project is still under testrun

## VERSION TO BE RELEASE
### Version 1.4
1. Increase automation coverage to config file
### Version 1.5
1. Setup result fetching mechanism for hardening
### Version 1.6
1. Increase coverage to Qual and Mock
### Version 1.7
1. Introducing excel result update for all hardening and qual result. Performing data analysis to scope down number of qual regression trigger. Only testcases that passed with targeted amount of seed triggered will only run in qual weekly run. (IDEA TO MANAGE QUAL REGRESSION NUMBER)

## RELEASED VERSION:
### Version 1.3.1.2
#### • Special Platform Feature:

Users can now specify special platform requirements for individual test cases directly in the Excel sheet using a dropdown menu. The automation script identifies and sorts these test cases, triggering them with a dedicated regression command for special platforms.

#### • Summarize Regression Trigger Result Feature:

Automation Script will summarize based on Validation Framework, Special Platform Request, Feature Tags, Testcases, Runid and Trigger Result (PASS, FAIL).

#### Version 1.2

#### • Framework & Feature Organization:

Automation now categorizes test cases by validation framework (Pytest or Perspec Maestro) and by feature. Each regression run is associated with a single framework and feature, simplifying tracking and management.

#### • Comprehensive Test Coverage:

All test cases for Pytest and Perspec Maestro are included.

#### • Python Environment Setup:

Automated environment setup ensures consistent functionality for all users.

#### Version 1.1

#### • Excel-Driven Hardening Regression:

Users can select test cases via checkboxes in Excel and trigger automated regression runs using main.py. The test list is generated from the Excel datasheet, making the hardening regression process fully       automated.


