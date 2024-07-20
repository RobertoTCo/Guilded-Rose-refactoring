from gilded_rose import update_quality_list, Item, SULFURAS

def test_sulfuras_sell_in_keeps_constant():
    items = [Item(SULFURAS, 4, 80)]
    update_quality_list(items)
    assert 4 == items[0].sell_in

def test_sulfuras_quality_keeps_constant():
    items = [Item(SULFURAS, 4, 80)]
    update_quality_list(items)
    assert 80 == items[0].quality
    
def test_sulfuras_quality_keeps_constant_after_sell_in():
    items = [Item(SULFURAS, 0, 80)]
    update_quality_list(items)
    assert 80 == items[0].quality