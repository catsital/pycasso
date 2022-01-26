from pycasso.constants import width, mask


class ARC4:
    def __init__(self, key):
        self.key = key

        global keylen, t, i, j, s
        keylen = len(self.key)
        t = None
        i = 0
        j = self.i = self.j = 0
        s = self.S = []

    def main(self):
        global i, j

        while i < width:
            s.append(i)
            i += 1

        for i in range(width):
            t = s[i]
            j = mask & (j + self.key[i % keylen] + t)
            s[i] = s[j]
            s[j] = t

        self.g(width)

    def g(self, count):
        t = None
        r = 0
        i = self.i
        j = self.j
        s = self.S

        while count:
            i = mask & (i + 1)
            t = s[i]
            j = mask & (j + t)
            s[i] = s[j]
            s[j] = t
            r = r * width + s[mask & (s[i] + s[j])]
            count -= 1

        self.i = i
        self.j = j

        return r
