import os
from pathlib import Path

### demo Setting
TOTAL_TIMEOUT   = 1200
SINGLE_TIMEOUT  = 2
MOD_LIMIT       = 1
USE_MODEL       = True
MODEL_TYPE      = 'GRU'
STOP_FAST       = True

### Print Setting
PROGRESS_PRINT  = True
INFO_PRINT      = True

### Testcase Filenames
TESTCASE_STARTNUM = 1
TESTCASE_PREFIX = ''
TESTCASE_POSTFIX = ''

### PROJECT DIRECTORIES
ROOT_DIR = Path(__file__).parent.parent
SRC_DIR = os.path.join(ROOT_DIR, 'src')
BIN_DIR = os.path.join(ROOT_DIR, 'bin')
TMP_DIR = os.path.join(ROOT_DIR, 'tmp')

### VSCM (variable-substitution-candidate-map)
# to compile vscm source, see "https://github.com/SweepFlaw/VarSubsCandListGenCpp"
VSCM_GENERATOR_BINARY = os.path.join(BIN_DIR, 'vscm')
VSCM_MAIN_OPTION = 0
VSCM_SELECT_MODE = 2

### Temporary Filenames
VSCM_FILENAME = os.path.join(TMP_DIR, 'vscm.csv')
MODIFIEDSRC_FILENAME = os.path.join(TMP_DIR, 'modified_src.cpp')
COMPILED_FILENAME = os.path.join(TMP_DIR, 'compiled.out')

### NN PRIORITY CALCULATOR ("https://github.com/SweepFlaw/position-learning")
POSLEARN_APPLY = USE_MODEL
POSLEARN_MODE = MODEL_TYPE
POSLEARN_PROJ_DIR = os.path.join(ROOT_DIR, 'position-learning')
POSLEARN_APPFILE = os.path.join(POSLEARN_PROJ_DIR, 'app.py')
