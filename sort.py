# Input file is plain txt file with indexes/names and scores


from collections import namedtuple

Person = namedtuple("Person", ["index", "score"])

def sortKey(e):
    return float(e.score)


fileName_in = input("Input file name: ")

file_in = open(fileName_in, "r")
file_out = open(fileName_in[0:-4] + "_sorted.txt", "w")

personList = []

indexCol = int(input("index column number: ")) - 1
scoreCol = int(input("score column number: ")) - 1

for line in file_in:
    l = line.split()
    if len(l) >= 2:
        personList.append(Person(l[indexCol], l[scoreCol]))

personList.sort(reverse=True, key=sortKey)

prevPersonScore = 0
prevPersonPos = 0

for i in range(0,len(personList)):
    if personList[i].score != prevPersonScore:
        prevPersonScore = personList[i].score
        prevPersonPos = i
    print(str(prevPersonPos+1) + " - " + personList[i].index + " " + personList[i].score)
    file_out.write(str(prevPersonPos+1) + " - " + personList[i].index + " " + personList[i].score + "\n")

file_in.close()
file_out.close()