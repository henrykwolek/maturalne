import io

def overallMoney(sales, cennik):
    sum = 0.0
    for sale in sales:
        s_Year = sale[0]
        for price in cennik:
            if s_Year == price[0]:
                quantity = sale[1].replace(",", ".")
                finalPrice = price[1].replace(",", ".")
                sum = sum + float(quantity) * float(finalPrice)

    return sum

sugarOpenerKilograms = open("./cukier.txt", "r", encoding='utf-8-sig')
sugarOpenerPrices = open("./cennik.txt", "r", encoding='utf-8-sig')
sugarWriter = open("./wynik4_2.txt", "w", encoding='utf-8-sig')

cennik = []
salesData = []

for price in sugarOpenerPrices:
    priceItem = price.split()
    cennik.append(priceItem)

#print(cennik)

for element in sugarOpenerKilograms:
    item = element.split()
    year = item[0].split("-")[0]
    kilograms = item[2]
    salesData.append([year, kilograms])

sugarWriter.write(str(overallMoney(salesData, cennik)))