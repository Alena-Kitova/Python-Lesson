from address import Address
from mailing import Mailing

to_address = Address(612100, "Екатеринбург", "Рябинина", "28", "25")
from_address = Address(512325, "Пермь", "Ленина", "155", "205")
mailing = Mailing(to_address, from_address, 2500, 1245666)

print(mailing)
