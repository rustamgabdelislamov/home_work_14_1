from src.product import Product
from src.smartphone import Smartphone
from src.lawn_grass import LawnGrass


def test_print_mixin(capsys):
    Product(
        name="Infinix",
        description="12GB",
        price=12000,
        quantity=5
    )
    message = capsys.readouterr()
    assert message.out.strip() == 'Product(Infinix, 12GB, 12000, 5)'

    Smartphone("Samsung Galaxy S23 Ultra",
               "256GB, Серый цвет, 200MP камера",
               180000.0,
               5,
               95.5,
               "S23 Ultra",
               256,
               "Серый")
    message = capsys.readouterr()
    assert message.out.strip() == "Smartphone(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)"

    LawnGrass("Газонная трава",
              "Элитная трава для газона",
              500.0,
              20,
              "Россия",
              "7 дней",
              "Зеленый")
    message = capsys.readouterr()
    assert message.out.strip() == 'LawnGrass(Газонная трава, Элитная трава для газона, 500.0, 20)'
