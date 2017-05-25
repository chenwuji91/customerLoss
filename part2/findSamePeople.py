
#!usr/bin/env python
# -*- coding: utf-8 -*-

import io_operation

def read_file():
    f1 = open('data/userlostprob_train.txt')
    train_data_x= {}
    zu_data_x = {}

    for eachline in f1 :
        if eachline.__contains__('sampleid'):
            continue

        data = eachline.split('\n')[0].split('\r')[0].split('	')
        useridstr = data[2]+'|'+data[9]+"|"+data[7]+"|"+data[6]+"|"+data[11]+"|"+data[16]+"|"\
                +data[23]+"|"+data[31]+"|"+data[36]\
                +"|"+data[13]+"|"+data[15]+"|"+data[20]+"|"+data[47]
        #train_data_x[useridstr] = 'data:'
        train_data_x[useridstr] = ''
        zu_data_x[useridstr] = []

    f2 = open('data/userlostprob_train.txt')
    for eachline in f2 :

        if eachline.__contains__('sampleid'):
            continue

        data = eachline.split('\n')[0].split('\r')[0].split('	')
        useridstr = data[2]+'|'+data[9]+"|"+data[7]+"|"+data[6]+"|"+data[11]+"|"+data[16]+"|"\
                +data[23]+"|"+data[31]+"|"+data[36]\
                +"|"+data[13]+"|"+data[15]+"|"+data[20]+"|"+data[47]
        #train_data_x[useridstr] = train_data_x[useridstr] + ' '+data[2]+'|'+data[0]
        train_data_x[useridstr] = train_data_x[useridstr] + '|'+data[1]

    return train_data_x


def read_file_test():
    f1 = open('data/yanzhengji_final.csv')
    train_data_x= {}
    zu_data_x = {}

    for eachline in f1 :
        if eachline.__contains__('sampleid') or len(eachline)<5:
            continue
        eachline = '0,'+eachline
        data = eachline.split('\n')[0].split('\r')[0].split(',')
        useridstr = data[2]+'|'+data[9]+"|"+data[7]+"|"+data[6]+"|"+data[11]+"|"+data[16]+"|"\
                +data[23]+"|"+data[31]+"|"+data[36]\
                +"|"+data[13]+"|"+data[15]+"|"+data[20]+"|"+data[47]
        #train_data_x[useridstr] = 'data:'
        train_data_x[useridstr] = ''
        zu_data_x[useridstr] = []

    f2 = open('data/yanzhengji_final.csv')
    for eachline in f2 :

        if eachline.__contains__('sampleid') or len(eachline)<5:
            continue
        eachline = '0,'+eachline
        data = eachline.split('\n')[0].split('\r')[0].split(',')
        useridstr = data[2]+'|'+data[9]+"|"+data[7]+"|"+data[6]+"|"+data[11]+"|"+data[16]+"|"\
                +data[23]+"|"+data[31]+"|"+data[36]\
                +"|"+data[13]+"|"+data[15]+"|"+data[20]+"|"+data[47]

        #train_data_x[useridstr] = train_data_x[useridstr] + ' '+data[2]+'|'+data[0]
        train_data_x[useridstr] = train_data_x[useridstr] + '|'+data[1]

    return train_data_x


if __name__ == '__main__':

    train_data_x = read_file()
    for line in train_data_x.keys():
        io_operation.write_to_file('data/sameuser_train.txt',train_data_x[line])

    train_data_y = read_file_test()
    for line in train_data_y.keys():
        io_operation.write_to_file('data/sameuser_test.txt',train_data_y[line])


