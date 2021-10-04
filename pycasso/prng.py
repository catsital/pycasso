from time import time

from pycasso.constants import width, chunks, startdenom, significance, overflow, mask
from pycasso.cipher import ARC4

def seedrandom(seed):
    key = []
    shortseed = mixkey(seed, key)
    arc4 = ARC4(shortseed)
    arc4.main()

    def prng():
        n = arc4.g(chunks)
        d = startdenom
        x = 0

        while n < significance:
            n = (n + x) * width
            d *= width
            x = arc4.g(1)

        while n >= overflow:
            n /= 2
            d /= 2
            x = x >> 1

        o = (n + x) / d

        return o

    return prng

def mixkey(seed, key):
    if not seed:
        seed = time()

    for j in range(0, len(str(seed))):
        key.insert(mask & j, ord(str(seed)[j]))

    return key
