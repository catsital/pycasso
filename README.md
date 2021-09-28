# Pycasso

Image obfuscator with seed. [1]

## Example

![example_scramble](./examples/en_Pepper-and-Carrot_by-David-Revoy_E05P01_p2_scramble.png)

Using this image [2] with `scramble` mode on `export`:

```python
img = 'examples/en_Pepper-and-Carrot_by-David-Revoy_E05P01_p2_pycasso.png'
slice_size = 30
seed = 'Pycasso'
```

With `unscramble` using the same `seed` and `slice_size` to revert the image to its unscrambled state:

![example_unscramble](./examples/en_Pepper-and-Carrot_by-David-Revoy_E05P01_p2_unscramble.png)

## References

[1] Pycasso is a partial port of [image-scramble](https://github.com/webcaetano/image-scramble), a JavaScript/Node.js module for scrambling/unscrambling images, and [shuffle-seed](https://github.com/webcaetano/shuffleseed), likewise a module that shuffles/unshuffles an array with seed, by [Andre Caetano](https://github.com/webcaetano). The original module uses [seedrandom](https://github.com/davidbau/seedrandom) to initialize the PRNG, whilst this version uses a basic implementation of the `random` module from the Python standard library. Needless to say, running the same seed on both versions will result to two distinct output.

[2] Sample image is taken from [Pepper & Carrot](https://peppercarrot.com/) by David Revoy licensed under [CC BY 4.0](https://www.peppercarrot.com/en/license/index.html).

## Getting Started

### Prerequisites
* Python 3.8+

### Setup
*  First, you should get a copy of this project in your local machine by either downloading the zip file or cloning the repository. `git clone https://github.com/catsital/pycasso.git`
* `cd` into `pycasso` directory.
* Run `python setup.py install` to install package.

#### Install from development
Install directly from the development source with pip by `python -m pip install git+https://github.com/catsital/pycasso@develop`


## Usage

Initialize a `Canvas` and use `scramble` on `export` by:

```python
import pycasso
img = 'image_input.png'
slice_size = 50
seed = 'seed'
canvas = pycasso.Canvas(img, slice_size, seed, 'image_output')
canvas.export(mode='scramble')
```

Or a plain one-liner:
```python
pycasso.Canvas('image_input.png', 50, 'seed', 'image_output').export()
```

Simply use `requests` to open images from web.

```python
import requests
img = requests.open('image_url', stream=True).raw
```

## Params

**img**
* Path to image source

**slice_size**
* Size of each slice

**seed**
* Seed to shuffle in same sequence

**output**
* Output file name

## Modes

**scramble** *default*
* Splits and scrambles image into tiles

**unscramble**
* Reverts the image to its original form given the same seed

*Modes can be used interchangeably and conversely perform their original functions. (i.e. If you use unscramble to scramble an image, it will scramble the image. Consequently you should use scramble to unscramble the image to its original form.)*

## License

```
Copyright (c) 2021 Julia Torres
Copyright (c) 2015 Andre Caetano

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
