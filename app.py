import sys

from setting import *
from makeVscm import genVscm
from modifyCode import readVscm
from testcase import readTC
from findVarError import findVarErr

if __name__ == "__main__":
    if len(argv) < 4:
        print('Usage: python3 app.py [SRC-file] [input-TC-dir] [output-TC-dir]')
        exit(-1)
    else:
        targetFilename = argv[1]
        inputTCdirname = argv[2]
        outputTCdirname = argv[3]
        
        with open(targetFilename, 'r') as tf:
            code = tf.readlines()
        genVscm(targetFilename, VSCM_FILENAME)
        vscm = readVscm(VSCM_FILENAME)
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

        print('FINISHED.')
        if rs == 0:
            print('SUCCESS')
        else:
            print('FAILED')
        print('ITER COUNT = ', vic)
        print('ELAPSED TIME = ', et)
        if rs == 0:
            print('<<<MODIFIED CODE>>>')
            print(mc)
