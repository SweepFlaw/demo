from .setting import *
import subprocess

# return two values
# 1. sorted vscm
# 2. the number of line-column pair from POSLEARN_APPFILE's output.
def applyNNResult(vscm, codeFilename):
    pr = subprocess.Popen(['python', POSLEARN_APPFILE, codeFilename, POSLEARN_MODE], cwd=POSLEARN_PROJ_DIR, stdout=subprocess.PIPE)
    pr_out, pr_err = pr.communicate()
    pr_out = pr_out.decode("utf-8") 
    rnnResult = list(set([(x.split(',')[0], x.split(',')[1]) for x in pr_out.split('\n')[1:-1]]))
    scoreDict = {}
    for i, c in enumerate(rnnResult):
        lin = int(c[0])
        col = int(c[1])
        scoreDict[(lin, col)] = i
    vscm_tmp = []
    for x in vscm:
        score = scoreDict.setdefault((int(x['targetLine']), int(x['targetColumn'])), len(rnnResult))
        vscm_tmp.append((x, score))
    return [ x[0] for x in sorted(vscm_tmp, key=lambda x: x[1]) ], len(rnnResult)