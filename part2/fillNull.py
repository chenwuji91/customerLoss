#!usr/bin/env python
# -*- coding: utf-8 -*-

import io_operation



def read_file():
    f1 = open('data/userlostprob_train.txt')
    f2 = open('data/yanzhengji_final.csv')
    train_data_x = []
    test_data_x = []
    for eachline in f1 :
        if eachline.__contains__('sampleid'):
            continue
        filename = []
        null_shuxing = [10,24,26,28,32,33,34,35,37,38,39,40,41,44]
        shuxings = eachline.split('\n')[0].split('\r')[0].split('	')
        shuxings_new = shuxings[0:4]
        del shuxings[0:4]
        for i in range(0,len(shuxings)):
            if shuxings[i] == 'NULL' :
                shuxings_new.append(str(0))
                if i in null_shuxing:
                    filename.append(str(0))
            else:
                shuxings_new.append(str(shuxings[i]))
                if i in null_shuxing:
                    filename.append(str(1))
        shuxings_new.extend(filename)
        shuxings_new = ','.join(shuxings_new)

        train_data_x.append(shuxings_new+'\n')

    for eachline in f2 :
        if eachline.__contains__('sampleid'):
            continue
        filename = []
        null_shuxing = [10,24,26,28,32,33,34,35,37,38,39,40,41,44]
        shuxings = eachline.split('\n')[0].split('\r')[0].split(',')
        shuxings_new = shuxings[0:3]
        del shuxings[0:3]
        for i in range(0,len(shuxings)):
            if shuxings[i] == 'NULL':
                shuxings_new.append(str(0))
                if i in null_shuxing:
                    filename.append(str(0))
            else:
                shuxings_new.append(str(shuxings[i]))
                if i in null_shuxing:
                    filename.append(str(1))
        shuxings_new.extend(filename)
        shuxings_new = ','.join(shuxings_new)

        test_data_x.append('0,'+shuxings_new+'\n')

    print 'train',len(train_data_x)
    print 'test',len(test_data_x)
    return train_data_x, test_data_x


if __name__ == '__main__':
    train_data_x, test_data_x = read_file()
    io_operation.write_to_file('data/train_fill_null.txt',train_data_x)
    io_operation.write_to_file('data/test_fill_null.txt',test_data_x)

