import argparse
import importlib.util
import os
import pandas as pd

class testline_csv_converter:
    def __init__(self):
        
        self.validation_framework_perspec_maestro = "perspec_maestro"
        self.validation_framework_pytest = "pytest"
        self.pytest_namenodes = "--pysv_config=ttlhg4"
    
    def call_testlist(self, testlist_path):

        print("Testlist Construction Log [info]: Importing testcase from testlist pyfile")
        module_name = os.path.splitext(os.path.basename(testlist_path))[0]
        spec = importlib.util.spec_from_file_location(module_name, testlist_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        testlist_variable = vars(module)
        print("Testlist Construction Log [pass]: Testcase from testlist pyfile successfully imported")
        return testlist_variable
    
    def testcase_extraction(self, testlist_variable):
        print("Testlist Construction Log [info]: Extracting Testcase from Excel")
        testcase_array = []
        for var_name, var_value in testlist_variable.items():
            if var_name.startswith('__'):
                continue
            if isinstance(var_value, dict):
                var_list = list(var_value.values())
                validation_framework = var_list[1]

                ### Perspec Maestro ###
                if validation_framework == self.validation_framework_perspec_maestro:
                    feature_tag_testlist = var_list[2][0]
                    args = var_list[-1]
                    args = args[0]
                    content_location = ''
                    if isinstance(args, dict):
                        content_location = args.get('content_location')
                        perspec_seed_count = args.get('perspec_seed_count')
                        maestro_seed_count = args.get('maestro_seed_count')
                        plat = args.get('plat')
                        plat_csv = args.get('plat_csv')
                    if content_location != '':
                        row = [validation_framework, '', var_name, perspec_seed_count, maestro_seed_count, content_location, feature_tag_testlist, plat, plat_csv, '', '', '']
                        testcase_array.append(row)

                ### Pytest ###
                elif validation_framework == self.validation_framework_pytest:
                    args = var_list[-1]
                    args = args[0]
                    content_path = ''
                    if isinstance(args, dict):
                        content_path = args.get('content_path')
                        pytest_args = args.get('pytest_args')
                        pytest_args = pytest_args.replace(self.pytest_namenodes, "")
                        timeout = args.get("timeout")
                    if content_path != '':
                        row = [validation_framework, '', var_name, '', '', '', '', '', '', content_path, pytest_args, timeout]
                        testcase_array.append(row)
                        
        print("Testlist Construction Log [pass]: Testcase from Excel successfully extracted")
        return testcase_array

    def excel_creation(self, testcase_array, xlsx_output_file, mode):
        
        columns = [
            'run_status', 'val_framework', 'feature_tag', 'testcase',
            'perspec_seed_count', 'maestro_seed_count', 'content_location',
            'feature_tag_testlist', 'plat', 'plat_csv', 'content_path', 
            'pytest_args', 'pytest_timeout', 'special_platform'
        ]

        # Insert empty value for run_status in each row
        for row in testcase_array:
            row.insert(0, '')
            row.insert(-1, '')

        df_new = pd.DataFrame(testcase_array, columns=columns)
        file_path = f'{xlsx_output_file}'

        if mode == 'write' or not os.path.exists(file_path):
            print("Testlist Construction Log [info]: Writing testcase into New Excel testlist")
            df_new.to_excel(file_path, index=False)
            print(f"Testlist Construction Log [pass]: Testcase successfully wrote into New Excel testlist: {file_path}")

        elif mode == 'append':
            print("Testlist Construction Log [info]: Appending testcase into Excel testlist")
            df_old = pd.read_excel(file_path)
            df_combined = pd.concat([df_old, df_new], ignore_index=True)
            df_combined.to_excel(file_path, index=False)
            print(f"Testlist Construction Log [pass]: Testcase successfully appendded into Excel testlist: {file_path}")
        else:
            raise ValueError(f"Testlist Construction Log [error]: Mode must be 'append' or 'write' not -> {mode}")


    
    def feature_tag_extraction(self, xlsx_output_file, feature_testcase_file):

        print("Testlist Construction Log [info]: Appending feature into testcase based on pvim feature")
        df1 = pd.read_excel(f'{xlsx_output_file}')
        df2 = pd.read_excel(f'{feature_testcase_file}')

        # Build lookup dictionary from df2: {column B: column A}
        lookup = dict(zip(df2.iloc[:, 1], df2.iloc[:, 0]))

        # For each row in df1, get column C, look up in df2, and update column B
        def update_column_b(row):
            search_value = row.iloc[3]  # Column C (index 2)
            if search_value in lookup:
                row.iloc[2] = lookup[search_value]  # Update column B (index 1)
            return row

        df1 = df1.apply(update_column_b, axis=1)
        print("Testlist Construction Log [pass]: Feature successfully appendded into testcase based on pvim feature")

        print("Testlist Construction Log [info]: Adding default false checkbox to testcase")
        with pd.ExcelWriter(f'{xlsx_output_file}', engine='xlsxwriter') as writer:
            df1.to_excel(writer, index=False, sheet_name='Sheet1')
            worksheet = writer.sheets['Sheet1']
            # Add autofilter (header is at row 0 in Excel, so use row 0)
            worksheet.autofilter(0, 0, len(df1), len(df1.columns)-1)
            for row_idx in range(1, 1 + len(df1)):
                worksheet.insert_checkbox(row_idx, 0, False)
        print("Testlist Construction Log [pass]: Default false checkbox successfully added to testcase")

    def main(self):
        parser = argparse.ArgumentParser(description="Process testlist.py and feature tag to write/append to output excel testlist.")
        parser.add_argument('-o', '--output_excel', type=str, help='Output EXCEL testlist file directory')
        parser.add_argument('-t', '--input_testlist', type=str, help='Input Testlist file')
        parser.add_argument('-f', '--input_featuretag', type=str, help='Input Feature Tag file')
        parser.add_argument('-m', '--mode', choices=['write', 'append'], help='Mode: write or append')

        args = parser.parse_args()
        xlsx_output_file = args.output_excel
        testlist_path = args.input_testlist
        feature_testcase_file = args.input_featuretag
        mode = args.mode

        print(f"Testlist Construction Log [input]: Output Excel Directory: {xlsx_output_file}")
        print(f"Testlist Construction Log [input]: Input Testlist file: {testlist_path}")
        print(f"Testlist Construction Log [input]: Input Feature Tag file: {feature_testcase_file}")
        print(f"Testlist Construction Log [input]: Mode: {mode}")

        #Import testlist
        testlist_variable = self.call_testlist(testlist_path)

        #Extract testcase from testlist.py
        testcase_array = self.testcase_extraction(testlist_variable)
        
        #Write or Append testcase into Excel
        self.excel_creation(testcase_array, xlsx_output_file, mode)
        
        #Add feature tag from pvim copied into the feature_testcase_file
        #Add default false checkbox
        self.feature_tag_extraction(xlsx_output_file,feature_testcase_file)
        print(f"Testlist Construction Log [pass]: Exported all dictionary variables in the desired format to {xlsx_output_file}")

if __name__ == "__main__":
    function = testline_csv_converter()
    function.main()



# if __name__ == "__main__":
#     function = testline_csv_converter("ace_pytest_qual_testlist_ttlhg4.py")
#     output_xlsx_file = 'ace_testlist_ttlhg4_overall'
#     feature_tag_file = 'featurewithtestcase_pytest'
#     function.main(output_xlsx_file, feature_tag_file, "write")
#     function = testline_csv_converter("ace_testlist_ttlhg4.py")
#     feature_tag_file = 'featurewithtestcase_perspec_maestro'
#     function.main(output_xlsx_file, feature_tag_file, "append")