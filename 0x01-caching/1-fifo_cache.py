#!/usr/bin/env python
""" Implement a FIFO cache algorithm
"""
from base_caching import BaseCaching
from collections import deque


class FIFOCache(BaseCaching):
    """ Implement a FIFO cache algorithm
    """

    def __init__(self):
        super().__init__()
        self.queue = deque(maxlen=BaseCaching.MAX_ITEMS)

    def put(self, key, item):
        """Assign to the dictionary the item value to the key"""
        if key is None or item is None:
            return
        
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            oldest_key = self.queue.popleft()
            del self.cache_data[oldest_key]
            print("DISCARD: {}".format(oldest_key))
        
        self.queue.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """ return the value in the dictionary link to the
        given key"""
        if (key is None) or (key not in self.cache_data):
            return None
        return self.cache_data[key]
