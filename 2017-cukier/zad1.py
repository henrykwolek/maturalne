import io

def findAllNip(bigArr):
    nipList = []
    for row in bigArr:
        nip = row[1]
        if not nip in nipList:
            nipList.append(nip)
    return nipList

def ileKtoKupil(nip, bigArr):
    suma = 0
    for row in bigArr:
        nipNum = row[1]
        if nipNum == nip:
            suma = suma + int(row[2])
    return suma

sugarOpener = open("./cukier.txt", "r")
sugarWriter = open("./wynik4_1.txt", "w", encoding="utf-8")

bigArr = []
interesy = []
for line in sugarOpener:
    bigArr.append(line.split())

for element in findAllNip(bigArr):
    interesy.append([element, int(ileKtoKupil(element, bigArr))])

posortowaneInteresy = sorted(interesy, key = lambda x: x[1])

sugarWriter.write(posortowaneInteresy[len(posortowaneInteresy) - 3][0] + " => " + str(posortowaneInteresy[len(posortowaneInteresy) - 3][1]) + "\n")
sugarWriter.write(posortowaneInteresy[len(posortowaneInteresy) - 2][0] + " => " + str(posortowaneInteresy[len(posortowaneInteresy) - 2][1]) + "\n")
sugarWriter.write(posortowaneInteresy[len(posortowaneInteresy) - 1][0] + " => " + str(posortowaneInteresy[len(posortowaneInteresy) - 1][1]) + "\n")