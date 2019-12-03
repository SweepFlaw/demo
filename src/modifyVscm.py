from setting import *
from position_learning import getRecommendList

# return two values
# 1. sorted vscm
# 2. the number of line-column pair from POSLEARN_APPFILE's output.
def applyNNResult(vscm, codeFilename):
    getRecommendList(codeFilename, MODEL_TYPE)
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