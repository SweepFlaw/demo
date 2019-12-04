import os
import subprocess
import sys
import time
from itertools import combinations

from .modifyCode import readVscm, modCodesFull
from .makeVscm import genVscm


# input:
#   - code (string)
#   - tmpFilename (string)
#   - cFilename (string) (compiled file name)
#   - inputTestcases (list(bytes))
#   - outputTestcases (list(bytes))
#   - singleTestTimeout (int)
#   - stopFast (bool, optional) (if stopFast true, return immediately when the test fails)
# output:
#   - totalResultCode (0 for success. 1 for testcase error. 2 for compile error. 3 for no testcases)
#   - resultCode for each testcases (list(int)) (0 for success. 1 for W/A. 2 for timeout. 3 for other runtime errors.)
def codeTest(code, tmpFilename, cFilename, inputTestcases, outputTestcases, singleTestTimeout, stopFast=True):
    # exceptional case : no testcases
    if len(inputTestcases) < 1:
        return (3, [])
    
    # put code into file
    with open(tmpFilename, 'w') as file:
        file.write(code)
    # compile
    p = subprocess.run(['g++', tmpFilename, '-o', cFilename], shell=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if p.returncode != 0:
        return (2, [])
    
    # run testcases
    totalResultCode = 0
    resultCodes = []
    for i, o in zip(inputTestcases, outputTestcases):
        try:
            p = subprocess.run([cFilename], input=i, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=singleTestTimeout)
        except subprocess.TimeoutExpired:
            totalResultCode = 1
            resultCodes.append(2)
            if stopFast:
                return totalResultCode, resultCodes
            else:
                continue
        except:
            totalResultCode = 1
            resultCodes.append(3)
            if stopFast:
                return totalResultCode, resultCodes
            else:
                continue
        if o == p.stdout:
            resultCodes.append(0)
        else:
            totalResultCode = 1
            resultCodes.append(1)
            if stopFast:
                return totalResultCode, resultCodes
    return totalResultCode, resultCodes


# input:
#   - code (list contains the whole code line by line.) (list(string))
#   - vscm (list(dictionary))
#   - tmpFilename (string)
#   - cFilename (string)
#   - modNum (int) (the number of modifications)
#   - inputTestcases (list(bytes))
#   - outputTestcases (list(bytes))
#   - singleTestTimeout (represent timeout seconds.)
#   - totalTimeout (represent timeout seconds. int, optional)  (non-positive value for no-limit)
#   - printDebugInfo (bool, optional)
# output: multiple return values.
#   - modified code String (string) (If it fails to find, return '')
#   - modified codeline Indices, start from 0 (list(int))
#   - selected vscmIndices for successful modification (list(int))
#   - returnStatus(int) (0 for success, 1 for not-found, 2 for timeout, 3 for no testcases, 4 for wrong-answer ok problem)
#   - resultCodes (list(int)) (results for each testcases: following the return value of codeTest.)
#   - elapsed time (int) (seconds)
#   - valid Iterate count (int)
def findVarErr(code, vscm, tmpFilename, cFilename, modNum, inputTestcases, outputTestcases, singleTestTimeout, totalTimeout=0, printDebugInfo=True):
    if printDebugInfo:
        print('findVarErr2 : dbg: findVarErr2 START')
    startTime = time.time()
    
    if len(inputTestcases) < 1:
        return ('', [], [], 3, [], (time.time() - startTime), 0)
    
    timeout = startTime + totalTimeout
    validModificationCount = 0
    
    # variables for debugging
    timeCache = startTime
    
    # debugging - print the length of vscm
    if printDebugInfo:
        print('findVarErr2 : dbg: VSCM Length: ', len(vscm))
        print('||  # of testcases: ', len(inputTestcases))
    
    for mN in range(1, modNum + 1):
        # mT for modification-tuple
        # mL for modification-list
          
        #debugging - print current mN
        if printDebugInfo:
            print('findVarErr2 : dbg: < SET mN VALUE >')
            print('||  mN = ', mN)
          
        for mT in combinations(range(len(vscm)), mN):
            sys.stdout.flush()
            # timeout check
            if totalTimeout > 0 and time.time() > timeout and printDebugInfo:
                print('findVarErr2 : dbg: reach at totalTimeout = ', totalTimeout)
                return ('', [], [], 2, [], (time.time() - startTime), validModificationCount)
        
            # modify Code
            mc, mcis, rs = modCodesFull(code, vscm, mT)
            
            if rs != 0:
                continue
                
            #  test code with testcases
            trc, rcs = codeTest(mc, tmpFilename, cFilename, inputTestcases, outputTestcases, singleTestTimeout)
            
            validModificationCount += 1
            # debugging - count the number of iteration
            if printDebugInfo:
                if validModificationCount % 20 == 1:
                    print('findVarErr2 : dbg: validModificationCount = ', validModificationCount)
                    print('||  ELAPSED TIME: ' + str(time.time() - timeCache))
                    timeCache = time.time()
                    sys.stdout.flush()
            
            if trc == 0:
                if printDebugInfo:
                    print('findVarErr2 : dbg: SUCCESS at validModificationCount = ', validModificationCount)
                return (mc, mcis, list(mT), 0, rcs, (time.time() - startTime), validModificationCount)
    return ('', [], [], 1, [], (time.time() - startTime), validModificationCount)