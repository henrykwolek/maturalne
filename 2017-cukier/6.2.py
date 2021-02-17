import io

#Methods

pixels = open("./dane.txt", "r", encoding="utf-8-sig")
pixelWriter = open("./wynik6_2.txt", "w", encoding="utf-8-sig")

symetryczne = 0
lineCount = 0

for line in pixels:
    lineCount += 1
    pixelLine = line.split()
    i = 0
    match = 0
    while i < 160:
        if pixelLine[i] == pixelLine[len(pixelLine) - i - 1]:
            match += 1
        i += 1
    if match == 160:
        symetryczne += 1

pixelWriter.write(str(lineCount - symetryczne))