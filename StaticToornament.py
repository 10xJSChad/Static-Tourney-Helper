import requests
import variables

def getCustomFromMatch(custom, matchID):
    r = requests.get(variables.tourney + "matches/" + matchID + "/players")
    fullSrc = []
    results = []
    for line in r.iter_lines():
        fullSrc.append(str(line))
    for i in range(0, len(fullSrc)):
        #print(fullSrc[i])
        if(fullSrc[i].find(custom) != -1):
            newLine = (fullSrc[i + 1][:-1])
            newLine = newLine[34:]
            results.append(newLine)
    return results

def getMatchFromBracket(match, bracket):
    r = requests.get(bracket)
    matchLine = ""
    matchID = ""
    quoteCount = 0
    for line in r.iter_lines():
        if str(line).find(match) != -1: matchLine = str(line); break
    for x in matchLine:
        if x == '"': quoteCount += 1
        if quoteCount == 9: matchID += x
    matchID = matchID[1:]
    return(matchID)

def getMatchAndCustom(match):
    return getCustomFromMatch(variables.custom, getMatchFromBracket(match, variables.bracket))

def getMatchAndCustomFormatted(match):
    results = getMatchAndCustom(match)
    formattedResult = ""
    for x in results:
        formattedResult += variables.prefix + x + ", "
    formattedResult += variables.aftertext
    return formattedResult

#print(getCustomFromMatch("SteamID"))
#print(getMatchFromBracket("M 2.1", variables.bracket))