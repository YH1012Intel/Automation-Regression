# Automation-Regression

To automate the regression in mode of hardening, mock and qual to reduce human intervention.



Available Feature
--------------------
-> Covers Perspec Maestro and Pytest 

-> Excel checkbox run regression feature 

-> Auto sorting of testcase based on feature and validation_framework for each regression runid 


### RELEASED VERSION
### Version 1.2
In this new version, automation can now organize your test cases by both the validation framework (Pytest and Perspec Maestro) and the feature they covered. Each regression runid is linked to just one framework and one feature, so it’s easier to keep track of what’s being tested. All test cases for Pytest and Perspec Maestro are now included. User can track test cases based on which framework and feature they belong to based on regression runid, making everything easier to manage. Python Environment setup feature available to ensure functionability for every user.

#### Steps to Trigger
1. cd to home directory /nfs/png/disks/png_viceipr_disk001/FalconRun/users/QUAL/Hardening_test/Automation-Regression 
3. python3.11.1 libs/setup_env.py to setup python environment and download required libraries
4. source pyenv/bin/activate.csh and make sure (py_env) shown at terminal
5. can try pip list and check the library version :

          Package         Version
          --------------- -----------
          numpy           2.2.0
          openpyxl        3.1.5
          pandas          2.3.0
          xlsxwriter      3.2.9

7. open ace_testlist_ttlhg4_v1.xlsx in your laptop for better gui view
8. tick for the testcase which required to be triggered in hardening
9. dont forget to SAVE YOUR FILE
10. run python3.11.1 main.py 
11. only regression trigger log result will be saved at /nfs/png/disks/png_viceipr_disk001/FalconRun/users/QUAL/Hardening_test/Hardening/{runid}

### !!!Precaution!!! 
No for now

### VERSION TO BE RELEASE
### Version 1.3
1. Introducing argument parsing mechanism which large number of testcase and group testcase -> An additional script which takes in feature tag as argument to trigger all testcase in input feature tag, or a script which pasting all the testcase to be triggered into a list and run the script
2. Adding capability to select special platform
### Version 1.4
1. Increase automation coverage to config file
### Version 1.5
1. Setup result fetching mechanism for hardening
### Version 1.6
1. Increase coverage to Qual and Mock
### Version 1.7
1. Introducing excel result update for all hardening and qual result. Performing data analysis to scope down number of qual regression trigger. Only testcases that passed with targeted amount of seed triggered will only run in qual weekly run. (IDEA TO MANAGE QUAL REGRESSION NUMBER)

OLD VERSION:
###### Version 1.1
Hardening Regression can now be trigger by automation with excel. Just select with checbox the testcase and trigger the main.py. Testlist will automatically be generated based on excel datasheet. Trigger of hardening regression is fully automated. 
