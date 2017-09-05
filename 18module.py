#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" module comment """

__author__ = 'jiangyue'

import sys

print(sys.argv)

# 如果在其他地方导入该模块时，if判断将失败
if __name__ == '__main__':
    print('main')

_private_a = 1

public_a = 2


def _private_function():
    print('private function')


def public_function():
    print('public function')

print(__doc__)


from PIL import Image

img = Image.open('test.jpg')
print(img.format, img.size, img.mode)
img.thumbnail((200, 100))
img.save('thumb.jpg', 'JPEG')

