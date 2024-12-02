
# Write team member names here: 


'''
Base class file for building a set-associative cache
Credit: R. Martin (W&M), A. Jog (W&M), Ramulator (CMU)
'''

import numpy as np
from math import log
import random


class Cache:
    def __init__(self, cSize, ways=2, bSize=4):
        '''
        Keep ways > 1 to keep the cache set associative
        '''
        
        if(ways < 2):
            print("Emulating a Direct mapped Cache!")

        self.cacheSize = cSize  # Bytes
        self.ways = ways        # Default: 2 way (i.e., set associative)
        self.blockSize = bSize  # Default: 4 bytes (i.e., 1 word block)
        self.sets = cSize // bSize // ways

        self.blockBits = 0
        self.setBits = 0

        if (self.blockSize != 1):
            self.blockBits = int(log(self.blockSize, 2))

        if (self.sets != 1):
            self.setBits = int(log(self.sets, 2))

        self.cache = np.zeros((self.sets, self.ways, self.blockSize), dtype=np.int64)
        self.cache = self.cache - 1

        self.metaCache = np.zeros((self.sets, self.ways), dtype=np.int64)
        self.metaCache = self.metaCache - 1

        self.hit = 0
        self.miss = 0
        self.hitlatency = 5 # cycle

    def reset(self):
        self.cache = np.zeros((self.sets, self.ways, self.blockSize), dtype=np.int64)
        self.cache = self.cache - 1

        self.metaCache = np.zeros((self.sets, self.ways), dtype=np.int64)
        self.metaCache = self.metaCache - 1

        self.hit = 0
        self.miss = 0
        
    '''
    Warning: DO NOT EDIT ANYTHING ABOVE THIS LINE
    '''


    '''
    Returns the set number of an address based on the policy discussed in the class
    Do NOT change the function definition and arguments
    '''

    def find_set(self, address):
        block_number = address//self.blockSize
        set_index = block_number % self.sets
        return set_index

    '''
    Returns the tag of an address based on the policy discussed in the class
    Do NOT change the function definition and arguments
    '''

    def find_tag(self, address):
        block_number = address//self.blockSize
        tag = block_number//self.sets
        return tag

    '''
    Search through cache for address
    return True if found
    otherwise False
    Do NOT change the function definition and arguments
    '''

    def find(self, address):
        set_index = self.find_set(address)
        tag = self.find_tag(address)
        for way in range(self.ways):
            if self.metaCache[set_index][way] == tag:
                self.hit += 1
                return True
        self.miss += 1
        return False

    '''
    Load data into the cache. 
    Something might need to be evicted from the cache and send back to memory
    Do NOT change the function definition and arguments
    '''

    def load(self, address):
        set_index = self.find_set(address)
        tag = self.find_tag(address)

        for i in range(self.ways): # search for an empty way
            if self.metaCache[set_index][i] == -1: # -1 means empty
                self.cache[set_index][i] = address # load the address into the cache
                self.metaCache[set_index][i] = tag # load the tag into the metaCache

        ways = [self.metaCache[set_index][i] for i in range(self.ways)] # get all the tags in the set
        min_idx = min(ways) # take value at the LRU index/way
        lru = ways.index(min_idx) # find the LRU index/way

        self.cache[set_index][lru] = address
        self.metaCache[set_index][-1] = tag # insert from the end

        return None
