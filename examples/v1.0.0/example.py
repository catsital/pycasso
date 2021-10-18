from pycasso import Canvas

img = '../examples/en_Pepper-and-Carrot_by-David-Revoy_E05P01_p2.png'
slice_size = 30
seed = 'Pycasso'
pyc = Canvas(img, slice_size, seed)
pyc.export(mode='scramble', path='en_Pepper-and-Carrot_by-David-Revoy_E05P01_p2_v1.0.0-prng.png')

# Canvas(img, slice_size, seed).export('scramble', 'en_Pepper-and-Carrot_by-David-Revoy_E05P01_p2_v1.0.0-prng.png')

img = 'en_Pepper-and-Carrot_by-David-Revoy_E05P01_p2_v1.0.0-prng.png'
slice_size = 30
seed = 'Pycasso'
pyc = Canvas(img, slice_size, seed)
pyc.export(mode='unscramble', path='en_Pepper-and-Carrot_by-David-Revoy_E05P01_p2_v1.0.0-prng-unscramble.png')

# Canvas(img, slice_size, seed).export('unscramble', 'en_Pepper-and-Carrot_by-David-Revoy_E05P01_p2_v1.0.0-prng-unscramble.png')
