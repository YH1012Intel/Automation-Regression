import os
import subprocess

# Path to Python 3.11.1 executable
python311_path = "/nfs/site/itools/em64t_SLES12SP5/pkgs/wrapper/2.15/bin/python3.11.1"  # <-- Change this to your actual path

python_libraries = []

home_dir = os.getcwd()

with open(os.path.join(home_dir, "libs", "requirements.txt"), 'r') as r:
    for python_library_requirement in r:
        python_libraries.append(python_library_requirement)

env_name = "py_env"

# Set proxy environment variables
proxy = "http://proxy-dmz.intel.com:912"
env = os.environ.copy()
env["http_proxy"] = proxy
env["https_proxy"] = proxy

# Step 1: Create the virtual environment with Python 3.11.1
subprocess.run([python311_path, "-m", "venv", env_name], check=True, env=env)

# Step 2: Construct the path to the pip executable inside the environment (Linux)
pip_path = os.path.join(env_name, "bin", "pip")

# Step 3: Install libraries in the environment
for lib in python_libraries:
    subprocess.run([pip_path, "install", lib], check=True, env=env)

print(f"Environment '{env_name}' created with Python 3.11.1 and libraries installed.")


# python3.11.1 libs/setup_env.py
# source myenv/bin/activate.csh
# pip list
# deactivate