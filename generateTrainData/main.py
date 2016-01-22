# -*- coding: utf-8 -*-
__author__ = 'adam'

import csv
import os
import shutil

# LIST SLICE DIR

def findAnnotation(filename):
    ifile  = open('BowFeature_anp_vnp.csv', "rU")
    reader = csv.reader(ifile,  dialect=csv.excel_tab)
    rownum = 0
    for row in reader:
        # Save header row.
        if rownum == 0:
            header = row
        else:
            colnum = 0
            data = row[0].split(',')
            if data[1275] == filename:
                annotation = data[0:1274]
                for index in range(0, len(annotation)):
                    if int(annotation[index]) == 0:
                        annotation[index] = -1
                    else:
                        if int(annotation[index] == 1):
                            annotation[index] = 1
                return annotation
                break
        rownum += 1
    ifile.close()

write_buffer = []
for sliceDir in os.listdir('/media/adam/工作区/GSO2015/slice/'):
    gif_file = sliceDir
    anno = findAnnotation(gif_file)
    for img_file in os.listdir('/media/adam/工作区/GSO2015/slice/' + sliceDir):
        if anno:
            line = list(anno)
            # line.append(img_file)
            line.insert(0, img_file)
            # print len(line)
            write_buffer.append(line)
            # print write_buffer

if not os.path.exists('/media/adam/工作区/GSO2015/' + 'train_set'):
    os.mkdir('/media/adam/工作区/GSO2015/' + 'train_set')
if not os.path.exists('/media/adam/工作区/GSO2015/' + 'test_set'):
    os.mkdir('/media/adam/工作区/GSO2015/' + 'test_set')

f_train = open('/media/adam/工作区/GSO2015/' + 'train_set' + '/' + 'label.txt', 'w')
f_test = open('/media/adam/工作区/GSO2015/' + 'test_set' + '/' + 'label.txt', 'w')

print 'total image: ' + len(write_buffer)
print 'train image: ' + int(len(write_buffer) * 4 / 5)
for index in range(0, len(write_buffer)):
    line = write_buffer[index]
    if index < int(len(write_buffer) * 4 / 5):
        for word in line:
            f_train.write(str(word) + ' ')
        f_train.write('\r\n')
        shutil.copy2('/media/adam/工作区/GSO2015/slice/' + line[0].split('-')[0] + '.gif/' + line[0],
                     '/media/adam/工作区/GSO2015/' + 'train_set/' + line[0])
    else:
        for word in line:
            f_test.write(str(word) + ' ')
        f_test.write('\r\n')
        shutil.copy2('/media/adam/工作区/GSO2015/slice/' + line[0].split('-')[0] + '.gif/' + line[0],
                     '/media/adam/工作区/GSO2015/' + 'test_set/' + line[0])




