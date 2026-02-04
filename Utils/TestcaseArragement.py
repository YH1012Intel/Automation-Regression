
class TestcaseArragement:
    def __init__(self):
        self.perspec_maestro = "perspec_maestro"
        self.pytest = "pytest"

    def main(self, testcase_execute_list):
        dict_list = {}
        dict_list[self.perspec_maestro] = []
        dict_list_perspec_maestro = dict_list[self.perspec_maestro]
        dict_list[self.pytest] = []
        dict_list_pytest = dict_list[self.pytest]
        groups_pm = {}
        groups_pt = {}
        for testcase_data in testcase_execute_list:
            if testcase_data[0] == self.perspec_maestro:
                
                key = testcase_data[1]  # second element
                if key not in groups_pm:
                    groups_pm[key] = []
                groups_pm[key].append(testcase_data)

            elif testcase_data[0] == self.pytest:
                key = testcase_data[1]  # second element
                if key not in groups_pt:
                    groups_pt[key] = []
                groups_pt[key].append(testcase_data)
        
        dict_list_perspec_maestro.append(groups_pm)
        dict_list_pytest.append(groups_pt)

        return dict_list
