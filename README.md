# Pycasso

[![Downloads](https://pepy.tech/badge/image-scramble)](https://pepy.tech/project/image-scramble)
[![Latest PyPI release](https://badgen.net/pypi/v/image-scramble)](https://pypi.org/project/image-scramble/)
[![Latest Github release](https://badgen.net/github/release/catsital/pycasso)](https://github.com/catsital/pycasso/releases/latest)
[![License](https://badgen.net/github/license/catsital/pycasso)](https://github.com/catsital/pycasso/blob/main/LICENSE)
[![Build](https://github.com/catsital/pycasso/actions/workflows/python-package.yml/badge.svg)](https://github.com/catsital/pycasso/actions/workflows/python-package.yml)
[![Deploy](https://github.com/catsital/pycasso/actions/workflows/deploy-main.yml/badge.svg)](https://github.com/catsital/pycasso/actions/workflows/deploy-main.yml)

Split image into tiles and scramble/unscramble them based on a seed. The demo application can be found at [https://image-scramble.herokuapp.com](https://image-scramble.herokuapp.com).

---

### Scramble

Using scramble mode on [this sample image](./examples/en_Pepper-and-Carrot_by-David-Revoy_E05P01_p2.png) will produce the following output:

![example_scramble](./examples/v1.0.0/en_Pepper-and-Carrot_by-David-Revoy_E05P01_p2_v1.0.0-prng.png)

### Unscramble

To revert the image to its original state, use the same `seed` and `slice_size` on unscramble mode.

![example_unscramble](./examples/v1.0.0/en_Pepper-and-Carrot_by-David-Revoy_E05P01_p2_v1.0.0-prng-unscramble.png)

## Credits

* Pycasso is a Python version of [webcaetano/image-scramble](https://github.com/webcaetano/image-scramble) and [webcaetano/shuffle-seed](https://github.com/webcaetano/shuffle-seed). This also uses a stripped-down port of [davidbau/seedrandom](https://github.com/davidbau/seedrandom) to initialize the PRNG.

* Sample image is taken from [Pepper&Carrot](https://peppercarrot.com/) by David Revoy licensed under [CC BY 4.0](https://www.peppercarrot.com/en/license/index.html).

## Setup

### Install from PyPI

```bash
$ pip install image-scramble
```

### Install from source

*  First, you should get a copy of this project in your local machine by either downloading the zip file or cloning the repository. `git clone https://github.com/catsital/pycasso.git`
* `cd` into `pycasso` directory.
* Run `python setup.py install` to install package.

## Usage

### Web application

* Run `python app/app.py`

### Docker

* Build from local using:

```bash
$ docker build -t "image-scramble" .
$ docker --name pycasso -p 5000:5000 -d image-scramble
```

* Get image from [Docker Hub]('https://hub.docker.com/r/catsital/image-scramble'):

```bash
$ docker pull catsital/image-scramble
```

### Command-line utility

```bash
$ pycasso image_input.png image_output scramble
```

This will produce a scrambled image with seed based on your current system time. Hence, the output will be completely unpredictable and irreversible. Use the options `-n` for `slice_size`, `-f` for `format`, and `-s` for `seed`, like so:

```bash
$ pycasso image_input.png image_output scramble -n 50 50 -s seed -f jpeg
```

### Script

Initialize a `Canvas` and use scramble on `export` by:

```python
from pycasso import Canvas
Canvas('image_input.png', (30, 30), 'seed').export('scramble', 'image_output', 'jpeg')
```
