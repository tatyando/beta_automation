month = int(input("Номер месяца, пожалуйста: "))

def month_to_season(month): 
    if (month == 1) or (month == 2) or (month == 12):
        print("Это зима :(")
    elif (month == 3) or (month == 4) or (month == 5):
        print("Это весна :)")
    elif (month == 6) or (month == 7) or (month == 8):
        print("Это лето :)")
    elif (month == 9) or (month == 10) or (month == 11):
        print("Это осень :(")
    else: 
        print("В году 12 месяцев, чухня")

month_to_season(month)
