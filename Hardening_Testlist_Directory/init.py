import sys 
import ntpath

current_path = ntpath.abspath(ntpath.dirname(__file__))
current_path = current_path.replace("\\","/")
sys.path.append(current_path + "/..")
import ace_proj_init as proj_init



