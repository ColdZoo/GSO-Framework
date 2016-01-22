# -*- encoding: utf-8 -*-
__author__ = 'adam'

# predict a single image's sentipair

import os
import caffe
import numpy as np

def init():
    global caffe_root
    global net
    global transformer
    caffe_root = '/home/adam/data/caffe-multi-label-example/'
    caffe.set_mode_gpu()
    net = caffe.Net('/home/adam/data/gsosp1274/deploy.prototxt',
                    '/home/adam/data/gsosp1274/snapshots/server_train_iter_24000', caffe.TEST)
    transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
    transformer.set_transpose('data', (2, 0, 1))
    # transformer.set_mean('data', np.load('/home/adam/data/gsosp1274/mean.binaryproto').mean(1).mean(1))
    transformer.set_raw_scale('data', 255)
    # transformer.set_channel_swap('data', (2, 1, 0))
    net.blobs['data'].reshape(1, 3, 227, 227)


def predict(sliced_image):
    global net
    net.blobs['data'].data[...] = transformer.preprocess('data', caffe.io.load_image(sliced_image))
    out = net.forward()
    result = out['fc8_gso'][0]
    sorted_res = sorted(result)
    top1 = sorted_res[len(sorted_res) - 1]
    top2 = sorted_res[len(sorted_res) - 2]
    top3 = sorted_res[len(sorted_res) - 3]
    top4 = sorted_res[len(sorted_res) - 4]
    top5 = sorted_res[len(sorted_res) - 5]
    index1 = -1
    index2 = -1
    index3 = -1
    index4 = -1
    index5 = -1
    for i in range(0, len(result)):
        value = result[i]
        if top1 == value and index1 == -1:  # in case top1 == top2
            index1 = i
        if top2 == value:
            index2 = i
        if top3 == value:
            index3 = i
        if top4 == value:
            index4 = i
        if top5 == value:
            index5 = i
    ret_value = np.zeros(len(sorted_res), int)
    ret_value = ret_value.tolist()
    ret_value[index1] = 1
    ret_value[index2] = 1
    ret_value[index3] = 1
    ret_value[index4] = 1
    ret_value[index5] = 1
    # print ret_value
    return ret_value

init()
predict('test.jpg')
