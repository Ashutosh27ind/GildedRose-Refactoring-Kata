import pytest
from gilded_rose import Item, GildedRose

def test_conjured_item_quality_degrades_twice_as_fast():
    item = Item("Conjured Mana Cake", 3, 6)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.quality == 4

def test_conjured_item_quality_never_negative():
    item = Item("Conjured Mana Cake", 3, 1)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.quality == 0

def test_conjured_item_degrades_by_4_after_sell_in():
    item = Item("Conjured Mana Cake", 0, 6)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.quality == 2

def test_conjured_item_quality_never_negative_after_expiry():
    item = Item("Conjured Mana Cake", 0, 3)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.quality == 0