import math


length = float(input("Введите сторону квадрата: "))

def square_area(length): 
    area = length*length
    print("Площадь квадрата:", area)

square_area(math.ceil(length))
