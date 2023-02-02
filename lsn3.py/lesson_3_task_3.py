from AddressAndMailing import Mailing
from AddressAndMailing import Address


letter = Mailing(
    Address("123456", "Москва", " улица Ленина", "д. 13", "кв. 14"), 
    Address("654321", "СПБ", "улица Мира", "д. 15", "кв. 16"), 
    150, "track-777")

print("Отправление", letter.track, "из", letter.otkuda, "в", letter.to, "Стомость", letter.cost, "рублей")
