#!usr/bin/env python
# -*- coding: utf-8 -*-

import xgboost as xgb
from datetime import datetime
# import judge_result
import io_operation
import sys
def read_file_for_local_test():#本地测试的程序读写
    f1 = open(sys.argv[4])
    test_id_list = []
    test_data_y = []
    for eachline in f1 :
        if eachline.__contains__('sampleid'):
            continue
        if len(eachline.split('\n')[0].split('\r')[0].split(',')) < 2:
            print eachline
            continue
        current_id = eachline.split('\n')[0].split('\r')[0].split(',')[1]
        test_data_y.append(int(eachline.split('\n')[0].split('\r')[0].split(',')[0]))
        test_id_list.append(current_id)
    return test_id_list, test_data_y

import pickle as p
def toFileWithPickle(filename, obj1):
    f = file(filename + '.data', "w")
    p.dump(obj1,f)
    f.close()


def xgboost_main(deep,rate,times):
    # dtrain = xgb.DMatrix('../data/agaricus.txt.train')
    # dtest = xgb.DMatrix('../data/agaricus.txt.test')

    dtrain = xgb.DMatrix(sys.argv[5])
    dtest = xgb.DMatrix(sys.argv[6])
    # specify parameters via map
    param = {'max_depth':deep, 'eta':rate, 'silent':0, 'objective':'binary:logistic' }
    num_round = times
    #  6,300,0.1   8,300,0.1   3,300,0.2   4,300,0.15  5,300,0.17
    bst = xgb.train(param, dtrain, num_round)
    toFileWithPickle('model_auto/xgboost_model_'+sys.argv[7]+'_'+ sys.argv[1] +'_'+ sys.argv[2] +'_'+ sys.argv[3], bst)
    # make prediction
    preds = bst.predict(dtest)
    print preds
    return preds

test_id_list,label = read_file_for_local_test()
prediction = xgboost_main(int(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3]))
if len(test_id_list) != len(prediction):
    print len(prediction)
    exit(-1)
predict_sample = {}
test_sample = {}
for i in range(len(test_id_list)):
    predict_sample.setdefault(test_id_list[i], 1 - prediction[i])
    test_sample.setdefault(test_id_list[i], label[i])
    # io_operation.write_to_file('../data/test0827online.csv',str(test_id_list[i]) + ',' + str(1 - prediction[i]) )

    io_operation.write_to_file('result/result_'+sys.argv[8]+'_'+ sys.argv[1] +'_'+ sys.argv[2] +'_'+ sys.argv[3] +'_.csv',str(test_id_list[i]) + ',' + str(1 - prediction[i]) + ',' + str(label[i]) )
exit(0)
#print judge_result.calculate_score(predict_sample, test_sample)