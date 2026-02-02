# Automation-Regression
To automate the regression in mode of hardening, mock and qual to reduce human intervention

### RELEASED VERSION
### Version 1.1
Hardening Regression can now be trigger by automation with excel. Just select with checbox the testcase and trigger the main_excel_method.py. Testlist will automatically be generated based on excel datasheet. Trigger of hardening regression is fully automated. 

#### Steps to Trigger
1. cd to /nfs/png/disks/png_viceipr_disk001/FalconRun/users/QUAL/Hardening_test/Automation-Regression
2. run python3.11.1 main_excel_method.py
3. only regression trigger log result will be saved at /nfs/png/disks/png_viceipr_disk001/FalconRun/users/QUAL/Hardening_test/Hardening/{runid}

### !!!Precaution!!! 
Please do not run for now as the required python library version is still not being imported and will not able to run
Required scripts to fetch required python library for the automation process thus not affecting the vnc session
Version 1.1 now only support perspec maestro without pytest (will be released in version 1.2)

### VERSION TO BE RELEASE
### Version 1.2
1. Increase coverage to pytest
2. Provide libs to fetch required python library version
### Version 1.2
1. Introducing argument parsing mechanism which large number of testcase and group testcase -> An additional script which takes in feature tag as argument to trigger all testcase in input feature tag, or a script which pasting all the testcase to be triggered into a list and run the script
### Version 1.3
3. Increase automation coverage to config file
### Version 1.4
1. Setup result fetching mechanism for hardening
### Version 1.5
1. Increase coverage to Qual and Mock
### Version 1.6
1. Introducing excel result update for all hardening and qual result. Performing data analysis to scope down number of qual regression trigger. Only testcases that passed with targeted amount of seed triggered will only run in qual weekly run. (IDEA TO MANAGE QUAL REGRESSION NUMBER)

