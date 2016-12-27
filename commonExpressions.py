import sqlite3


class CommonExpressions:
    punctuations = [".", "?", ";", ":", "!", "(", ")", ",", "\\", "\""]
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


def save(indexed, keysindex, outputtype = "txt"):
    if outputtype == "txt":
        output = ""
        for i in range(len(keysindex)):
            output = output + "\n {}  :: {}".format(keysindex[i], str(indexed[keysindex[i]]))
        fileoutput = open("output.txt", "w")
        fileoutput.write(output)
        fileoutput.close()
    elif outputtype == "sqlite3":
        db = sqlite3.connect("output.db")
        dbc = db.cursor()
        dbc.execute("CREATE TABLE freqAnalyisis(word TEXT, count INT)")
        for i in range(len(keysindex)):
            dbc.execute("INSERT INTO freqAnalyisis values(\"{}\", {})".format(
                keysindex[i], indexed[keysindex[i]]))
        db.commit()
        db.close()
