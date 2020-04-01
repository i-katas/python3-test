from pytest import approx


def test_serialize_state_with_tuple():
    product = Product(name='iPhone', price=5999)

    assert product.name == 'iPhone' and product.price == approx(5999)
    from pickle import loads, dumps

    restored = loads(dumps(product))
    assert restored.name == 'iPhone' and restored.price == approx(5999)


class Product:
    def __init__(self, name: str, price: float):
        self.name, self.price = name, price

    def __getstate__(self):
        return self.name, self.price

    def __setstate__(self, state):
        self.name, self.price = state
