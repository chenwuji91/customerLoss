#!usr/bin/env python
# -*- coding: utf-8 -*-

import io_operation
from datetime import datetime
def read_file():
    f1 = open('data/train_fill_null.txt')
    train_data_x= {}
    train_data_x_new = {}
    data = []
    for eachline in f1 :
        eachline = eachline.split('\n')[0].split('\r')[0].split(',')

        if eachline.__contains__('sampleid') or len(eachline)<5:
            continue
        date_interval = datetime.strptime(eachline[3],'%Y-%m-%d').day - datetime.strptime(eachline[2],'%Y-%m-%d').day
        weekday = datetime.strptime(eachline[3],'%Y-%m-%d').strftime("%w")
        weekday_see = datetime.strptime(eachline[2],'%Y-%m-%d').strftime("%w")
        if weekday in [5,6]:
            weekday = 0
        else:
            weekday = 1
        if weekday_see in [5,6]:
            weekday_see = 0
        else:
            weekday_see = 1
        if eachline[48] == 0:
            sid0 = 0
        else:
            sid0 = 1
        if eachline[48] == 1:
            sid1 = 0
        else:
            sid1 = 1
        del eachline[23]
        train_data_x[eachline[1]] = eachline+[str(date_interval)]+[str(weekday)]+[str(weekday_see)]+[str(sid0)]+[str(sid1)]
        train_data_x_new[eachline[1]] = []

    f2 = open('data/sameuser_train.txt')
    for eachline in f2 :
        sampleidlist = eachline.split('\n')[0].split('\r')[0].split('|')[1:]
        #print sampleidlist
        new_tezheng_max = {}
        new_tezheng_min = {}
        #new_tezheng_mean = {}
        shuxinglst = [4,5,6,7,8,10,12,14,17,18,19,21,22,24,25,26,27,28,29,30,32,33,34,35,37,38,39,40,41,42,43,44,45,46,48,49,50]
        for i in shuxinglst:
            new_tezheng_max[i] = -1000000
        for i in shuxinglst:
            new_tezheng_min[i] = 1000000
        #for i in shuxinglst:
            #new_tezheng_mean[i] = 0
        for sample in sampleidlist:
            for i in shuxinglst:
                new_tezheng_max[i] =str(max([float(train_data_x[sample][i]),float(new_tezheng_max[i])]))
                new_tezheng_min[i] =str(min([float(train_data_x[sample][i]),float(new_tezheng_min[i])]))

        for sample in sampleidlist:
            data.append(','.join(train_data_x[sample]+new_tezheng_max.values()+new_tezheng_min.values()+[str(len(sampleidlist))])+'\n')
    io_operation.write_to_file('data/train_online.txt',data)


def read_test_file():
    f1 = open('data/test_fill_null.txt')
    train_data_x= {}
    train_data_x_new = {}
    data = []
    for eachline in f1 :
        eachline = eachline.split('\n')[0].split('\r')[0].split(',')

        if eachline.__contains__('sampleid') or len(eachline)<5:
            continue
        date_interval = datetime.strptime(eachline[3],'%Y-%m-%d').day - datetime.strptime(eachline[2],'%Y-%m-%d').day
        weekday = datetime.strptime(eachline[3],'%Y-%m-%d').strftime("%w")
        weekday_see = datetime.strptime(eachline[2],'%Y-%m-%d').strftime("%w")
        if weekday in [5,6]:
            weekday = 0
        else:
            weekday = 1
        if weekday_see in [5,6]:
            weekday_see = 0
        else:
            weekday_see = 1
        if eachline[48] == 0:
            sid0 = 0
        else:
            sid0 = 1
        if eachline[48] == 1:
            sid1 = 0
        else:
            sid1 = 1
        del eachline[23]
        train_data_x[eachline[1]] = eachline+[str(date_interval)]+[str(weekday)]+[str(weekday_see)]+[str(sid0)]+[str(sid1)]
        train_data_x_new[eachline[1]] = []

    f2 = open('data/sameuser_test.txt')
    for eachline in f2 :
        sampleidlist = eachline.split('\n')[0].split('\r')[0].split('|')[1:]
        #print sampleidlist
        new_tezheng_max = {}
        new_tezheng_min = {}
        #new_tezheng_mean = {}
        shuxinglst = [4,5,6,7,8,10,12,14,17,18,19,21,22,24,25,26,27,28,29,30,32,33,34,35,37,38,39,40,41,42,43,44,45,46,48,49,50]
        for i in shuxinglst:
            new_tezheng_max[i] = -1000000
        for i in shuxinglst:
            new_tezheng_min[i] = 1000000
        #for i in shuxinglst:
            #new_tezheng_mean[i] = 0
        for sample in sampleidlist:
            for i in shuxinglst:
                new_tezheng_max[i] =str(max([float(train_data_x[sample][i]),float(new_tezheng_max[i])]))
                new_tezheng_min[i] =str(min([float(train_data_x[sample][i]),float(new_tezheng_min[i])]))

        for sample in sampleidlist:
            data.append(','.join(train_data_x[sample]+new_tezheng_max.values()+new_tezheng_min.values()+[str(len(sampleidlist))])+'\n')
    io_operation.write_to_file('030_data/test_online.txt',data)

if __name__ == '__main__':
    #read_file()
    read_file()
    read_test_file()


