#!usr/bin/env python
# -*- coding: utf-8 -*-
#


def get_index_list():
    import glob
    f = glob.glob('result/*')
    index_list = []
    for eachfile in f:
        f2 = open(eachfile)
        for eachline in f2:
            index = eachline.split(',')[0]
            index_list.append(index)
        f2.close()
        if len(index_list) != 653300:
            print 'Error line count'
            exit(-2)
        break
    return index_list

def get_data():
    import glob
    f = glob.glob('result/*')
    data_all = []
    for eachfile in f:
        data_one = []
        f2 = open(eachfile)
        for eachline in f2:
            prob = float(eachline.split(',')[1])
            data_one.append(prob)
        f2.close()
        if len(data_one) != 653300:
            print 'Error line count'
            exit(-2)
        data_all.append(data_one)
    return data_all

def get_avg(data_all):
    avg_list = []
    for i in range(len(data_all[0])):
        avg = 0
        for j in range(len(data_all)):
            avg = data_all[j][i] + avg
        avg = avg/len(data_all)
        avg_list.append(avg)
    return avg_list

if __name__ == '__main__':
    import io_operation
    index_list = get_index_list()
    data_all = get_data()
    avg_list = get_avg(data_all)
    for i in range(len(index_list)):
        io_operation.write_to_file('avg_result_of_six_model.csv', str(index_list[i]) + ',' + str(avg_list[i]))


