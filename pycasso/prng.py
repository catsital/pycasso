from pycasso.constants import width, chunks, startdenom, significance, overflow, mask
from pycasso.cipher import ARC4

def seedrandom(seed):
    key = []
    shortseed = mixkey(seed, key)
    arc4 = ARC4(shortseed)

    def prng():
        arc4.main()
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
            x = rshift(x, 1)

        o = (n + x) / d

        return o

    return prng

def rshift(val, n): return (val % 0x100000000) >> n

def mixkey(seed, key):
    stringseed = seed + ''

    for j in range(0, len(stringseed)):
        key.insert(mask & j, ord(stringseed[j]))

    return key
