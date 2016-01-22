# -*- encoding: utf-8 -*-
__author__ = 'adam'

#  get Test dataset's Accuracy.

import os
import predict as pd

test_dir = '/media/adam/工作区/GSO2015/test_set_2088/'
# test_dir = '/media/adam/工作区/GSO2015/train_set_8352/'

def compare2Vectors(predict_vector, label):
    score = 0
    for i in range(0, len(predict_vector)):
        if predict_vector[i] == 1:
            if int(label[i]) == 1:
                # score += 0.5
                return 1
    return score



def getlabelfromecontent(filename, content):
    len_line = len(content[0].split(' '))
    for line in content:
        if line.split(' ')[0] == filename:
            u = line.split(' ')[1:len_line]
            k = u[len_line-2]  # k is \r\n here
            u = line.split(' ')[1:len_line-1]
            return line.split(' ')[1:len_line-1]

#  open test label
with open(test_dir + 'label.txt') as f:
    content = f.readlines()


pd.init()
#  open test dataset

file_count = 0
total_score = 0
for i in os.listdir(test_dir):
    if i.endswith('.jpg'):
        file_count += 1
        print 'processing: ' + i
        result = pd.predict(test_dir + i)
        label = getlabelfromecontent(i, content)
        score = compare2Vectors(result, label)
        total_score += score

print 'accuracy is: ' + str(total_score / file_count)


