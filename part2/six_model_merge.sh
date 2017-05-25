#!/usr/bin/env bash



python fillNull.py
python findSamePeople.py
python mergeFeatures.py
python dataFilter.py
#进行数据格式转换

python format_translate1.py 030_data/train_030_1_1.txt 030_data/train_030_1_1.txt.libsvmformat
python format_translate1.py 030_data/train_030_1_2.txt 030_data/train_030_1_2.txt.libsvmformat
python format_translate1.py 030_data/train_030_1_3.txt 030_data/train_030_1_3.txt.libsvmformat
python format_translate1.py 030_data/train_030_1_4.txt 030_data/train_030_1_4.txt.libsvmformat
python format_translate1.py 030_data/train_030_1_5.txt 030_data/train_030_1_5.txt.libsvmformat
python format_translate1.py 030_data/test_online.txt 030_data/test_online.txt.libsvmformat

# 创建文件夹
mkdir result
mkdir model_auto

# 删除之前生成的所有结果
rm result/*
rm model_auto/*



# 开始运行模型
#1
python xgboost_auto.py 4 0.1 200 030_data/test_online.txt 030_data/train_030_1_1.txt.libsvmformat 030_data/test_online.txt.libsvmformat Monday_1 Evening_1
python xgboost_auto.py 4 0.1 200 030_data/test_online.txt 030_data/train_030_1_2.txt.libsvmformat 030_data/test_online.txt.libsvmformat Monday_2 Evening_2
python xgboost_auto.py 4 0.1 200 030_data/test_online.txt 030_data/train_030_1_3.txt.libsvmformat 030_data/test_online.txt.libsvmformat Monday_3 Evening_3
python xgboost_auto.py 4 0.1 200 030_data/test_online.txt 030_data/train_030_1_4.txt.libsvmformat 030_data/test_online.txt.libsvmformat Monday_4 Evening_4
python xgboost_auto.py 4 0.1 200 030_data/test_online.txt 030_data/train_030_1_5.txt.libsvmformat 030_data/test_online.txt.libsvmformat Monday_5 Evening_5

#2
python xgboost_auto.py 4 0.08 250 030_data/test_online.txt 030_data/train_030_1_1.txt.libsvmformat 030_data/test_online.txt.libsvmformat Monday_1 Evening_1
python xgboost_auto.py 4 0.08 250 030_data/test_online.txt 030_data/train_030_1_2.txt.libsvmformat 030_data/test_online.txt.libsvmformat Monday_2 Evening_2
python xgboost_auto.py 4 0.08 250 030_data/test_online.txt 030_data/train_030_1_3.txt.libsvmformat 030_data/test_online.txt.libsvmformat Monday_3 Evening_3
python xgboost_auto.py 4 0.08 250 030_data/test_online.txt 030_data/train_030_1_4.txt.libsvmformat 030_data/test_online.txt.libsvmformat Monday_4 Evening_4
python xgboost_auto.py 4 0.08 250 030_data/test_online.txt 030_data/train_030_1_5.txt.libsvmformat 030_data/test_online.txt.libsvmformat Monday_5 Evening_5

#3
python xgboost_auto.py 5 0.06 230 030_data/test_online.txt 030_data/train_030_1_1.txt.libsvmformat 030_data/test_online.txt.libsvmformat Monday_1 Evening_1
python xgboost_auto.py 5 0.06 230 030_data/test_online.txt 030_data/train_030_1_2.txt.libsvmformat 030_data/test_online.txt.libsvmformat Monday_2 Evening_2
python xgboost_auto.py 5 0.06 230 030_data/test_online.txt 030_data/train_030_1_3.txt.libsvmformat 030_data/test_online.txt.libsvmformat Monday_3 Evening_3
python xgboost_auto.py 5 0.06 230 030_data/test_online.txt 030_data/train_030_1_4.txt.libsvmformat 030_data/test_online.txt.libsvmformat Monday_4 Evening_4
python xgboost_auto.py 5 0.06 230 030_data/test_online.txt 030_data/train_030_1_5.txt.libsvmformat 030_data/test_online.txt.libsvmformat Monday_5 Evening_5

#4
python xgboost_auto.py 5 0.08 200 030_data/test_online.txt 030_data/train_030_1_1.txt.libsvmformat 030_data/test_online.txt.libsvmformat Monday_1 Evening_1
python xgboost_auto.py 5 0.08 200 030_data/test_online.txt 030_data/train_030_1_2.txt.libsvmformat 030_data/test_online.txt.libsvmformat Monday_2 Evening_2
python xgboost_auto.py 5 0.08 200 030_data/test_online.txt 030_data/train_030_1_3.txt.libsvmformat 030_data/test_online.txt.libsvmformat Monday_3 Evening_3
python xgboost_auto.py 5 0.08 200 030_data/test_online.txt 030_data/train_030_1_4.txt.libsvmformat 030_data/test_online.txt.libsvmformat Monday_4 Evening_4
python xgboost_auto.py 5 0.08 200 030_data/test_online.txt 030_data/train_030_1_5.txt.libsvmformat 030_data/test_online.txt.libsvmformat Monday_5 Evening_5

#5
python xgboost_auto.py 6 0.05 220 030_data/test_online.txt 030_data/train_030_1_1.txt.libsvmformat 030_data/test_online.txt.libsvmformat Monday_1 Evening_1
python xgboost_auto.py 6 0.05 220 030_data/test_online.txt 030_data/train_030_1_2.txt.libsvmformat 030_data/test_online.txt.libsvmformat Monday_1 Evening_2
python xgboost_auto.py 6 0.05 220 030_data/test_online.txt 030_data/train_030_1_3.txt.libsvmformat 030_data/test_online.txt.libsvmformat Monday_1 Evening_3
python xgboost_auto.py 6 0.05 220 030_data/test_online.txt 030_data/train_030_1_4.txt.libsvmformat 030_data/test_online.txt.libsvmformat Monday_1 Evening_4
python xgboost_auto.py 6 0.05 220 030_data/test_online.txt 030_data/train_030_1_5.txt.libsvmformat 030_data/test_online.txt.libsvmformat Monday_1 Evening_5

#6
python xgboost_auto.py 6 0.07 190 030_data/test_online.txt 030_data/train_030_1_1.txt.libsvmformat 030_data/test_online.txt.libsvmformat Monday_1 Evening_1
python xgboost_auto.py 6 0.07 190 030_data/test_online.txt 030_data/train_030_1_2.txt.libsvmformat 030_data/test_online.txt.libsvmformat Monday_1 Evening_2
python xgboost_auto.py 6 0.07 190 030_data/test_online.txt 030_data/train_030_1_3.txt.libsvmformat 030_data/test_online.txt.libsvmformat Monday_1 Evening_3
python xgboost_auto.py 6 0.07 190 030_data/test_online.txt 030_data/train_030_1_4.txt.libsvmformat 030_data/test_online.txt.libsvmformat Monday_1 Evening_4
python xgboost_auto.py 6 0.07 190 030_data/test_online.txt 030_data/train_030_1_5.txt.libsvmformat 030_data/test_online.txt.libsvmformat Monday_1 Evening_5


#融合结果  生成的结果保存在 当前目录下的 avg_result_of_six_model.csv
rm avg_result_of_six_model.csv
python avg.py