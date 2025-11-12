nominal_banknotes = [5000,2000,1000,500,200,100]
money = int(input("Введите сумму"))
if money <= 0 or money % 100 != 0:
    print("введите число больше 0 и кратное 100")
else:
    for i in nominal_banknotes:
        count_banknotes = money // i
        money %= i
        print(f"Будет выдано купюр номинал в {i} - {count_banknotes}")