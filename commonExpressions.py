import sqlite3
import time
from openpyxl import Workbook
from docx import Document
import matplotlib.pyplot as plt
import numpy as np


class CommonExpressions:
    punctuations = [".", "?", ";", ":", "!", "(", ")", ",", "\\", "\"", "-",
                    "--", "”", "“", "\n", "\t", "—", "'", "  "]
    suffices_tr = ["'nin", "'nın", "'a", "'e", "'i",
                    "'in", "'ın", "'ım", "'im", "'den", "'dan", "'ten",
                    "'tan", "'te", "'ta", "'i" "'de", "'da",
                    "’nin", "’nın", "’a", "’e",
                    "’in", "’ın", "’ım", "’im", "’den", "’dan", "’ten",
                    "’tan", "’te", "’ta", "’i", "’de", "’da"]
    conjunctions_tr = [" ve ", " ama ", " ki ", " de ", " da ", " mi "]
    conjunctions_en = [" and ", " but ", " or ", " so ", " therefore ", " thus "]
    suffices_en = ["'s", "'re", "n't"]
    trtolatin = ["I"]
    trtolatindict = {"I": "i"}
    conjunctions = {"Turkish":conjunctions_tr, "English":conjunctions_en}
    suffixes = {"Turkish":suffices_tr, "English":suffices_en}
    lang_sep = {"suffix":suffixes, "conjunctions":conjunctions}


def prepare(stringObject, tr = "no"):
    hold = stringObject
    if tr == "yes":
        for i in range(len(CommonExpressions.trtolatin)):
            hold = hold.replace(CommonExpressions.trtolatin[i], CommonExpressions.trtolatindict[CommonExpressions.trtolatin[i]])
    for i in range(len(CommonExpressions.punctuations)):
        hold = hold.replace(CommonExpressions.punctuations[i], " ")
    hold = hold.lower()
    output = hold.split(" ")
    outputResWordSpace = output.count('')
    for i in range(outputResWordSpace):
        output.remove('')
    return output


def save(indexed, keysindex, outputtype = "txt"):
    if outputtype == "txt" or outputtype == "csv":
        output = "word,count"
        for i in range(len(keysindex)):
            output = output + "\n{},{}".format(keysindex[i], str(indexed[keysindex[i]]))
        fileoutput = open("output{}.{}".format(outputtype ,time.ctime().replace(":", "-")), "w")
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

def strip(input_, lang="Turkish", method="suffix", toBeRemoved = []):
    if toBeRemoved == []:
        toBeRemoved = CommonExpressions.lang_sep[method][lang]
    for i in range(len(toBeRemoved)):
        input_ = input_.replace(toBeRemoved[i], "")
    return input_

def draw(data):
    words = data.keys()
    count = data.values()
    xaxis = []
    for i in range(len(words)):
        xaxis.append(i)
    plt.bar(xaxis, count)
    plt.xticks(xaxis, words)
    plt.ylabel('Number of usage')
    plt.xlabel('Words')
    plt.title('Word Usage Graph')
    plt.show()
