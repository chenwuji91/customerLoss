import sys
import xgboost as xgb
import numpy as np
#from sklearn.datasets import load_svmlight_file
from sklearn import grid_search
#from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import precision_recall_curve
from sklearn.grid_search import ParameterGrid

def load(filename):
    with open(filename) as fin:
        X = list()
        y = list()
        for line in fin:
            data = line.strip().split("\t")
            y.append(float(data[0]))
            tmptrain = list()
            for i in xrange(1,len(data)):
                tmpval = data[i].split(":")[1]
                if tmpval == "NULL":
                    tmptrain.append(np.nan)
                else:
                    tmptrain.append(float(tmpval))
            X.append(tmptrain)
    return np.array(X),np.array(y)


def train(X,Y,params,test_x):
    clf = xgb.XGBClassifier(**params)
    clf.fit(X,Y)
    test_pred = predict(clf,test_x)
    test_pred = getProb(test_pred)
    return test_pred


def getAvgByCol(predlist):
    length = len(predlist)
    l = np.array(predlist)
    col_sum = map(sum,zip(*l))
    col_avg = np.array(col_sum)/length
    return col_avg

def predict(clf,X):
    return clf.predict_proba(X)

def output(outputfile,test_pred):
    f = file(outputfile,"w+")
    f.write("prob\n")
    for p in test_pred:
        f.write("%f\n"%p)
    f.close()

def run(testfile,testoutputfile):
    params = {
    "max_depth":[6,5],
    "learning_rate":[0.06,0.04,0.05],
    "n_estimators":[150,175,200,225,250],
    "subsample":[0.9],
    "colsample_bytree":[0.8]
    }
    param_list = list(ParameterGrid(params))
    train_x_list = list()
    train_y_list = list()
    testpredlist = list()

    for i in xrange(1,6):
        X,y = load("newtrain/train_"+str(i))
        train_x_list.append(X)
        train_y_list.append(y)
    test_x,test_y = load(testfile)
    for i in xrange(len(param_list)):
        tmptest = train(train_x_list[i%5],train_y_list[i%5],param_list[i],test_x)
        testpredlist.append(tmptest)

    test_col_avg = getAvgByCol(testpredlist)
    output(testoutputfile,test_col_avg)


def getProb(pred):
    realp = list()
    for p in pred:
        realp.append(p[0])
    return realp

def getScore(valid_pred,valid_y):
    precision, recall, threshold = precision_recall_curve(valid_y==0, valid_pred[:,0])
    maxrecall = 0
    for p, r in zip(precision, recall):
        if p >= 0.97 and r > maxrecall:
            maxrecall = r
    return maxrecall

if __name__ == '__main__':
    run(sys.argv[1],sys.argv[2])

