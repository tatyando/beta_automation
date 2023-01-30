lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
print(sum(lst)) # ну а зачем изобретать велосипеды


# ну так уж и быть
lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]

def summa():
    summ = 0
    for i in range(len(lst)):
        summ = summ + int(lst[i])
    print(summ)

summa()
