import datetime
import os
import shutil

class HardeningOutputFolderConstructor:
    def __init__(self):
        None
    
    def intel_workweek_day_convertor(self):
        date_obj = datetime.date.today()
        iso_year, iso_week, iso_weekday = date_obj.isocalendar()
        workweek_str = f"{str(iso_year)[-2:]}WW{iso_week}_{iso_weekday}"
        return workweek_str
    
    def time_now(self):
        current_time = datetime.datetime.now()
        return current_time.hour, current_time.minute, current_time.second

    def main(self, home_dir):
        hardening_output_folder_directory = os.path.join(os.path.dirname(home_dir), 'Hardening')
        intel_workweek_day = self.intel_workweek_day_convertor()
        hour, minute, second = self.time_now()
        output_folder_name = f"hardening_{intel_workweek_day}_{hour:02d}{minute:02d}{second:02d}"
        output_folder_path = os.path.join(hardening_output_folder_directory, output_folder_name)
        os.mkdir(output_folder_path)
        #Copy init.py and ace_proj_init.py into the output folder
        init_output_file = os.path.join(output_folder_path, 'init.py')
        shutil.copy(os.path.join(home_dir, 'Hardening_Testlist_Directory', 'init.py') , init_output_file)
        proj_init_output_file = os.path.join(output_folder_path, 'ace_proj_init.py')
        shutil.copy(os.path.join(home_dir, 'Hardening_Testlist_Directory', 'ace_proj_init.py') , proj_init_output_file)
        return output_folder_path