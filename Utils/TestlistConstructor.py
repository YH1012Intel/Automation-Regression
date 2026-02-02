import json
import random
# from ExcelTestcaseRetrival import ExcelTestcaseRetrival

class TestlistConstructor:
    def __init__(self, json_file, testlist_template_txt, testlist_output_file):

        self.json_file = json_file
        self.testlist_output_file = testlist_output_file
        self.testlist_template_txt = testlist_template_txt

    def testline_cmd_extra_content_extraction(self, argument_type, testcase):

        # Load JSON file
        with open(self.json_file, 'r') as file:
            data = json.load(file)
        data = data[argument_type]
        matching_keys = None
        # Find all testcases where testcase list contains the testcase
        for key, value in data.items():
            if testcase in value["testcase"]:
                matching_keys = key
        return(matching_keys)

    def argument_presetup_json_cmd_extraction(self, testline_argument_presetup_list):

        def extraction_setup_cmd(arugment_presetup):
            with open(self.json_file, 'r') as file:
                data = json.load(file)
            
            for section in data.values():
                if isinstance(section, dict):
                    for key, value in section.items():
                        if arugment_presetup == key:
                            return value.get('cmd')
            return None

        testline_argument_presetup_list = list(set(testline_argument_presetup_list))
        testline_argument_presetup_cmd_list =[]
        for arugment_presetup in testline_argument_presetup_list:
            arugment_presetup_cmd = extraction_setup_cmd(arugment_presetup)
            if '"' in arugment_presetup_cmd:
                arugment_presetup_cmd = arugment_presetup_cmd.replace('"', '\\"')
            testline_argument_presetup_cmd_list.append([arugment_presetup, arugment_presetup_cmd])
        
        return testline_argument_presetup_cmd_list

    def testline_constructor(self, testlist_excel_data):
        argument_presetup_list =[]
        ### Perspec Maestro Testline Construction ###
        if testlist_excel_data[0] == 'perspec_maestro':
            # Construct args portion
            if testlist_excel_data[7] == None and testlist_excel_data[8] == None:
                args = [{'content_location':f'{testlist_excel_data[5]}', 'maestro_tags': 'maestro_tags', 'perspec_files': 'perspec_files', 'perspec_args': 'perspec_args', 'perspec_seed': int(random.randint(0,100000)), 'perspec_seed_count': int(testlist_excel_data[3]), 'maestro_seed_count': int(testlist_excel_data[4])}]
            elif testlist_excel_data[7] != None and testlist_excel_data[8] == None:
                args = [{'content_location':f'{testlist_excel_data[5]}', 'maestro_tags': 'maestro_tags', 'perspec_files': 'perspec_files', 'perspec_args': 'perspec_args', 'perspec_seed': int(random.randint(0,100000)), 'perspec_seed_count': int(testlist_excel_data[3]), 'maestro_seed_count': int(testlist_excel_data[4]), 'plat': str('plat')}]
            elif testlist_excel_data[7] != None and testlist_excel_data[8] != None:
                args = [{'content_location':f'{testlist_excel_data[5]}', 'maestro_tags': 'maestro_tags', 'perspec_files': 'perspec_files', 'perspec_args': 'perspec_args', 'perspec_seed': int(random.randint(0,100000)), 'perspec_seed_count': int(testlist_excel_data[3]), 'maestro_seed_count': int(testlist_excel_data[4]), 'plat': str('plat'), 'plat_csv': str('plat_csv')}]

            # Construct whole testline 
            testline_cmd = f"{testlist_excel_data[2]} = {{'job': '{testlist_excel_data[2]}', 'type': 'perspec_maestro', 'feature_list' :['{testlist_excel_data[6]}'], 'args': {args}}}"
            #print(cmd)
            
            if "'content_location': " in testline_cmd:
                testline_cmd = testline_cmd.replace("'content_location': ", "'content_location': r")
            if "'maestro_tags': 'maestro_tags'" in testline_cmd:
                testline_cmd = testline_cmd.replace("'maestro_tags': 'maestro_tags'", "'maestro_tags': maestro_tags")
            if "'perspec_files': 'perspec_files'" in testline_cmd:
                json_matchkey = self.testline_cmd_extra_content_extraction("perspec_files", testlist_excel_data[2])
                if json_matchkey == None:
                    #print("Keys containing", testlist_excel_data[1], "in list_a:", matching_keys1)
                    testline_cmd = testline_cmd.replace("'perspec_files': 'perspec_files'", "'perspec_files': perspec_files")
                else:
                    #print("Keys containing", testlist_excel_data[1], "in list_a:", matching_keys1)
                    testline_cmd = testline_cmd.replace("'perspec_files': 'perspec_files'", f"'perspec_files': {json_matchkey}")
                    argument_presetup_list.append(json_matchkey)
            if "'perspec_args': 'perspec_args'" in testline_cmd:
                json_matchkey = self.testline_cmd_extra_content_extraction("perspec_args", testlist_excel_data[2])
                if json_matchkey == None:
                    #print("Keys containing", testlist_excel_data[1], "in list_a:", matching_keys1)
                    testline_cmd = testline_cmd.replace("'perspec_args': 'perspec_args'", "'perspec_args': perspec_args")
                else:
                    #print("Keys containing", testlist_excel_data[1], "in list_a:", matching_keys1)
                    testline_cmd = testline_cmd.replace("'perspec_args': 'perspec_args'", f"'perspec_args': {json_matchkey}")
                    argument_presetup_list.append(json_matchkey)
            if "'plat': 'plat'" in testline_cmd:
                json_matchkey = self.testline_cmd_extra_content_extraction("plat", testlist_excel_data[2])
                if json_matchkey == None:
                    #print("Keys containing", testlist_excel_data[1], "in list_a:", matching_keys1)
                    testline_cmd = testline_cmd.replace("'plat': 'plat'", "'plat': plat")
                else:
                    #print("Keys containing", testlist_excel_data[1], "in list_a:", matching_keys1)
                    testline_cmd = testline_cmd.replace("'plat': 'plat'", f"'plat': {json_matchkey}")
                    argument_presetup_list.append(json_matchkey)
            if "'plat_csv': 'plat_csv'" in testline_cmd:
                json_matchkey = self.testline_cmd_extra_content_extraction("plat_csv", testlist_excel_data[2])
                if json_matchkey == None:
                    #print("Keys containing", testlist_excel_data[1], "in list_a:", matching_keys1)
                    testline_cmd = testline_cmd.replace("'plat_csv': 'plat_csv'", "'plat_csv': plat_csv")
                else:
                    #print("Keys containing", testlist_excel_data[1], "in list_a:", matching_keys1)
                    testline_cmd = testline_cmd.replace("'plat_csv': 'plat_csv'", f"'plat_csv': {json_matchkey}")
                    argument_presetup_list.append(json_matchkey)
            
            return testline_cmd, argument_presetup_list, testlist_excel_data[2]

    def testlist_constructor(self, testline_argument_presetup_cmd_list, testline_command_list, testline_executed_list):
        with open(self.testlist_template_txt, 'r') as read_file, open(self.testlist_output_file, 'w') as write_file:
            
            # Writing Top Template of testline py file
            for line in read_file:
                write_file.write(line)

            # Spacing
            write_file.write('\n')

            # Writing presetup argument
            for presetup_argument in testline_argument_presetup_cmd_list:
                argument_name, argument_cmd = presetup_argument
                write_file.write(f"{argument_name} = {argument_cmd}\n")
            
            # Spacing
            write_file.write('\n')

            # Writing testline command 
            for testline_command in testline_command_list:
                write_file.write(f"{testline_command}\n")

            # Double Spacing
            write_file.write("\n\n")

            # Writing Testcase into the list of TESTLINES_TO_BE_EXECUTE
            write_file.write(f"TESTLINES_TO_BE_EXECUTE = [")
            for testcase in testline_executed_list:
                write_file.write(f"{testcase}, ")
            write_file.write(f"]")

    def main(self, testcase_execute_list):

        testline_command_list = []
        testline_argument_presetup_list = []
        testline_executed_list = []

        #For each testcase in the list, construct the testline command
        print("Testlist Construction Log [info]: Constructing Testline commands")
        for testcase_data in testcase_execute_list:
            testline_cmd, argument_presetup_list, testcase = self.testline_constructor(testcase_data)
            testline_command_list.append(testline_cmd)
            testline_executed_list.append(testcase)
            for arugment_presetup_variable in argument_presetup_list:
                testline_argument_presetup_list.append(arugment_presetup_variable)
        print("Testlist Construction Log [PASS]: Testline commands sucessfully constructed")
        
        #Extract the argument presetup command from json
        print("Testlist Construction Log [info]: Extracting Presetup Argument")
        testline_argument_presetup_cmd_list = self.argument_presetup_json_cmd_extraction(testline_argument_presetup_list)
        print("Testlist Construction Log [PASS]: Presetup Argument successfully extracted")

        #Construct the testline.py
        print("Testlist Construction Log [info]: Constructing Testlist Python file")
        self.testlist_constructor(testline_argument_presetup_cmd_list, testline_command_list, testline_executed_list)
        print("Testlist Construction Log [PASS]: Testlist Python file successfully constructed")

# if __name__ == "__main__":
#     testlist_excel = 'ace_testlist_ttlhg4_perspec_maestro_v1.xlsx'
#     presetup_argument_json_file = 'argument_presetup.json'
#     testline_template_txt = 'ace_testlist_ttlhg4_template.txt'
#     testlist_output_file = 'testlist_3.py'
#     excel_function = ExcelTestcaseRetrival(testlist_excel)
#     testcase_execute_list = excel_function.main()
#     function = TestlistConstructor( presetup_argument_json_file, testline_template_txt, testlist_output_file)
#     function.main(testcase_execute_list)

        

