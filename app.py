from sys import argv

import src
from src.setting import *
from src.makeVscm import genVscm
from src.modifyCode import readVscm
from src.modifyVscm import applyNNResult
from src.testcase import readTC
from src.findVarError import findVarErr

if __name__ == "__main__":
    if len(argv) < 4:
        print('Usage: python3 app.py [SRC-file] [input-TC-dir] [output-TC-dir]')
        exit(-1)
    else:
        targetFilename = os.path.abspath(argv[1])
        inputTCdirname = os.path.abspath(argv[2])
        outputTCdirname = os.path.abspath(argv[3])
        
        with open(targetFilename, 'r') as tf:
            code = tf.readlines()
        
        genVscm(targetFilename, VSCM_FILENAME)
        vscm = sorted(readVscm(VSCM_FILENAME), key=lambda x: (x['targetLine'], x['targetColumn'], x['targetStr']))
        if USE_MODEL:
            vscm, _ = applyNNResult(vscm, targetFilename)

        itcs, otcs = readTC(inputTCdirname, outputTCdirname)

        mc, mci, vi, rs, rc, et, vic = findVarErr(
            code,
            vscm,
            MODIFIEDSRC_FILENAME,
            COMPILED_FILENAME,
            MOD_LIMIT,
            itcs,
            otcs,
            SINGLE_TIMEOUT,
            TOTAL_TIMEOUT,
            INFO_PRINT
        )

        print('\n============================FINISHED.')
        if rs == 0:
            print('RESULT: SUCCESS')
        else:
            print('RESULT: FAILED')
        print('ITER COUNT =\t', vic)
        print('ELAPSED TIME =\t', et)
        if rs == 0:
            print('MODIFIED LINES =\t', list(map(lambda x : x + 1, mci)))
            print('<<<MODIFIED CODE>>>')
            print(mc)
