from gilded_rose import update_quality_list, Item, BACKSTAGE

def test_backstage_quality_does_not_decrease():
    items = [Item(BACKSTAGE, 12, 10)]
    assert 9 != items[0].quality

def test_backstage_quality_increases():
    items = [Item(BACKSTAGE, 12, 10)]
    update_quality_list(items)
    assert 11 == items[0].quality

def test_backstage_quality_increases_by_two_when_sell_between_10_and_5_days():
    items = [Item(BACKSTAGE, 10, 10)]
    update_quality_list(items)
    assert 12 == items[0].quality

def test_backstage_quality_increases_by_three_when_sell_between_5_and_0_days():
    items = [Item(BACKSTAGE, 5, 10)]
    update_quality_list(items)
    assert 13 == items[0].quality

def test_backstage_quality_drops_to_zero_after_sell_date():
    items = [Item(BACKSTAGE, 0, 10)]
    update_quality_list(items)
    assert 0 == items[0].quality
