import os
from setting import *

def readTC(inputTCDir, outputTCDir):
    inputTestcases = []
    outputTestcases = []
    i = TESTCASE_STARTNUM
    while True:
        fn = TESTCASE_PREFIX + str(i) + TESTCASE_POSTFIX
        try:
            with open(os.path.join(inputTCDir, fn), 'rb') as itcf:
                with open(os.path.join(outputTCDir, fn), 'rb') as otcf:
                    inputTestcases.append(itcf.read())
                    outputTestcases.append(otcf.read())
        except IOError:
            break
        i += 1
    return inputTestcases, outputTestcases