# -*- coding: utf-8 -*-

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

class ItemUpdater:
    def __init__(self, item):
        self.item = item

    def update(self):
        self.update_quality()
        self.update_sell_in()
        if self.item.sell_in < 0:
            self.update_expired()

    def update_quality(self):
        if self.item.quality > 0:
            self.item.quality -= 1

    def update_sell_in(self):
        self.item.sell_in -= 1

    def update_expired(self):
        if self.item.quality > 0:
            self.item.quality -= 1

class AgedBrieUpdater(ItemUpdater):
    def update_quality(self):
        if self.item.quality < 50:
            self.item.quality += 1

    def update_expired(self):
        if self.item.quality < 50:
            self.item.quality += 1

class SulfurasUpdater(ItemUpdater):
    def update(self):
        pass  # Legendary, does not change

class BackstagePassUpdater(ItemUpdater):
    def update_quality(self):
        if self.item.quality < 50:
            self.item.quality += 1
            if self.item.sell_in < 11 and self.item.quality < 50:
                self.item.quality += 1
            if self.item.sell_in < 6 and self.item.quality < 50:
                self.item.quality += 1

    def update_expired(self):
        self.item.quality = 0

class ConjuredUpdater(ItemUpdater):
    def update_quality(self):
        degrade = 2
        if self.item.quality > 0:
            self.item.quality -= degrade
            if self.item.quality < 0:
                self.item.quality = 0

    def update_expired(self):
        degrade = 2
        if self.item.quality > 0:
            self.item.quality -= degrade
            if self.item.quality < 0:
                self.item.quality = 0

def get_updater(item):
    if item.name == "Aged Brie":
        return AgedBrieUpdater(item)
    if item.name == "Sulfuras, Hand of Ragnaros":
        return SulfurasUpdater(item)
    if item.name.startswith("Backstage passes"):
        return BackstagePassUpdater(item)
    if item.name.startswith("Conjured"):
        return ConjuredUpdater(item)
    return ItemUpdater(item)

class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            get_updater(item).update()
