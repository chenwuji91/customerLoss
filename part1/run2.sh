#!/bin/sh
rm featuremap
echo "makedata"
python newscripts/changetest.py
python newscripts/recoverdata.py userlostprob_train.txt newtrain.txt
#<<!
echo "getfeature"
echo "feature1"
python newscripts/feature1.py newtrain.txt tmp/feature1.train
python newscripts/feature1.py newtest.txt tmp/feature1.test
#cp tmp/feature1.train tmp/feature1.valid
echo "feature2_mod_3"
python newscripts/feature2_mod_3.py newtrain.txt tmp/feature2_mod_3.train 
python newscripts/feature2_mod_3.py newtest.txt tmp/feature2_mod_3.test
#cp tmp/feature2_mod_3.train tmp/feature2_mod_3.valid
echo "feature7"
python newscripts/cluster5_mod.py newtrain.txt newtest.txt tmp/feature7.train tmp/feature7.test
#cp tmp/feature7.train tmp/feature7.valid
echo "feature8"
python newscripts/cluster6_mod.py newtrain.txt newtest.txt tmp/feature8.train tmp/feature8.test
#cp tmp/feature8.train tmp/feature8.valid
echo "feature10"
python newscripts/feature10.py newtrain.txt tmp/feature10.train 
python newscripts/feature10.py newtest.txt tmp/feature10.test
#cp tmp/feature10.train tmp/feature10.valid
echo "feature11_all_mod"
python newscripts/feature11_all_mod.py newtrain.txt tmp/feature11_all_mod.train 
python newscripts/feature11_all_mod.py newtest.txt tmp/feature11_all_mod.test
#cp tmp/feature11_all_mod.train tmp/feature11_all_mod.valid
echo "datapoint_2"
echo "fea_2_1_7_8_10_11"
#<<!
echo "join"
for i in 1 2 3 4 5
do
    echo $i
    python newscripts/getnewlabel.py newdata/train_yujun_online_$i.txt userlostprob_train.txt newdata/newdatapoint_$i.train
    python newscripts/join.py newdata/newdatapoint_$i.train tmp/feature2_mod_3.train tmp/join_1.train
    python newscripts/join.py tmp/join_1.train tmp/feature1.train tmp/join_2.train
    python newscripts/join.py tmp/join_2.train tmp/feature7.train tmp/join_3.train
    python newscripts/join.py tmp/join_3.train tmp/feature8.train tmp/join_4.train
    python newscripts/join.py tmp/join_4.train tmp/feature10.train tmp/join_5.train
    python newscripts/join.py tmp/join_5.train tmp/feature11_all_mod.train tmp/join.train
    python newscripts/feature_map.py tmp/join.train newtrain/train_$i featuremap
done
#!
echo "join test"
python newscripts/gettestlable.py
python newscripts/join.py newdata/datapoint.test tmp/feature2_mod_3.test tmp/join_1.test
python newscripts/join.py tmp/join_1.test tmp/feature1.test tmp/join_2.test
python newscripts/join.py tmp/join_2.test tmp/feature7.test tmp/join_3.test
python newscripts/join.py tmp/join_3.test tmp/feature8.test tmp/join_4.test
python newscripts/join.py tmp/join_4.test tmp/feature10.test tmp/join_5.test
python newscripts/join.py tmp/join_5.test tmp/feature11_all_mod.test tmp/join.test
python newscripts/feature_map.py tmp/join.test newtest/test_newread featuremap


echo "train"    
python -u newscripts/newtrain.py newtest/test_newread newtest/newtest.pred
paste -d ',' newtest/test_newread_sampleid newtest/newtest.pred > newresult.csv

rm tmp/join*
