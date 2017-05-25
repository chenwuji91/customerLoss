import sys
from sklearn.cluster import KMeans
import numpy as np
from sklearn import preprocessing

def normalizeByColumn(array):
    length = len(array[0])
    flag = True
    matrix_arr = np.mat(array).T
    for i in xrange(length):
        tmpcolumn = matrix_arr[i,:]
        tmpcolumnarr = tmpcolumn.getA()
        tmpnorm = preprocessing.normalize(tmpcolumnarr)
        if flag == True:
            array_aftnorm = tmpnorm
            flag = False
        else:
            array_aftnorm = np.row_stack((array_aftnorm,tmpnorm))
    return np.array(np.mat(array_aftnorm).T)


def getfeature(trainfile,testfile,trainoutputfile,testoutputfile):
    train_X = list()
    sampleid = list()

    test_X = list()
    sampleid2 = list()
    f = file(trainoutputfile,"w+")
    f2 = file(testoutputfile,"w+")
    with open(trainfile) as fin:
        fin.readline()
        for line in fin:
            data = line.strip().split("\t")
            sampleid.append(data[1])
            for i in xrange(len(data)):
                if data[i] == "NULL":
                    data[i] = -1
           # train_X.append([float(data[5]),float(data[7]),float(data[9]),float(data[11]),float(data[16]),float(data[23]),float(data[47])])
            train_X.append([float(data[6]),float(data[7]),float(data[9]),float(data[11]),float(data[16]),float(data[19]),float(data[23])])

    with open(testfile) as fin:
        fin.readline()
        for line in fin:
            data = line.strip().split("\t")
            sampleid2.append(data[1])
            for i in xrange(len(data)):
                if data[i] == "NULL":
                    data[i] = -1
            test_X.append([float(data[6]),float(data[7]),float(data[9]),float(data[11]),float(data[16]),float(data[19]),float(data[23])])

    final_x = np.append(np.array(train_X),np.array(test_X),axis=0)
    # final_y = np.append(np.array(Y),np.array(valid_y))
    final_x = normalizeByColumn(final_x)
    train_X = final_x[0:len(sampleid),:]
    test_X = final_x[0:len(sampleid2),:]

    kmodel = KMeans(n_clusters=16)
    kmodel.fit(final_x)
    train_Y = kmodel.predict(train_X)
    for i in xrange(len(train_Y)):
        f.write("c6:%d\t#A:%s\n"%(train_Y[i],sampleid[i]))
    f.close()

    test_Y = kmodel.predict(test_X)
    for i in xrange(len(test_Y)):
        f2.write("c6:%d\t#A:%s\n"%(test_Y[i],sampleid2[i]))
    f2.close()

if __name__ == '__main__':
    getfeature(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])



