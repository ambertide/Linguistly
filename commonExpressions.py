import sqlite3
import time
from openpyxl import Workbook
from docx import Document


class CommonExpressions:
    punctuations = [".", "?", ";", ":", "!", "(", ")", ",", "\\", "\"", "-",
                    "--", "  ", "”", "“"]
    suffices_tr = ["'nin", "'nın", "'a", "'e", "'i", "'", "'de", "'da",
                    "'in", "'ın", "'ım", "'im", "'den", "'dan", "'ten",
                    "'tan", "”", "'te", "'ta",
                    "’nin", "’nın", "’a", "’e", "’i", "’de", "’da",
                    "’in", "’ın", "’ım", "’im", "’den", "’dan", "’ten",
                    "’tan", "’te", "’ta"]


    suffices_en = ["'s", "'re", "n't"]
    trtolatin = ["I"]
    trtolatindict = {"I": "i"}


def prepare(stringObject, tr = "no"):
    hold = stringObject
    if tr == "yes":
        for i in range(len(CommonExpressions.trtolatin)):
            hold = hold.replace(CommonExpressions.trtolatin[i], CommonExpressions.trtolatindict[CommonExpressions.trtolatin[i]])
    for i in range(len(CommonExpressions.punctuations)):
        hold = hold.replace(CommonExpressions.punctuations[i], " ")
    hold = hold.lower()
    output = hold.split(" ")
    return output


def save(indexed, keysindex, outputtype = "txt"):
    if outputtype == "txt":
        output = ""
        for i in range(len(keysindex)):
            output = output + "\n {}  :: {}".format(keysindex[i], str(indexed[keysindex[i]]))
        fileoutput = open("output{}.txt".format(time.ctime().replace(":", "-")), "w")
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
        wb.save("output{}.xlsx".format(time.ctime().replace(":", "-")))
    elif outputtype == "csv":
        output = "word,count"
        for i in range(len(keysindex)):
            output = output + "\n{},{}".format(keysindex[i], str(indexed[keysindex[i]]))
        fileoutput = open("output{}.csv".format(time.ctime().replace(":", "-")), "w")
        fileoutput.write(output)
        fileoutput.close()


def strip_suffices(input_, lang="Turkish"):
    if lang == "Turkish":
        for i in range(len(CommonExpressions.suffices_tr)):
            input_ = input_.replace(CommonExpressions.suffices_tr[i], "")
    elif lang == "English":
        for i in range(len(commonExpressions.suffices_en)):
            input_ = input_.replace(CommonExpressions.suffices_en[i], "")
    return input_

def save_unsufficed(inputed, method="txt"):
    if method == "txt":
        file_ = open("outputSuffix.txt", "w")
        file_.write(inputed)
        file_.close()
    elif method == "docx":
        output_file = Document()
        inputedlines = inputed.split("\n")
        for i in range(len(inputedlines)):
            output_file.add_paragraph(inputedlines[i])
        output_file.save("output.docx")
