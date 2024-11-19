from address import Address
from mailing import Mailing

from_address = Address(
    postal_code="123456",
    city="Москва",
    street="Ленина",
    house="10",
    apartment="15"
)

to_address = Address(
    postal_code="654321",
    city="Санкт-Петербург",
    street="Невский проспект",
    house="20",
    apartment="25"
)

mailing = Mailing(
    to_address=to_address,
    from_address=from_address,
    cost=350,
    track="AB123456789RU"
)

print(mailing)