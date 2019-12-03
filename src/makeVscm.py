import subprocess

from setting import *

vscmMainOption=VSCM_MAIN_OPTION
vscmSelectCandOption=VSCM_SELECT_MODE

# targetCppSourcePath(string)
# vscmOutputFilePath(string)
# output: (void). File with the name vscmOutputFilePath created.
def genVscm(targetCppSourcePath, vscmOutputFilePath):
    subprocess.call([
        VSCM_GENERATOR_BINARY,
        targetCppSourcePath,
        vscmOutputFilePath,
        str(vscmMainOption),
        str(vscmSelectCandOption)
    ])