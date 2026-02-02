import pandas as pd
import openpyxl

class ExcelTestcaseRetrival:
    def __init__(self, testlist_excel):
        self.testlist_excel = testlist_excel
        self.wb = openpyxl.load_workbook(self.testlist_excel)
        self.ws = self.wb.active
        None
    
    def testlist_excel_extract(self):
        testcase_execute_list=[]
        for row in self.ws.iter_rows(min_row=2, values_only=True):
            checkbox = row[0]  
            if checkbox is True:
                data = [row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]]
                testcase_execute_list.append(data)
        return testcase_execute_list

    def testlist_excel_release(self):

        df1 = pd.read_excel(self.testlist_excel)
        with pd.ExcelWriter(self.testlist_excel, engine='xlsxwriter') as writer:
            df1.to_excel(writer, index=False, sheet_name='Sheet1')
            worksheet = writer.sheets['Sheet1']
            # Add autofilter (header is at row 0 in Excel, so use row 0)
            worksheet.autofilter(0, 0, len(df1), len(df1.columns)-1)
            for row_idx in range(1, 1 + len(df1)):
                worksheet.insert_checkbox(row_idx, 0, False)
    
    def main(self):
        #Extract the testcase from excel which checkbox is set to TRUE
        print("Excel Log [info]: Extracting testcase from excel sheet")
        testcase_execute_list = self.testlist_excel_extract()
        print("Excel Log [PASS]: Testcase successfully extracted from excel sheet")
        #Refresh the checbox to false and release the excel
        #Comment now as i dont wanna release and reset again, the function is ald proven functioning
        # print("Excel Log [info]: Refreshing checkbox in excel sheet")
        # self.testlist_excel_release()
        # print("Excel Log [PASS]: Checbox successfully unchecked in excel sheet")
        return testcase_execute_list

# if __name__ == "__main__":
#     script_dir = os.path.dirname(os.path.abspath(__file__))
#     main_folder = os.path.dirname(script_dir)
#     testlist_excel = 'ace_testlist_ttlhg4_perspec_maestro_v1.xlsx'
#     testlist_excel = os.path.join(main_folder, testlist_excel)
    
#     function = ExcelTestcaseRetrival(testlist_excel)
#     testcase_execute_list = function.main()
#     print(testcase_execute_list)
