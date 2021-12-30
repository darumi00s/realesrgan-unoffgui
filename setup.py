import cx_Freeze
import sys
import os
import os.path

import re

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

executables = [cx_Freeze.Executable("main.py", base="Win32GUI", icon="./src/icon.ico")]

cx_Freeze.setup(
    name='Real-ESRGAN Unofficial GUI V1',
    version='1.0',
    executables=executables,
    options = { "build.exe":{"packages":["tkinter", "re"],
    'include_files':[
        os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
        os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'),
    ]}
    }
)