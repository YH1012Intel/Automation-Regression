#!/bin/sh
"true" '''\'
[ -e /usr/intel/bin/python3.6.3a ] && exec /usr/intel/bin/python3.6.3a "$0" "$@"
exec python3 "$0" "$@"
'''


import hashlib
import os
import site
import subprocess
import sys


# This is the new USER_BASE (prev default was ~/.local) for pip to install packages into
my_dir_path = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
user_base_path = os.getenv("PYTHONUSERBASE", my_dir_path)

# TODO: Recursively check containing folders? Where should requirements.txt live?
requirements_path = os.path.join(my_dir_path, "requirements.txt")
hash_path = os.path.join(my_dir_path, "dependency_hash.txt")

# Figure out the USER_SITE suffix (typically lib/pythonX.Y/site-packages) for this
# Python version, and append it to new USER_BASE to create the new USER_SITE
user_site_path = os.path.join(user_base_path, site.USER_SITE[len(site.USER_BASE) + 1:])

# Allow for imports from this new USER_SITE path
sys.path.insert(0, user_site_path)

# Update USER_BASE to match our desired USER_SITE install path
_modified_env = os.environ.copy()
_modified_env["PYTHONUSERBASE"] = user_base_path


def _get_cur_req_hash():
    """Return an MD5 hash of the requirements.txt file contents, to check for changes"""

    hasher = hashlib.md5()
    with open(requirements_path, "rb") as f:
        hasher.update(f.read())
    return hasher.hexdigest()


def _install_dependencies(use_pythonsv_index=False):
    """Install/upgrade packages from requirements.txt into the USER_SITE directory"""
    
    # Install/upgrade the packages
    cmd_list = [
        sys.executable,
        "-m",
        "pip",
        "install",
        "--upgrade",
        # "--no-deps",
        "--no-cache-dir",
        "-r",
        requirements_path,
    ]
    cmd_index_list = ["-i", "https://intelpypi.intel.com/root/pypi"]
    # PyPI mirror does not require a username/password, so we hide the output from users
    kwargs = {"stdout": subprocess.PIPE, "stderr": subprocess.STDOUT}

    # We may be falling back and needing to check the PythonSV packages
    if use_pythonsv_index:
        cmd_index_list = ["-i", "https://intelpypi.intel.com/pythonsv/staging"]
        # Don't redirect stdout/stderr; we need to interactively login for this index
        kwargs = {}

    result = subprocess.run(cmd_list + cmd_index_list, env=_modified_env, **kwargs)
    if result.returncode:
        if use_pythonsv_index:
            print("Unable to install dependencies. Exiting.")
            sys.exit(result.returncode)
        else:
            # Missing packages may not be in the public PyPI; check PythonSV packages
            print("Unable to install using root/pypi; checking pythonsv/staging...")
            _install_dependencies(use_pythonsv_index=True)

    # Write the new requirements.txt hash for future dependency change checks
    try:
        with open(hash_path, "w") as f:
            f.write(_get_cur_req_hash())

    # We may not have write access to this location; can check in other ways
    except IOError:
        pass


def _requirements_changed():
    """Check if the requirements.txt match the currently installed list of packages"""

    # Try to use the stored MD5 hash to detect differences
    try:
        with open(hash_path, "r") as f:
            prev_hash = f.read().strip()

        cur_hash = _get_cur_req_hash()
        if cur_hash != prev_hash:
            print("Change to requirements.txt detected. Upgrading dependencies...")
            return True

    # If the MD5 has hasn't been stored, we may not have downloaded the dependencies
    # yet, OR we may not have write access to this directory. Regardless, we check using
    # pip list.
    except FileNotFoundError:
        # Get the requirements.txt dependencies
        with open(requirements_path, "r") as f:
            cur_deps = set()
            for l in f:
                # FIXME: This requires that all requirements.txt dependencies are
                #        pinned; we don't support "pkg>=1.0.0" for example
                pkg, ver = l.strip().split("==")
                cur_deps.add("%s/%s" % (pkg, ver))

        # Get the currently installed packages
        cmd_list = [sys.executable, "-m", "pip", "list", "--format=legacy"]
        installed = subprocess.check_output(
            cmd_list, env=_modified_env, stderr=subprocess.PIPE
        )
        installed_deps = set()
        for pkg_line in installed.decode("utf8").strip().split("\n"):
            pkg, ver = pkg_line.strip().split()
            ver = ver.replace("(", "").replace(")", "")
            # These won't be listed in requirements.txt; ignore
            if pkg in ("pip", "setuptools"):
                continue
            installed_deps.add("%s/%s" % (pkg, ver))

        if cur_deps != installed_deps:
            print("Change to requirements.txt detected. Upgrading dependencies...")
            return True

    return False


def _check_packages():
    """Check if we need to install/upgrade requirements.txt packages"""

    # If there are no third-party packages, we have no need to install anything
    if not os.path.exists(requirements_path):
        print("No requirements.txt file found; skipping package install check.")
        return

    # If we have third-party packages and USER_SITE doesn't exist, install everything
    if not os.path.isdir(user_site_path):
        print("Missing user site-packages directory; installing dependencies...")
        _install_dependencies()
        return

    # If the requirements.txt file has changed, install/upgrade changed packages
    if _requirements_changed():
        _install_dependencies()


_check_packages()