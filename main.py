
valuta = "₸"
summa = 0
count = 0
buy = 0
cancellation = 0

summa = int(input("Укажите бюджет для покупок: "))
startSumma = summa

while (summa > 0 and buy != -1):
    print("Остаток:", summa, valuta)
    buy = int(input("Введите стоимость товара: "))

    if (buy > summa):
        print("*" * 43)
        print("Стоимость покупки не может превышать бюджет.")
        print("*" * 43)
    elif (buy > 0):
        summa -= buy
        count += 1
        if (summa < 200 and summa > 0):
            print(f"Внимание! Осталось {summa} {valuta}!")

print(f"Вы потратили {startSumma - summa} {valuta}.")
print(f"При этом совершили {count} покупок.")