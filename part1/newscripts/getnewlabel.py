import sys

def getSam(inputfile):
    samid = list()
    with open(inputfile) as fin:
        for line in fin:
            data = line.strip()
            samid.append(data)
    return samid

def makedata(inputfile,outputfile,samid):
    f = file(outputfile,"w+")
    sample_label = dict()
    with open(inputfile) as fin:
        fin.readline()
        for line in fin:
            data = line.strip().split("\t")
            if len(data) != 51:
                continue
            sample_label.setdefault(data[1],data[0])
    for i in xrange(len(samid)):
        if sample_label.has_key(samid[i]):
            f.write(sample_label[samid[i]]+"\t#A:"+samid[i]+"\n")
    f.close()
if __name__ == '__main__':
    samid = getSam(sys.argv[1])
    makedata(sys.argv[2],sys.argv[3],samid)
