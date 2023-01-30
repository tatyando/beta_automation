x = int(input("Сколько деняк положить на счет: "))
y = int(input("На какой срок (в годах): "))

def bank(x, y):
    for i in range(0, y):
        x = x*1.1
    return x

print(bank(x, y))
