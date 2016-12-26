class CommonExpressions:
    punctuations = [".", "?", ";", ":", "!", "(", ")", ","]
    trtolatin = ["I"]
    trtolatindict = {"I": "i"}


def prepare(stringObject):
    hold = ""
    for i in range(len(CommonExpressions.trtolatin)):
        hold = stringObject.replace(CommonExpressions.trtolatin[i], CommonExpressions.trtolatindict[CommonExpressions.trtolatin[i]])
    for i in range(len(CommonExpressions.punctuations)):
        hold = stringObject.replace(CommonExpressions.punctuations[i], "")
    hold = hold.lower()
    output = hold.split(" ")
    return output
