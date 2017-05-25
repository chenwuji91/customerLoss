import sys
import numpy as np

def getData(inputfilename):
    user_sampleid = dict()
    sampleid_data = dict()
    with open(inputfilename) as fin:
        fin.readline()
        for line in fin:
            data = line.strip().split("\t")
            sampleid_data.setdefault(data[1],list())
            for i in xrange(len(data)):
                # if data[i] == "NULL":
                #     data[i] = "0"
                sampleid_data[data[1]].append(data[i])
#            user = data[2]+"|"+data[5]+"|"+data[27]+"|"\
#                +data[31]+"|"+data[36]\
#                +"|"+data[13]+"|"+data[15]+"|"+data[20]+"|"+data[47]
		#+"|"+data[5]+"|"+data[18]+"|"+data[25]+"|"+data[27]+"|"+data[42]+"|"+data[46]+"|"+data[49]
            user = data[2]+"|"+data[9]+"|"+data[7]+"|"+data[6]+"|"+data[11]+"|"+data[16]+"|"\
                +data[25]+"|"+data[23]+"|"+data[31]+"|"+data[36]+"|"+data[27]+"|"+data[42]\
                +"|"+data[13]+"|"+data[15]+"|"+data[20]+"|"+data[47]+"|"+data[5]+"|"+data[18]+"|"+data[46]+"|"+data[49]
            user_sampleid.setdefault(user,list()) 
            user_sampleid[user].append(data[1])
    return user_sampleid,sampleid_data

def getnullnum(username):
    data = username.split("|")
    num = 0
    for i in xrange(len(data)):
        if data[i] == "NULL":
            num += 1
    return num

def getlabdiff(samplelist,sampleid_data):
    diffnum = 0
    for i in xrange(len(samplelist)):
        tmpdata = sampleid_data[samplelist[i]]
        if i == 0:
            flag = tmpdata[0]
        else:
            if tmpdata[0] != flag:
                diffnum += 1
    return diffnum


def getfeature(user_sampleid,sampleid_data,outputfile):
    user_fea = dict()
    for k in user_sampleid:
        samplelist = user_sampleid[k]
        user_fea.setdefault(k,list())
        user_fea[k].append(len(samplelist))


#        feature_num = [8,12,14,17,19,21,22,24,26,28,29,32,33,34,35,38,39,40,41,44,45,50]
        without = [2,5,6,7,9,11,13,15,16,18,20,23,25,27,31,36,42,46,47,49]
        feature_num = range(4,51)
        feature_num = filter(lambda x: x not in without, feature_num)
        sam_data = list()
        
        for j in xrange(len(feature_num)):
            for i in xrange(len(samplelist)):
                tmpdata = sampleid_data[samplelist[i]]
                tmplist = list()
                if tmpdata[feature_num[j]] == "NULL":
                    continue
                tmplist.append(float(tmpdata[feature_num[j]]))
            if len(tmplist) == 0:
                tmplist.append(float(-1))
            sam_data.append(tmplist)

        for j in xrange(len(feature_num)):
            user_fea[k].append(np.max(sam_data[j]))
            user_fea[k].append(np.min(sam_data[j]))
            # user_fea[k].append(np.mean(sam_data[j]))
#            user_fea[k].append(np.var(sam_data[j]))
#            user_fea[k].append(np.std(sam_data[j]))
#        nullnum = getnullnum(k)
#        user_fea[k].append(nullnum)
#        diffnum = getlabdiff(samplelist,sampleid_data)
#        user_fea[k].append(diffnum)


    f = file(outputfile,"w+")
    for k in user_fea:
        samplelist = user_sampleid[k]
        featurelist = user_fea[k]
        for i in xrange(len(samplelist)):
            for j in xrange(len(featurelist)):
                f.write("f11_%d:%f\t"%(j,featurelist[j]))
            f.write("#A:%s\n"%samplelist[i])
    f.close()

if __name__ == '__main__':
    user_sampleid,sampleid_data = getData(sys.argv[1])
    getfeature(user_sampleid,sampleid_data,sys.argv[2])
