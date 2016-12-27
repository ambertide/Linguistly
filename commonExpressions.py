class CommonExpressions:
    punctuations = [".", "?", ";", ":", "!", "(", ")", ","]
    trtolatin = ["I"]
    trtolatindict = {"I": "i"}


def prepare(stringObject, tr = "no"):
    hold = stringObject
    if tr == "yes":
        for i in range(len(CommonExpressions.trtolatin)):
            hold = hold.replace(CommonExpressions.trtolatin[i], CommonExpressions.trtolatindict[CommonExpressions.trtolatin[i]])
    for i in range(len(CommonExpressions.punctuations)):
        hold = hold.replace(CommonExpressions.punctuations[i], "")
    hold = hold.lower()
    output = hold.split(" ")
    return output
