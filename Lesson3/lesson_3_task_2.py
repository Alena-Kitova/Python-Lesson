from smartphone import Smartphone

catalog = [
    Smartphone("iPhone", "16Pro", "+79899526241"),
    Smartphone("Samsung", "S25", "+79861248654"),
    Smartphone("Xiaomi", "15", "+79851258694"),
    Smartphone("Realme", "12Pro", "+79879456821"),
    Smartphone("Honor", "x8c", "+79899996565")
]

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model} - {smartphone.number}")
