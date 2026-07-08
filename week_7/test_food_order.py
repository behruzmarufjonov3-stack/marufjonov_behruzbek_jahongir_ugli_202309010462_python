from food_order import calculate_total

def test_order1():
    assert calculate_total(10, 2) == 20

# test if total food order is equal to 30
def test_order_30():
    assert calculate_total(15, 2) == 30

# test if total food order is equal to 100
def test_order_100():
    assert calculate_total(20, 5) == 100

# test if total food order is equal to 10
def test_order_10():
    assert calculate_total(5, 2) == 10

# test if total food order is equal to "invalid price"
def test_invalid_price():
    assert calculate_total(-5, 2) == "invalid price"
    assert calculate_total(0, 2) == "invalid price"

# test if total food order is equal to "invalid quantity"
def test_invalid_quantity():
    assert calculate_total(10, -1) == "invalid quantity"
    assert calculate_total(10, 0) == "invalid quantity"