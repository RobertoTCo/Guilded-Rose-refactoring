from gilded_rose import update_quality_list, Item, AGED_BRIE

def test_aged_brie_quality_does_not_decrease():
    items = [Item(AGED_BRIE, 0, 10)]
    assert 9 < items[0].quality

def test_aged_brie_quality_increases_by_one():
    items = [Item(AGED_BRIE, 1, 10)]
    update_quality_list(items)
    assert 11 == items[0].quality

def test_aged_brie_increase_by_one_after_sell_in():
    items = [Item(AGED_BRIE, 0, 10)]
    update_quality_list(items)
    assert 11 == items[0].quality