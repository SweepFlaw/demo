from sys import argv
from json import dump

import src
from src.setting import *
from src.makeVscm import genVscm
from src.modifyCode import readVscm
from src.modifyVscm import applyNNResult
from src.testcase import readTC
from src.findVarError import findVarErr

if __name__ == "__main__":
    if len(argv) < 4:
        if JSONFILE_OUT:
            print('Usage: python3 app.py [SRC-file] [input-TC-dir] [output-TC-dir] [Json-output-file]')
        else:
            print('Usage: python3 app.py [SRC-file] [input-TC-dir] [output-TC-dir]')
        exit(-1)
    elif JSONFILE_OUT and (len(argv) < 5):
        print('Usage: python3 app.py [SRC-file] [input-TC-dir] [output-TC-dir] [Json-output-file]')
        exit(-1)
    else:
        targetFilename = os.path.abspath(argv[1])
        inputTCdirname = os.path.abspath(argv[2])
        outputTCdirname = os.path.abspath(argv[3])

        if JSONFILE_OUT:
            jsonOutFilename = os.path.abspath(argv[4])
        
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
            PROGRESS_PRINT
        )

        if PROGRESS_PRINT:
            print('app.py : dbg: findVarErr2 FINISHED')

        if INFO_PRINT:
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

        # JSON file output format
        if JSONFILE_OUT:
            d = {}
            d['targetFilename'] = targetFilename
            d['inputTCdirname'] = inputTCdirname
            d['outputTCdirname'] = outputTCdirname
            d['modifiedCode'] = mc          # check 'modified code String' in 'findVarError.py'
            d['modifiedCodeLines'] = mci    # check 'modified codeline Indices' in 'findVarError.py'
            d['returnStatus'] = rs          # check 'returnStatus' in 'findVarError.py'
            d['resultCodes'] = rc           # check 'resultCodes' in 'findVarError.py'
            d['elapsedTime'] = et           # check 'elpased time' in 'findVarError.py'
            d['iterCount'] = vic            # check 'valid Iterate count' in 'findVarError.py'
            with open(jsonOutFilename, JSONFILE_OUTOPTION) as jsonfile:
                if PROGRESS_PRINT:
                    print('app.py : dbg: JSONFILE WRITE START')
                dump(d, jsonfile, indent=JSONFILE_INDENT)
                if PROGRESS_PRINT:
                    print('app.py : dbg: JSONFILE WRITE FINISHED')

