#!/usr/bin/env python
""" Implement a LFU cache algorithm
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LFUCache(BaseCaching):
    """ Implement a FIFO cache algorithm
    """

    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()
        self.frequency = {}

    def put(self, key, item):
        """Assign to the dictionary the item value to the key"""
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            least_freq = min(self.frequency.values())
            frequencies = self.frequency.items()
            least_freq_keys = [k for k, v in frequencies if v == least_freq]

            lru_key = next(iter(self.cache_data))
            for key in least_freq_keys:
                if key in self.cache_data:
                    lru_key = key
                break

            del self.cache_data[lru_key]
            del self.frequency[lru_key]
            print("DISCARD: {}".format(lru_key))
        self.cache_data[key] = item
        self.frequency[key] = self.frequency.get(key, 0) + 1

    def get(self, key):
        """ return the value in the dictionary link to the
        given key"""
        if (key is None) or (key not in self.cache_data):
            return None
        self.frequency[key] = self.frequency.get(key, 0) + 1
        return self.cache_data[key]
