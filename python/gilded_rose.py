# -*- coding: utf-8 -*-

MAX_QUALITY = 50
MIN_QUALITY = 0
SULFURAS_QUALITY = 80

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

def clamp_quality(item, max_quality=MAX_QUALITY):
    if item.name == "Sulfuras, Hand of Ragnaros":
        item.quality = SULFURAS_QUALITY
    else:
        if item.quality < MIN_QUALITY:
            item.quality = MIN_QUALITY
        if item.quality > max_quality:
            item.quality = max_quality

class ItemUpdater:
    """Base updater for normal items."""
    def __init__(self, item):
        self.item = item

    def update(self):
        self.update_quality()
        self.update_sell_in()
        if self.item.sell_in < 0:
            self.update_expired()
        clamp_quality(self.item)

    def update_quality(self):
        self.item.quality -= 1

    def update_sell_in(self):
        self.item.sell_in -= 1

    def update_expired(self):
        self.item.quality -= 1

class AgedBrieUpdater(ItemUpdater):
    """Aged Brie increases in quality as it ages."""
    def update_quality(self):
        self.item.quality += 1

    def update_expired(self):
        self.item.quality += 1

class SulfurasUpdater(ItemUpdater):
    """Sulfuras never changes."""
    def update(self):
        self.item.quality = SULFURAS_QUALITY  # Always 80
        pass

class BackstagePassUpdater(ItemUpdater):
    """Backstage passes increase in quality as sell_in approaches, drop to 0 after."""
    def update_quality(self):
        if self.item.sell_in > 10:
            self.item.quality += 1
        elif self.item.sell_in > 5:
            self.item.quality += 2
        elif self.item.sell_in > 0:
            self.item.quality += 3
        else:
            self.item.quality = 0  # Will be clamped in update()

    def update_expired(self):
        self.item.quality = 0

class ConjuredUpdater(ItemUpdater):
    """Conjured items degrade in quality twice as fast as normal items."""
    def update_quality(self):
        self.item.quality -= 2

    def update_expired(self):
        self.item.quality -= 2

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