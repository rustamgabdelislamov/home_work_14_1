from src.order import Order
from src.product import Product


def test_order(capsys):
    product = Product(
        name="Infinix",
        description="12GB",
        price=12000,
        quantity=5
    )
    order = Order(product, 2)

    assert order.total_price == 24000
