from commonExpressions import CommonExpressions, prepare


file_ = input("Welcome to the Linguistly 0.1, please write the directory of"
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
for i in range(len(keysindex)):
    output = output + "\n {}  - {}".format(keysindex[i], str(indexed[keysindex[i]]))

file_output = open("output.txt", "w")
file_output.write(output)
file_output.close()
