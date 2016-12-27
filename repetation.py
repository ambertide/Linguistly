from commonExpressions import CommonExpressions, prepare, save


file_ = input("Welcome to the Linguistly, please write the directory of"
    " the document you wish to analyize: ")
file = open(file_, "r")
initdata = file.read()
file.close()
findata = prepare(initdata)

indexed = {}
indata = list(set(findata))
for i in range(len(indata)):
    indexed[indata[i]] = findata.count(indata[i])

keysindex = list(indexed)
output = ""
save(indexed, keysindex, outputtype="txt")
save(indexed, keysindex, outputtype="sqlite3")
