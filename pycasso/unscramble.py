#!/usr/bin/env python

import io
import os
import re
import sys
import math
from PIL import Image

from pycasso.shuffleseed import shuffle, unshuffle

class Canvas:
    def __init__(self, img, slice_size, seed=None):
        self.img = Image.open(img)
        self.slice_width, self.slice_height = slice_size
        self.seed = seed
        self.canvas = Image.new(
            mode="RGBA",
            size=(self.img_width, self.img_height),
            color=(255,255,255)
        )

        if slice_size == 0:
            raise ValueError("Invalid slice size specified: input must be greater than or equal to one.")

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
        return math.ceil(self.img_width / self.slice_width) * math.ceil(self.img_height / self.slice_height)

    def get_slices(self):
        slices = {}
        vertical_slices = math.ceil(self.img_width / self.slice_width)
        horizontal_slices = self.img_height / self.slice_height
        for i in range(0, self.total_parts):
            slice = {}
            row = int(i / vertical_slices)
            col = i - row * vertical_slices
            slice['x'] = col * self.slice_width
            slice['y'] = row * self.slice_height
            slice['width'] = (
                self.slice_width - (
                    0 if slice['x'] + int(self.slice_width) <= self.img_width else (
                        slice['x'] + int(self.slice_width)
                    ) - self.img_width
                )
            )
            slice['height'] = (
                self.slice_height - (
                    0 if slice['y'] + int(self.slice_height) <= self.img_height else (
                        slice['y'] + int(self.slice_height)
                    ) - self.img_height
                )
            )
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
        return i if (self.img_height % self.slice_height) == 0 else i + 1

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
        if not os.path.isabs(path):
            path = os.path.join(os.getcwd(), self.set_stdname(path))

        os.makedirs(os.path.dirname(path), exist_ok=True)
        return path

    def export(self, mode=None, path=None, format=None):
        try:
            if not mode:
                mode = "scramble"

            if not format:
                format = "png"

            if format == "jpg":
                format = "jpeg"

            if format == "jpeg":
                self.canvas = self.canvas.convert("RGB")

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

                    tiles = self.img.crop(
                        box=(
                            group['x'] + x,
                            group['y'] + y,
                            group['x'] + x + slices[g][i]['width'],
                            group['y'] + y + slices[g][i]['height']
                        )
                    )
                    self.canvas.paste(
                        tiles,
                        box=(
                            slices[g][i]['x'],
                            slices[g][i]['y'],
                            slices[g][i]['x'] + slices[g][i]['width'],
                            slices[g][i]['y'] + slices[g][i]['height']
                        )
                    )

            img_bytes = io.BytesIO()
            self.canvas.save(img_bytes, format)

            if path:
                if path.endswith('/'):
                    filename = f"pycasso-{self.img_filename}"
                    path = os.path.join(path, filename)

                output = f"{path}.{format}"

                with open(
                    self.set_directory(output)
                    if not os.path.exists(output) else output, 'wb'
                ) as file:
                    file.write(img_bytes.getvalue())

            return img_bytes

        except ValueError as error:
            raise SystemExit(f"Error: {error}")

    def close(self):
        self.img.close()
