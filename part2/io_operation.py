#!usr/bin/env python
# -*- coding: utf-8 -*-
#加载原始数据
from datetime import datetime
import numpy as np


def read_file_for_local_test():#本地测试的程序读写
    f1 = open('../data/train/part1')
    train_data_x = []
    train_data_y = []
    test_data_x = []
    test_data_y = []
    train_id_list = []
    test_id_list = []

    for eachline in f1 :
        if eachline.__contains__('sampleid'):
            continue
        data_list = eachline.split('\n')[0].split('\r')[0].split(',')    #数据做一个处理  把日期变成两个的时间差
        date_interval = datetime.strptime(data_list[3], '%Y-%m-%d').day - datetime.strptime(data_list[2], '%Y-%m-%d').day
        attribuite_list = [date_interval] + eachline.split('\n')[0].split('\r')[0].split('	')[4:len(data_list)]
        current_id = eachline.split('\n')[0].split('\r')[0].split(',')[1]
        attribuite_list_new = []
        for eache in attribuite_list:
            if eache == 'NULL':
                eache = np.nan
            else:
                eache = float(eache)
            attribuite_list_new.append(eache)

        if len(train_data_x) < 66666:
            train_data_y.append(int(eachline.split('\n')[0].split('\r')[0].split('	')[0]))
            train_data_x.append(attribuite_list_new)
            train_id_list.append(current_id)

        elif len(test_data_x) < 33333:
            test_data_y.append(int(eachline.split('\n')[0].split('\r')[0].split('	')[0]))
            test_data_x.append(attribuite_list_new)
            test_id_list.append(current_id)
        else:
            break

    return train_data_x, train_data_y, test_data_x, test_data_y, train_id_list, test_id_list


def read_file_for_submit(): #提交数据的文件读写
    f1 = open('train_027_4_1.txt')
    f2 = open('test_027_4.txt')
    train_data_x = []
    train_data_y = []
    test_data_x = []
    sample_id = []
    true_id = []

    for eachline in f1:
        if eachline.__contains__('sampleid') or len(eachline)<5:
            continue
        data_list = eachline.split('\n')[0].split('\r')[0].split(',')
        attribuite_list = data_list[2:len(data_list)]
        train_data_y.append(int(eachline.split('\n')[0].split('\r')[0].split(',')[0]))
        train_data_x.append(attribuite_list)
    for eachline in f2:
        if eachline.__contains__('sampleid') or len(eachline)<5:
            continue
        data_list = eachline.split('\n')[0].split('\r')[0].split(',')
        attribuite_list = data_list[2:]
        sample_id.append(int(data_list[1]))
        true_id.append(int(data_list[0]))
        test_data_x.append(attribuite_list)
    return train_data_x,train_data_y,test_data_x,sample_id,true_id


def read_file_for_submit_2():
    f1 = open('../data/train_027_3_1.txt')
    f2 = open('../data/test_027_3.txt')
    train_data_x = []
    train_data_y = []
    test_data_x = []
    sample_id = []
    true_id = []
    train_sample_id = []
    train_true_id = []
    for eachline in f1:
        if eachline.__contains__('sampleid') or len(eachline)<5:
            continue
        data_list = eachline.split('\n')[0].split('\r')[0].split(',')
        attribuite_list =  [float(i) for i in data_list[4:]]
        train_sample_id.append(int(data_list[1]))
        train_true_id.append(int(data_list[0]))
        train_data_y.append(int(eachline.split('\n')[0].split('\r')[0].split(',')[0]))
        train_data_x.append(attribuite_list)
    for eachline in f2:
        if eachline.__contains__('sampleid') or len(eachline)<5:
            continue
        data_list = eachline.split('\n')[0].split('\r')[0].split(',')
        attribuite_list = [float(i) for i in data_list[4:]]
        sample_id.append(int(data_list[1]))
        true_id.append(int(data_list[0]))
        test_data_x.append(attribuite_list)
    return train_data_x,train_data_y,test_data_x,sample_id,true_id,train_sample_id,train_true_id



def write_to_file(filename, data):  #文件写入
    f = file(filename, 'a+')
    f.writelines(data)
    f.writelines('\n')
    f.close()
