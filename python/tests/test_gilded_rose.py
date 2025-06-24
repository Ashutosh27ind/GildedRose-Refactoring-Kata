# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def test_update_quality_on_sample_items(self):
        items = [
            Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
            Item(name="Aged Brie", sell_in=2, quality=0),
            Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
            Item(name="Conjured Mana Cake", sell_in=3, quality=6),
        ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        expected = [
            ("+5 Dexterity Vest", 9, 19),
            ("Aged Brie", 1, 1),
            ("Elixir of the Mongoose", 4, 6),
            ("Sulfuras, Hand of Ragnaros", 0, 80),
            ("Sulfuras, Hand of Ragnaros", -1, 80),
            ("Backstage passes to a TAFKAL80ETC concert", 14, 21),
            ("Backstage passes to a TAFKAL80ETC concert", 9, 50),
            ("Backstage passes to a TAFKAL80ETC concert", 4, 50),
            ("Conjured Mana Cake", 2, 4),
        ]
        for item, (exp_name, exp_sell_in, exp_quality) in zip(items, expected):
            self.assertEqual(exp_name, item.name)
            self.assertEqual(exp_sell_in, item.sell_in)
            self.assertEqual(exp_quality, item.quality)

if __name__ == '__main__':
    unittest.main()