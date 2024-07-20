from gilded_rose import update_quality_list, Item, CONJURED

def test_conjured_quality_decreases_as_twice():
    items = [Item(CONJURED, 1, 10)]
    update_quality_list(items)
    assert 8 == items[0].quality

def test_conjured_quality_decreases_twice_as_fast_after_sell_in():
    items = [Item(CONJURED, 0, 10)]
    update_quality_list(items)
    assert 6 == items[0].quality
