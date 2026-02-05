
class TestcaseArragement:
    def __init__(self):
        self.perspec_maestro = "perspec_maestro"
        self.pytest = "pytest"
        self.special_platform = "special_platform"

    def main(self, testcase_execute_list):
        dict_list = {}
        dict_list[self.perspec_maestro] = []
        dict_list_perspec_maestro = dict_list[self.perspec_maestro]
        dict_list[self.pytest] = []
        dict_list_pytest = dict_list[self.pytest]
        dict_list[self.special_platform] = []
        dict_list_special_platform = dict_list[self.special_platform]
        groups_pm = {}
        groups_pt = {}
        groups_sp = {}
        
        #Iterate for each testcase in excel list
        for testcase_data in testcase_execute_list:
            
            #Perspec Maestro condition
            if testcase_data[0] == self.perspec_maestro:

                #Special Platform condition
                if testcase_data[9] != None:
                    platform_number = testcase_data[9]
                    val_framework = testcase_data[0]
                    feature = testcase_data[1]
                    if platform_number not in groups_sp:
                        groups_sp[platform_number] = {}
                        groups_sp[platform_number][val_framework] = {}
                        groups_sp[platform_number][val_framework][feature] = []
                    else:
                        if val_framework not in groups_sp[platform_number]:
                            groups_sp[platform_number][val_framework] = {}
                            groups_sp[platform_number][val_framework][feature] = []
                    if feature not in groups_sp[platform_number][val_framework]:           
                        groups_sp[platform_number][val_framework][feature] = []
                    groups_sp[platform_number][val_framework][feature].append(testcase_data)

                #Normal condition
                else:
                    feature = testcase_data[1]
                    if feature not in groups_pm:
                        groups_pm[feature] = []
                    groups_pm[feature].append(testcase_data)

            #Pytest condition
            elif testcase_data[0] == self.pytest:

                #Special Platform condition
                if testcase_data[6] != None:
                    platform_number = testcase_data[6]
                    val_framework = testcase_data[0]
                    feature = testcase_data[1]
                    if platform_number not in groups_sp:
                        groups_sp[platform_number] = {}
                        groups_sp[platform_number][val_framework] = {}
                        groups_sp[platform_number][val_framework][feature] = []
                    else: 
                        if val_framework not in groups_sp[platform_number]:
                            groups_sp[platform_number][val_framework] = {}
                            groups_sp[platform_number][val_framework][feature] = []
                            
                    if feature not in groups_sp[platform_number][val_framework]:    
                        groups_sp[platform_number][val_framework][feature] = []
                    groups_sp[platform_number][val_framework][feature].append(testcase_data)
                
                #Normal condition
                else:
                    feature = testcase_data[1]  
                    if feature not in groups_pt:
                        groups_pt[feature] = []
                    groups_pt[feature].append(testcase_data)

        dict_list_perspec_maestro.append(groups_pm)
        dict_list_pytest.append(groups_pt)
        dict_list_special_platform.append(groups_sp)

        return dict_list
