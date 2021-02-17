import io

#Methods

pixels = open("./dane.txt", "r", encoding="utf-8-sig")
pixelWriter = open("./wynik6_1.txt", "w", encoding="utf-8-sig")

allPixels = []

for line in pixels:
    pixelLine = line.split()
    for pixel in pixelLine:
        allPixels.append(int(pixel))

pixelWriter.write(str(max(allPixels)) + "\n")
pixelWriter.write(str(min(allPixels)))