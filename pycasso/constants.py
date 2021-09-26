import math

width = 256
chunks = 6
digits = 52
startdenom = int(math.pow(width, chunks))
significance = int(math.pow(2, digits))
overflow = significance * 2
mask = width - 1
