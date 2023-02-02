from Smartphone import Smartphone


catalog = []

iPhone = Smartphone("Apple", "iPhone 13 Pro", "8-999-999-99-99")
Samsung = Smartphone("Samsung", "Galaxy Fold", "8-888-888-88-88")
Huawei = Smartphone("Huawei", "Mate 100500", "8-777-777-77-77")
top_za_svoi_dengi = Smartphone("Xiaomi", "Redmi Note 9", "8-666-666-66-66")
connecting_people = Smartphone("Nokia", "3310", "8-555-555-55-55")


catalog.append(iPhone)
catalog.append(Samsung)
catalog.append(Huawei)
catalog.append(top_za_svoi_dengi)
catalog.append(connecting_people)


for i in catalog:
    print(Smartphone.describe(i))
