# Automation-Regression

This automation project streamlines regression testing in hardening, mock, and qualification modes, significantly reducing manual intervention. The solution leverages Excel-based test selection and automated scripting to organize, trigger, and track regression runs efficiently.



Available Feature
--------------------
-> Covers Perspec Maestro and Pytest 

-> Excel checkbox run regression feature 

-> Auto sorting of testcase based on feature and validation_framework for each regression runid 

-> Ability to trigger with selected special platform


## RELEASED VERSION
### Version 1.3.1
#### • Special Platform Feature:

Users can now specify special platform requirements for individual test cases directly in the Excel sheet using a dropdown menu. The automation script identifies and sorts these test cases, triggering them with a dedicated regression command for special platforms.

## Steps to Trigger
1. CD to Automation Regression home directory
   
          cd /nfs/png/disks/png_viceipr_disk001/FalconRun/users/QUAL/Hardening_test/Automation-Regression
   
2. Setup python environment and download required libraries

          python3.11.1 libs/setup_env.py
3. Source python environement and make sure (py_env) shown at terminal

          pyenv/bin/activate.csh
4. Can try pip list and check the library version :

          pip list


          Package         Version
          --------------- -----------
          numpy           2.2.0
          openpyxl        3.1.5
          pandas          2.3.0
          xlsxwriter      3.2.9

5. Open ace_testlist_ttlhg4_v1.xlsx in your laptop for better gui view
6. Tick for the testcase which required to be triggered in hardening
7. Dont forget to SAVE YOUR FILE
8. Run  main.py

          python3.11.1 main.py
9. Only regression trigger log result will be saved at /nfs/png/disks/png_viceipr_disk001/FalconRun/users/QUAL/Hardening_test/Hardening/{runid}
10. To deactivate the python environment whenever not to be use
    
         deactivate

## !!!Precaution!!! 
No for now

## VERSION TO BE RELEASE
### Version 1.3.2
1. Introducing argument parsing mechanism which large number of testcase and group testcase -> An additional script which takes in feature tag as argument to trigger all testcase in input feature tag, or a script which pasting all the testcase to be triggered into a list and run the script
### Version 1.4
1. Increase automation coverage to config file
### Version 1.5
1. Setup result fetching mechanism for hardening
### Version 1.6
1. Increase coverage to Qual and Mock
### Version 1.7
1. Introducing excel result update for all hardening and qual result. Performing data analysis to scope down number of qual regression trigger. Only testcases that passed with targeted amount of seed triggered will only run in qual weekly run. (IDEA TO MANAGE QUAL REGRESSION NUMBER)

## OLD VERSION:
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


