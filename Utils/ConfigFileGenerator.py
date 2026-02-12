import os
import json

class ConfigFileGenerator:

    def __init__(self):
        home_dir = os.getcwd()
        self.config_json = os.path.join(home_dir, "Library", "config_file.json")
        self.image_location = '/nfs/png/disks/png_coesv_disk001/fpga_images/ACE'

    def json_extraction(self):
        
        with open(self.config_json, 'r') as file:
            data = json.load(file)
        return data
    
    def perspec_maestro_config_file_generator(self, config_file_location, config_dict):
        with open(config_file_location, "w")as f:
            f.write("\n")
            for header in config_dict:
                line = ""
                line += f"{header} = "
                line += "{"
                for info in config_dict[header]:
                    if info in ["ingredient_source", "branch"]:
                        line += f"'{info}': r'{config_dict[header][info][0]}', "
                    elif info in ['ingredient_fpga_image']:
                        line += f"'{info}' : r'{self.image_location + '/' + config_dict[header][info][0] + '/project.conf'}', "
                    elif info in ["ingredient_devices"]:
                        line += f"'{info}': ['{config_dict[header][info][0]}'], "
                    elif info in ["skip_copy", "port_value", "duration", "manifest_args"]:
                        line += f"'{info}': {config_dict[header][info][0]}, "
                    elif info in ["acquire_ingredients", "system_provisioning", "system_discovery", "testline_recovery", "testline_execution", "maestro_workflow_seed_recovery", "setup_settings"]:
                        line += f"'{info}': ["
                        for internal_data in config_dict[header][info][0]:
                            line += f"{internal_data}, "
                        if config_dict[header][info][0]:
                            line = line[:-2]
                        line += f"], "
                    elif info in ["environment_variables"]:
                        line += f"'{info}': "
                        line += "{"
                        for internal_data in config_dict[header][info][0]:
                            
                            line += f"{internal_data}, "
                        line = line[:-2]
                        line += "}, "
                    else:
                        line += f"'{info}': '{config_dict[header][info][0]}', "
                line = line[:-2]
                line += "}"
                
                f.write(f"{line}\n\n")
    
    def pytest_config_file_generator(self, config_file_location, config_dict):

        with open(config_file_location, "w")as f:
            f.write("\n")

            for top in config_dict:
                f.write(f"{top} ")
                f.write("= { \n\n")

                if top == "phases":
                    for header in config_dict[top]:
                        line = ""
                        line += f"'{header}' :\n[\n"       
                        for info in config_dict[top][header]:
                            line += "{"
                            for key, value in  info.items():
                                if key in ['coregroups', 'devices', 'port_value', 'duration']:
                                    line += f"'{key}' : {value},"
                                elif key in ['ingredient_fpga_image']:
                                    line += f"'{key}' : r'{self.image_location + '/' + value + '/project.conf'}',"
                                elif key in ['environment_variables']:
                                    line += f"'{key}' :"
                                    line += "{"
                                    for ev_key, ev_value in value.items():
                                        line += f"'{ev_key}' : r'{ev_value}',"
                                    line = line[:-1]
                                    line += "},"
                                else:
                                    line += f"'{key}' : '{value}',"
                            line = line[:-1]
                            line += "},\n"
                        line = line[:-1]
                        line += "\n"
                        line += "],"
                        f.write(f"{line}\n\n")

                elif top == "CONFIG":
                    line = ""
                    for key, value in config_dict[top].items():
                        if key in ["manifest_args", "environment_variables"]:
                            line += f"'{key}' : {value},\n"
                        else:
                            line += f"'{key}' : '{value}',\n"
                    f.write(f"{line}")
                
                f.write("} \n\n")
            
    def perspec_maestro_config_handler(self, json_data, val_framework, config_dict, header, title_list, description_list):
        config_dict[header] = {}
        for i in range (len(title_list)):
            config_dict[header][title_list[i]] = []
            config_dict[header][title_list[i]].append(json_data[val_framework][header][title_list[i]][description_list[i] if description_list[i] in list(json_data[val_framework][header][title_list[i]]) else None])

    def pytest_config_handler(self, json_data, val_framework, config_dict, top, header, title_list, description_list):
        
        if top == "phases":
            config_dict[top][header] = []
            for i in range (len(title_list)):
                group = {}
                for j in range (len(title_list[i])):
                    group[title_list[i][j]] = {}
                    if title_list[i][j] in ["environment_variables"]:
                        for k in range (len(description_list[i][j])):
                            group[title_list[i][j]][description_list[i][j][k]] = {}
                            group[title_list[i][j]][description_list[i][j][k]] = json_data[val_framework][top][header][i][title_list[i][j]][description_list[i][j][k]]["default" if "default" in list(json_data[val_framework][top][header][i][title_list[i][j]][description_list[i][j][k]]) else None]
                    else:
                        group[title_list[i][j]] = json_data[val_framework][top][header][i][title_list[i][j]][description_list[i][j] if description_list[i][j] in list(json_data[val_framework][top][header][i][title_list[i][j]]) else None]
                config_dict[top][header].append(group)

        elif top == "CONFIG":
            config_dict[top] = {}
            for i in range (len(title_list)):
                config_dict[top][title_list[i]] = json_data[val_framework][top][title_list[i]][description_list[i] if description_list[i] in list(json_data[val_framework][top][title_list[i]]) else None]


    def main(self, val_framework, config_file_location, testcycle, fpga_image, system_provisioning, maestro, maestro_branch):

        json_data = self.json_extraction()

        config_dict = {}
        print("FPGA_IMAGE", fpga_image)
        

        if val_framework == "perspec_maestro":

            # Maestro Repo or Maestro Side Branch only one can be saved
            if maestro == "maestro_github_remote_side_branch":
                self.perspec_maestro_config_handler(json_data, val_framework, config_dict, maestro, ["BB_NAME", "branch"], ["default", maestro_branch])
                print("maestro", maestro, maestro_branch)
            elif maestro == "maestro_repo":
                self.perspec_maestro_config_handler(json_data, val_framework, config_dict, maestro, ["BB_NAME", "ingredient_source", "skip_copy"], ["default", maestro_branch, "default"])

            # Coverage Github Setup
            self.perspec_maestro_config_handler(json_data, val_framework, config_dict, "coverage_github_setup", ["BB_NAME", "database"], ["default", "default"])

            # Haps Programming
            self.perspec_maestro_config_handler(json_data, val_framework, config_dict, "haps_programming", ["BB_NAME", "BB_TAG", "ingredient_fpga_image"], ["default", "default", fpga_image])

            # Sonora Fec
            if system_provisioning != "default":
                self.perspec_maestro_config_handler(json_data, val_framework, config_dict, "sonora_fec", ["BB_NAME", "ingredient_fec_sof_image_1"], ["default", "default"])

            # Power Cycle Sut
            self.perspec_maestro_config_handler(json_data, val_framework, config_dict, "power_cycle_sut", ["BB_NAME", "port_value", "duration"], ["default", "default", "default"])

            # Maestro System Discovery
            self.perspec_maestro_config_handler(json_data, val_framework, config_dict, "maestro_system_discovery", ["BB_NAME", "maestro_tags"], ["default", "default"])

            # Verify FPGA
            self.perspec_maestro_config_handler(json_data, val_framework, config_dict, "verify_fpga", ["BB_NAME", "ingredient_devices"], ["default", "default"])

            # FPGA Perspec Maestro
            self.perspec_maestro_config_handler(json_data, val_framework, config_dict, "fpga_perspec_maestro", ["acquire_ingredients", "system_provisioning", "system_discovery", "testline_recovery", "testline_execution", "maestro_workflow_seed_recovery"], [maestro, system_provisioning, "default", "default", "default", "default"])

            # Config
            self.perspec_maestro_config_handler(json_data, val_framework, config_dict, "CONFIG", ["ip", "project", "val_environment", "val_framework", "hardwareclass", "manifest_type", "manifest_args", "testcycle", "environment_variables", "setup_settings"], ["default", "default", "default", "default", "default", "default", "default", testcycle, "default", "default"])

            # Generate Config File
            self.perspec_maestro_config_file_generator(config_file_location, config_dict)
        
        elif val_framework == "pytest":
            config_dict = {}
            config_dict["phases"] = {}

            self.pytest_config_handler(json_data, val_framework, config_dict, "phases", "system_provisioning", [["BB_NAME","branch", "url", "subdirectory"], ["BB_NAME"], ["BB_NAME"], ["BB_NAME", "coregroups", "devices"],["BB_NAME", "ingredient_fpga_image"], ["BB_NAME"], ["BB_NAME", "port_value", "duration"], ["BB_NAME"], ["BB_NAME"]], [["default", maestro_branch, "default", "default"], ["default"], ["default"], ["default", "default", "default"], ["default", fpga_image], ["default"], ["default", "default", "default"], ["default"], ["default"]])
            self.pytest_config_handler(json_data, val_framework, config_dict, "phases", "testline_execution", [["BB_NAME"], ["BB_NAME"], ["BB_NAME", "port_value", "duration"], ["BB_NAME"], ["BB_NAME", "environment_variables"]], [["default"], ["default"], ["default", "default", "default"], ["default"], ["default", ["PYTHONPATH", "PYSV_PATH"]]])
            self.pytest_config_handler(json_data, val_framework, config_dict, "CONFIG", "", ["ip", "testcycle", "project", "environment", "val_framework", "val_environment", "manifest_args", "hardwareclass", "environment_variables", "manifest_type"], ["default", testcycle, "default", "default", "default", "default", "default", "default", "default", "default"])

            self.pytest_config_file_generator(config_file_location, config_dict)


# if __name__ == "__main__":
#     home_dir = os.getcwd()
#     config_json_file = os.path.join(home_dir, "Library", "config_file.json")
#     function = ConfigFileGenerator()
#     config_file_location = os.path.join(home_dir, "config_file.py")

#     val_framework = "pytest"
#     maestro_1 = "maestro_github_remote_side_branch"
#     maestro_2 = "maestro_repo"
#     maestro_repo_1 = "helmi_repo"
#     maestro_branch = "2605p3_TAM"
#     fpga_image = "drop3build0v62019"
#     system_provisioning = "sonora_fec"

#     function.main(val_framework, config_file_location, "fvVVD", maestro_branch="biultr", fpga_image="drop3build0v62021")