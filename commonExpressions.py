import sqlite3
import time
from openpyxl import Workbook


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
        timeL = time.ctime().split()
        timeS = ""
        for i in range(len(timeL)):
            timeS = timeS + timeL[i]
        timeS = timeS.replace(":", "")
        db = sqlite3.connect("output.db")
        dbc = db.cursor()
        dbc.execute("CREATE TABLE {}(word TEXT, count INT)".format(str(timeS)))
        for i in range(len(keysindex)):
            dbc.execute("INSERT INTO {} values(\"{}\", {})".format(
                str(timeS), keysindex[i], indexed[keysindex[i]]))
        db.commit()
        db.close()
    elif outputtype == "xlsx":
        wb = Workbook()
        ws = wb.active
        turn = 0
        endturn = len(keysindex)
        while turn < endturn:
            ws.append([keysindex[turn], indexed[keysindex[turn]]])
            turn += 1
        wb.save("output.xlsx")
