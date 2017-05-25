#!usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
import sys

def libsvm_format_translate(input, output):
    # from sys import argv
    # script, input, output = argv

    txt = open(input, 'r')
    svm_data = open(output, 'w')
    for line in txt.readlines():
        if line.__contains__('sampleid'):
            continue
        line = line.split('\r')[0].split('\n')[0]
        features = line.split(',')
        num = len(features)
        if num < 5:
            print line
            continue
        svm_format = features[0]
        # date_interval = datetime.strptime(features[3], '%Y-%m-%d').day - datetime.strptime(features[2], '%Y-%m-%d').day
        # svm_format = "%s %d:%s" % (svm_format, 1, date_interval)
        # features[2] = datetime.strptime(features[2], '%Y-%m-%d').weekday()
        # features[3] = datetime.strptime(features[3], '%Y-%m-%d').weekday()
        for i in range(4, num):
            if features[i] == 'NULL':
                features[i] = 0
            if features[i]!= 0:
                svm_format = "%s %d:%s" % (svm_format, i-3, features[i])
        svm_format = svm_format + '\n'
        svm_data.write(svm_format)
        # print svm_format
    txt.close()
    svm_data.close()

input = sys.argv[1] #'../data/test/testonline0827.txt'
output = sys.argv[2] #'../data/test/testonline0827.txt.libsvmformat'
libsvm_format_translate(input, output)