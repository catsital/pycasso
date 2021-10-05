import os
import re
import math
import logging
from PIL import Image

from pycasso.shuffleseed import shuffle, unshuffle

log = logging.getLogger(__name__)

class Canvas:
    def __init__(self, img, slice_size, seed=None):
        self.img = Image.open(img)
        self.slice_size = abs(slice_size)
        self.seed = seed
        self.canvas = Image.new(mode="RGBA",
                                size=(self.img_width, self.img_height),
                                color=(255,255,255))

        if slice_size == 0:
            log.error("Invalid slice size specified: input must be greater than or equal to one.")
            raise SystemExit

    @property
    def img_width(self):
        return self.img.size[0]

    @property
    def img_height(self):
        return self.img.size[1]

    @property
    def img_filename(self):
        return self.get_basename(self.img.filename)

    @property
    def total_parts(self):
        return math.ceil(self.img_width / self.slice_size) * math.ceil(self.img_height / self.slice_size)

    def get_slices(self):
        slices = {}
        vertical_slices = math.ceil(self.img_width / self.slice_size)
        horizontal_slices = self.img_height / self.slice_size
        for i in range(0, self.total_parts):
            slice = {}
            row = int(i / vertical_slices)
            col = i - row * vertical_slices
            slice['x'] = col * self.slice_size
            slice['y'] = row * self.slice_size
            slice['width'] = (self.slice_size - (0 if slice['x'] + self.slice_size <= self.img_width else (slice['x'] + self.slice_size) - self.img_width))
            slice['height'] = (self.slice_size - (0 if slice['y'] + self.slice_size <= self.img_height else (slice['y'] + self.slice_size) - self.img_height))
            if '{0}-{1}'.format(slice['width'], slice['height']) not in slices.keys():
                slices['{0}-{1}'.format(slice['width'], slice['height'])] = []
            slices['{0}-{1}'.format(slice['width'], slice['height'])].append(slice)

        return slices

    def get_cols_in_group(self, slices):
        if len(slices) == 1:
            return 1
        t = 'init'
        for i in range(0, len(slices)):
            if t == 'init':
                t = slices[i]['y']
            if t != slices[i]['y']:
                return i
                break
        return i if (self.img_height % self.slice_size) == 0 else i + 1

    def get_group(self, slices):
        this = {}
        this['slices'] = len(slices)
        this['cols'] = self.get_cols_in_group(slices)
        this['rows'] = len(slices) / this['cols']
        this['width'] = slices[0]['width'] * this['cols']
        this['height'] = slices[0]['height'] * this['rows']
        this['x'] = slices[0]['x']
        this['y'] = slices[0]['y']
        return this

    @staticmethod
    def get_basename(filename):
        return os.path.basename(filename)

    @staticmethod
    def set_stdname(filename):
        pattern = re.compile(r'[?"|:<>*]', flags=re.VERBOSE)
        return pattern.sub("", str(filename))

    def set_directory(self, path):
        filename = f"pycasso-{self.img_filename}"
        if path:
            if not os.path.isabs(path):
                path = os.path.join(os.getcwd(), path)
        else:
            path = os.path.join(os.getcwd(), filename)

        if path.endswith('/'):
            path = os.path.join(path, filename)

        os.makedirs(os.path.dirname(path), exist_ok=True)
        return path

    def export(self, mode='scramble', path=None):
        try:
            path = self.set_stdname(path)
            slices = self.get_slices()

            for g in slices:
                group = self.get_group(slices[g])
                shuffle_ind = []
                for i in range(0, len(slices[g])):
                    shuffle_ind.append(i)
                if mode == 'unscramble':
                    shuffle_ind = unshuffle(shuffle_ind, self.seed)
                if mode == 'scramble':
                    shuffle_ind = shuffle(shuffle_ind, self.seed)

                for i in range(0, len(slices[g])):
                    s = shuffle_ind[i]
                    row = int(s / group['cols'])
                    col = s - row * group['cols']
                    x = col * slices[g][i]['width']
                    y = row * slices[g][i]['height']

                    tiles = self.img.crop(box=(group['x'] + x,
                                               group['y'] + y,
                                               group['x'] + x + slices[g][i]['width'],
                                               group['y'] + y + slices[g][i]['height']))

                    self.canvas.paste(tiles, box=(slices[g][i]['x'],
                                                  slices[g][i]['y'],
                                                  slices[g][i]['x'] + slices[g][i]['width'],
                                                  slices[g][i]['y'] + slices[g][i]['height']))

            filename = self.set_directory(path)

            if filename.endswith(".jpeg") or filename.endswith(".jpg"):
                self.canvas = self.canvas.convert("RGB")

            self.canvas.save(filename)

        except ValueError as error:
            log.error("Error encountered - {}".format(error))
