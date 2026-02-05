import datetime
import os
import shutil

class HardeningOutputFolderConstructor:
    def __init__(self):
        None
    
    def format_status_line(self, label, status):
        padding = max(40 - len(f"{label} [{status}]: "), 0)
        return f"{label}{' ' * padding}[{status}]"
    
    def intel_workweek_day_convertor(self):
        date_obj = datetime.date.today()
        iso_year, iso_week, iso_weekday = date_obj.isocalendar()
        workweek_str = f"{str(iso_year)[-2:]}WW{iso_week}_{iso_weekday}"
        return workweek_str
    
    def time_now(self):
        current_time = datetime.datetime.now()
        return current_time.hour, current_time.minute, current_time.second

    def main(self, validation_framework, feature_testcase, home_dir, validation_framework_sp=None, platform=None):
        
        print(f"{self.format_status_line('Output Directory Folder Log', 'info')}: Constructing Temporary Output Folder Directory")
        hardening_output_folder_directory = os.path.join(os.path.dirname(home_dir), 'Hardening')
        intel_workweek_day = self.intel_workweek_day_convertor()
        hour, minute, second = self.time_now()
        if platform == None:
            output_folder_name = f"hardening_{intel_workweek_day}_{hour:02d}{minute:02d}{second:02d}_{validation_framework}_{feature_testcase}"
        else:
            output_folder_name = f"hardening_{intel_workweek_day}_{hour:02d}{minute:02d}{second:02d}_{validation_framework_sp}_{feature_testcase}_{platform}"
        output_folder_path = os.path.join(hardening_output_folder_directory, output_folder_name)
        os.mkdir(output_folder_path)

        print(f"{self.format_status_line('Output Directory Folder Log', 'info')}: Adding external files for perspec maestro")
        if validation_framework == "perspec_maestro" or validation_framework_sp == "perspec_maestro":
            #Copy init.py and ace_proj_init.py into the output folder
            init_output_file = os.path.join(output_folder_path, 'init.py')
            shutil.copy(os.path.join(home_dir, 'Hardening_Testlist_Directory', 'init.py') , init_output_file)
            proj_init_output_file = os.path.join(output_folder_path, 'ace_proj_init.py')
            shutil.copy(os.path.join(home_dir, 'Hardening_Testlist_Directory', 'ace_proj_init.py') , proj_init_output_file)
        
        print(f"{self.format_status_line('Output Directory Folder Log', 'info')}: {output_folder_path}")
        print(f"{self.format_status_line('Output Directory Folder Log', 'PASS')}: Temporary Output Folder Directory Completed Successfully")
        return output_folder_path