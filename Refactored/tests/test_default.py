from gilded_rose import update_quality_list, Item

def test_item_records_name():
    items = [Item("foo", 0, 0)]
    assert "foo" == items[0].name

def test_item_records_sell_in():
    items = [Item("foo", 0, 0)]
    assert 0 == items[0].sell_in

def test_item_records_quality():
    items = [Item("foo", 0, 0)]
    assert 0 == items[0].quality

def test_item_keeps_name():
    items = [Item("foo", 0, 0)]
    update_quality_list(items)
    assert "foo" == items[0].name

def test_item_decreases_sell_in_when_called():
    items = [Item("foo", 0, 0)]
    update_quality_list(items)
    assert -1 == items[0].sell_in

def test_item_decreases_quality():
    items = [Item("foo", 1, 1)]
    update_quality_list(items)
    assert 0 == items[0].quality

def test_item_decreases_quality_twice_as_fast_after_sell_by_date():
    items = [Item("foo", 0, 2)]
    update_quality_list(items)
    assert 0 == items[0].quality

def test__item_quality_never_negative():
    items = [Item("foo", 0, 0)]
    update_quality_list(items)
    assert 0 == items[0].quality

def test_item_quality_never_higher_than_50():
    items = [Item("Aged Brie", 0, 50)]
    update_quality_list(items)
    assert 50 == items[0].quality