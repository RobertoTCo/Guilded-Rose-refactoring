# -*- coding: utf-8 -*-
from Item_class import Item
from typing import Iterable, Protocol

def decrease_item_sell_in(item: Item, days: int = 1) -> None:
    item.sell_in -= days

def decrease_item_quality(item: Item, amount: int = 1) -> None:
    item.quality = max(0, item.quality - amount)

def increase_item_quality(item: Item, amount: int = 1) -> None:
    item.quality = min(50, item.quality + amount)
class ItemUpdater(Protocol):
    def update_item_sell_in(self, item: Item) -> None: ...

    def update_item_quality(self, item: Item) -> None: ...
class DefaultItemUpdater(ItemUpdater):
    def update_item_sell_in(self, item: Item) -> None:
        decrease_item_sell_in(item, days=1)

    def update_item_quality(self, item: Item) -> None:
        decrease_item_quality(item, amount=1)
        if item.sell_in < 0:
            decrease_item_quality(item, amount=1)

class AgedBrieItemUpdater(DefaultItemUpdater):
    def update_item_quality(self, item: Item) -> None:
        increase_item_quality(item, amount=1)

class SulfurasItemUpdater(DefaultItemUpdater):
    def update_item_sell_in(self, item: Item) -> None:
        pass
    def update_item_quality(self, item: Item) -> None:
        pass
class BackstageItemUpdater(DefaultItemUpdater):
    def update_item_quality(self, item: Item) -> None:
        increase_item_quality(item, amount=1)
        if item.sell_in <= 10:
            increase_item_quality(item, amount=1)
        if item.sell_in <= 5:
            increase_item_quality(item, amount=1)
        if item.sell_in < 0:
            item.quality = 0
class ConjuredItemUpdater(DefaultItemUpdater):
    def update_item_quality(self, item: Item) -> None:
        decrease_item_quality(item, amount=2)
        if item.sell_in < 0:
            decrease_item_quality(item, amount=2)

# we need to create specifications for 4 items:
AGED_BRIE = "Aged Brie"
SULFURAS = "Sulfuras, Hand of Ragnaros"
BACKSTAGE = "Backstage passes to a TAFKAL80ETC concert"
CONJURED = "Conjured Mana Cake"

ITEM_UPDATER: dict[str, ItemUpdater] = {
    AGED_BRIE: AgedBrieItemUpdater(),
    SULFURAS: SulfurasItemUpdater(),
    BACKSTAGE: BackstageItemUpdater(),
    CONJURED: ConjuredItemUpdater(),
}

def update_quality_list(items: Iterable[Item]) -> None:
    for item in items:
        update_quality_selected_item(item)
    
def update_quality_selected_item(item: Item) -> None:
    updater = ITEM_UPDATER.get(item.name, DefaultItemUpdater())
    updater.update_item_sell_in(item)
    updater.update_item_quality(item)