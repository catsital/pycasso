from pycasso import Canvas

img = 'examples/en_Pepper-and-Carrot_by-David-Revoy_E05P01_p2.png'
slice_size = 30
seed = 'Pycasso'
pyc = Canvas(img, slice_size, seed)
pyc.export(mode='scramble', path='en_Pepper-and-Carrot_by-David-Revoy_E05P01_p2_scramble.png')

# Canvas('examples/en_Pepper-and-Carrot_by-David-Revoy_E05P01_p2.png', 30, 'Pycasso').export('scramble', 'en_Pepper-and-Carrot_by-David-Revoy_E05P01_p2_scramble.png')

img = 'examples/en_Pepper-and-Carrot_by-David-Revoy_E05P01_p2_scramble.png'
pyc = Canvas(img, slice_size, seed)
pyc.export(mode='unscramble', path='en_Pepper-and-Carrot_by-David-Revoy_E05P01_p2_unscramble.png')

# Canvas('examples/en_Pepper-and-Carrot_by-David-Revoy_E05P01_p2_scramble.png', 30, 'Pycasso').export('unscramble', 'en_Pepper-and-Carrot_by-David-Revoy_E05P01_p2_unscramble.png')
