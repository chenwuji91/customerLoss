import sys
import numpy as np
def getData(model1,model2):
    m1_problist = list()
    m2_problist = list()
    m1_dict = dict()
    m2_dict = dict()
    with open(model1) as fin:
        fin.readline()
        for line in fin:
            data = line.strip().split(",")
            m1_problist.append(float(data[1]))
            m1_dict.setdefault(data[0],float(data[1]))

    with open(model2) as fin:
        fin.readline()
        for line in fin:
            data = line.strip().split(",")
            m2_problist.append(float(data[1]))
            m2_dict.setdefault(data[0],float(data[1]))

    m1_max = np.max(m1_problist)
    m1_min = np.min(m1_problist)
    m1_max_min = m1_max - m1_min
    m2_max = np.max(m2_problist)
    m2_min = np.min(m2_problist)
    m2_max_min = m2_max - m2_min
    f = file("prediction_mrqin26_final.csv","w+")
    f.write("sampleid,prob\n")
    for k in m1_dict:
        m1_dict[k] = ((m1_dict[k] - m1_min) / (m1_max_min) + (m2_dict[k] - m2_min) / (m2_max_min)) / 2.0
#        m1_dict[k] = 0.537 * (m1_dict[k] - m1_min) / (m1_max_min) + 0.463 * (m2_dict[k] - m2_min) / (m2_max_min) 
#        m1_dict[k] = (m1_dict[k] + m2_dict[k]) / 2.0
        f.write("%s,%f\n"%(k,m1_dict[k]))
       # print("%s,%f"%(k,m1_dict[k]))
    f.close()
if __name__ == '__main__':
    getData(sys.argv[1],sys.argv[2])

