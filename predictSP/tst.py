__author__ = 'adam'


a = [1, 2, 3, 4, 5]
a = '1 2 3 4 5'
numlen = len(a.split(' '))
b = a.split(' ')[1:numlen]

print b