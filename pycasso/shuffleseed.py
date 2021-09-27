import math

from pycasso.prng import seedrandom

def islist(this):
    return type(this) is list

def seedrand(seed, min, max):
    return math.floor(seed() * (max - min + 1)) + min

def shuffle(list, seed=None):
    if not islist(list):
        return None

    size = len(list)
    rng = seedrandom(seed)
    resp = []
    keys = []

    for i in range(0, size):
        keys.append(i)

    for i in range(0, size):
        r = seedrand(rng, 0, len(keys)-1)
        g = keys[r]
        splice(keys, r, 1)
        resp.append(list[g])

    return resp

def unshuffle(list, seed=None):
    if not islist(list):
        return None

    size = len(list)
    rng = seedrandom(seed)
    resp = []
    map = []
    keys = []

    for i in range(0, size):
        resp.append(None)
        keys.append(i)

    for i in range(0, size):
        r = seedrand(rng, 0, len(keys)-1)
        g = keys[r]
        splice(keys, r, 1)
        resp[g] = list[i]

    return resp

def splice(target, start, delete_count=None, *items):
    if delete_count == None:
        delete_count = len(target) - start

    total = start + delete_count
    removed = target[start:total]
    target[start:total] = items

    return removed
