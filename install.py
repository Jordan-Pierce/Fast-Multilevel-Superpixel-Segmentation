import os
import sys
import platform
import subprocess

# ----------------------------------------------
# OS
# ----------------------------------------------
osused = platform.system()

if osused not in ['Windows', 'Linux']:
    raise Exception("This install script is only for Windows or Linux")


# ----------------------------------------------
# Python version
# ----------------------------------------------
python_v = f"{sys.version_info[0]}{sys.version_info[1]}"
python_sub_v = int(sys.version_info[1])

# check python version
if python_sub_v != 8:
    raise Exception(f"Only Python 3.{python_sub_v} is supported.")


# ----------------------------------------------
# Other dependencies
# ----------------------------------------------
install_requires = [
    'wheel',
    'msvc-runtime',

    'numpy',
    'pandas',
    'seaborn',
    'matplotlib',
    'scikit-image',
    'opencv-python',
    'cython',
    'fast-slic'

]

# Installing all the other packages
for package in install_requires:

    try:
        print(f"NOTE: Installing {package}")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

    except Exception as e:
        print(f"There was an issue installing {package}\n{e}\n")
        print(f"If you're not already, please try using a conda environment with python 3.8")
        sys.exit(1)

print("Done.")