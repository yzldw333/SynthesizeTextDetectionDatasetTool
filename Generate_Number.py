#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
#
#  FreeType high-level python API - Copyright 2011-2015 Nicolas P. Rougier
#  Distributed under the terms of the new BSD license.
#
# -----------------------------------------------------------------------------
from freetype import *
from PIL import Image
import numpy as np
import numpy
import matplotlib.pyplot as plt
def GenerateNumberPic(text='10',textsize=100,color=(1,0,0),font='./Vera.ttf'):

    face = Face(font)
    face.set_char_size( textsize*64 )
    slot = face.glyph
    RGBA = [('R', float), ('G', float), ('B', float), ('A', float)]
    # First pass to compute bbox
    width, height, baseline = 0, 0, 0
    previous = 0
    length=len(text)
    for i,c in enumerate(text):
        face.load_char(c)
        bitmap = slot.bitmap
        height = max(height,
                     bitmap.rows + max(0,-(slot.bitmap_top-bitmap.rows)))
        baseline = max(baseline, max(0,-(slot.bitmap_top-bitmap.rows)))
        kerning = face.get_kerning(previous, c)
        width += (slot.advance.x >> 6) + (kerning.x >> 6)
        previous = c

    img = numpy.zeros((height,width), dtype=RGBA)
    Z = numpy.zeros((height,width),dtype='float32')
    # Second pass for actual rendering
    x, y = 0, 0
    previous = 0
    for c in text:
        face.load_char(c)
        bitmap = slot.bitmap
        top = slot.bitmap_top
        left = slot.bitmap_left
        w,h = bitmap.width, bitmap.rows
        y = height-baseline-top
        kerning = face.get_kerning(previous, c)
        x += (kerning.x >> 6)

        Z[y:y+h,x:x+w] += numpy.array(bitmap.buffer, dtype=numpy.uint8).reshape(h,w)/256.0
        x += (slot.advance.x >> 6)
        previous = c
    img['A'] = Z
    img['R'] = color[0]
    img['G'] = color[1]
    img['B'] = color[2]
    I = img.view(dtype=float).reshape(img.shape[0], img.shape[1], 4)
    I = (I*255).astype(int).astype(np.uint8)
    image = Image.fromarray(I,mode='RGBA')
    return image

if __name__ == '__main__':
    GenerateNumberPic()