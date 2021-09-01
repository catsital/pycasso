from pycasso import Canvas

img = 'examples/en_Pepper-and-Carrot_by-David-Revoy_E05P01_p2.png'
slice_size = 30
seed = 'Pycasso'
pyc = Canvas(img, slice_size, seed, 'en_Pepper-and-Carrot_by-David-Revoy_E05P01_p2_scramble')
pyc.export(mode='scramble')

# Canvas('examples/en_Pepper-and-Carrot_by-David-Revoy_E05P01_p2.png', 30, 'Pycasso', 'en_Pepper-and-Carrot_by-David-Revoy_E05P01_p2_scramble').export('scramble')

img = 'examples/en_Pepper-and-Carrot_by-David-Revoy_E05P01_p2_scramble.png'
pyc = Canvas(img, slice_size, seed, 'en_Pepper-and-Carrot_by-David-Revoy_E05P01_p2_unscramble')
pyc.export(mode='unscramble')

# Canvas('examples/en_Pepper-and-Carrot_by-David-Revoy_E05P01_p2_scramble.png', 30, 'Pycasso', 'en_Pepper-and-Carrot_by-David-Revoy_E05P01_p2_unscramble').export('unscramble')
