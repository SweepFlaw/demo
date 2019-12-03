from csv import reader
from copy import deepcopy
from itertools import combinations

from makeVscm import genVscm


# input: targetFilename(string)
# output: entireFile String line by line (list(string))
def readTargetFile(targetFilename):
    with open(targetFilename, 'r') as file:
        codeStr = file.readlines()
    return codeStr


# input: vscmFilename(string)
# output: vscm = list(dictionary)
# -- dictionary layout
#    - targetLine (int)
#    - targetColumn (int)
#    - targetOffset (int)
#    - targetLength (int)
#    - targetStr (string)
#    - candidateLine (int)
#    - candidateColumn (int)
#    - candidateOffset (int)
#    - candidateLength (int)
#    - candidateStr (string)
def readVscm(vscmFilename, csvSeparator=','):
    vscm = []
    with open(vscmFilename, 'r') as csvfile:
        vscmReader = reader(csvfile, delimiter=csvSeparator)
        for row in vscmReader:
            r = {}
            r['targetLine'] = int(row[0])
            r['targetColumn'] = int(row[1])
            r['targetOffset'] = int(row[2])
            r['targetLength'] = int(row[3])
            r['targetStr'] = row[4]
            r['candidateLine'] = int(row[5])
            r['candidateColumn'] = int(row[6])
            r['candidateOffset'] = int(row[7])
            r['candidateLength'] = int(row[8])
            r['candidateStr'] = row[9]
            vscm.append(r)
    return vscm


# input: 
#   - code (list contains the whole code line by line.) (list(string))
#   - vscm (list(dictionary))
#   - vscmIndice (list(int))
# output: multiple return values.
#   - modified codeline Strings (dict(int -> string)),
#   - modified codeline Index, start from 0 (list(int)),
#   - returnStatus(int) (0 for success, (-1) for failure, (-2) for failure)
def modCodes(code, vscm, vscmIndice):
    # check if vscmIndex is valid index
    for vscmindex in vscmIndice:
        if len(vscm) < vscmindex:
            return ({}, [], -1)
        
    modSpecs = [{'lineNo': vscm[k]['targetLine'] - 1,
                 'colNo': vscm[k]['targetColumn'] - 1,
                 'tarStr': vscm[k]['targetStr'],
                 'canStr': vscm[k]['candidateStr']
                } for k in vscmIndice]
    
    # modSpecsDict : dict(int -> list(modSpec))
    #   map the lineNumber to the subset of modSpecs.
    modSpecsDict = {}
    for ms in modSpecs:
        modSpecsDict.setdefault(ms['lineNo'], [])
        modSpecsDict[ms['lineNo']].append(ms)
    
    # msbl for mode-spec-___-list. I don't know why i named it like that.
    # check if two or more vscm indice points to the same location or 
    for k, msbl in modSpecsDict.items():
        for (spec1, spec2) in combinations(msbl, 2):
            if (spec1['colNo'] == spec2['colNo']):
            #or len(spec1['tarStr']) + spec1['colNo'] > spec2['colNo']:
                return ({}, [], -2)
        # sort lists in modSpecsDict by 'colNo' value.
        modSpecsDict[k] = sorted(msbl, key=lambda x:x['colNo'])
    
    # mcs : modified codeline Strings(dict(int -> string)), return value.
    mcs = {}
    for k, msbl in modSpecsDict.items():
        if 0 < len(msbl):
            lineNum = msbl[0]['lineNo']
            mc = deepcopy(code[lineNum])
            if len(msbl) < 2:
                msbl0 = msbl[0]
                # same as the function 'modCode'
                front = mc[:msbl0['colNo']]
                end = mc[msbl0['colNo'] + len(msbl0['tarStr']):]
                mc = "".join([front, msbl0['canStr'], end])
                mcs[lineNum] = mc
            else:
                cc = []
                cc.append(mc[:(msbl[0]['colNo'])])
                for i in range(0, len(msbl)-1):
                    cc.append(msbl[i]['canStr'])
                    start = msbl[i]['colNo'] + len(msbl[i]['tarStr'])
                    end = msbl[i+1]['colNo']
                    cc.append(mc[start:end])
                cc.append(msbl[-1]['canStr'])
                start = msbl[-1]['colNo'] + len(msbl[-1]['tarStr'])
                cc.append(mc[start:])
                mcs[lineNum] = ''.join(cc)
        else:
            pass
    
    return (mcs, [k for (k,v) in modSpecsDict.items()], 0)


# function modCodesFull
# input:
#   - code (list contains the whole code line by line.) (list(string))
#   - vscm (list(dictionary))
#   - vscmIndice (list(int))
# output: multiple return values.
#   - modified whole source String (string)
#   - modified codeline Index, start from 0 (list(int))
#   - returnStatus(int) (0 for success, (-1) for failure, (-2) for failure)
def modCodesFull(code, vscm, vscmIndice):
    mcs, mcis, rs = modCodes(code, vscm, vscmIndice)
    if rs != 0:
        return (code, [], rs)
       
    mcsList = []
    for i in range(0, len(code)):
        if i in mcis:
            mcsList.append(mcs[i])
        else:
            mcsList.append(code[i])
    return (''.join(mcsList), mcis, 0)
