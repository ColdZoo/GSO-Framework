# -*- coding: utf-8 -*-
import sliceLogic as sl
import os
__author__ = 'adam'

for i in os.listdir('/media/adam/工作区/GSO2015/gif/'):
    if i.endswith('.gif'):
        print '/media/adam/工作区/GSO2015/gif/' + i
        print '/media/adam/工作区/GSO2015/slice/' + i
        sl.processImage('/media/adam/工作区/GSO2015/gif/' + i, '/media/adam/工作区/GSO2015/slice/' + i)
    else:
        continue
