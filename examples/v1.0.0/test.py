from pycasso import Canvas

img = '../examples/en_Pepper-and-Carrot_by-David-Revoy_E05P01_p2.png'
slice_size = 30
seed = 'Pycasso'
pyc = Canvas(img, slice_size, seed, 'en_Pepper-and-Carrot_by-David-Revoy_E05P01_p2_v1.0.0-prng')
pyc.export(mode='scramble')

# Canvas(img, slice_size, seed, 'en_Pepper-and-Carrot_by-David-Revoy_E05P01_p2_v1.0.0-prng').export('scramble')

img = 'en_Pepper-and-Carrot_by-David-Revoy_E05P01_p2_v1.0.0-prng.png'
slice_size = 30
seed = 'Pycasso'
pyc = Canvas(img, slice_size, seed, 'en_Pepper-and-Carrot_by-David-Revoy_E05P01_p2_v1.0.0-prng-unscramble')
pyc.export(mode='unscramble')

# Canvas(img, slice_size, seed, 'en_Pepper-and-Carrot_by-David-Revoy_E05P01_p2_v1.0.0-prng').export('unscramble')
