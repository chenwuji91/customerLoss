import sys

def getData(inputfile,outputfile):
    f = file(outputfile,"w+")
    with open(inputfile) as fin:
        firstline = fin.readline()
        f.write(firstline)
        for line in fin:
            data = line.strip().split("\t")
            f.write("%s"%data[0])
            if data[7] != "NULL":
                if data[23] == "NULL":
                    data[23] = data[7]
            elif data[23] != "NULL":
                if data[7] == "NULL":
                    data[7] = data[23]
            for i in xrange(1,len(data)):
                f.write("\t%s"%data[i])
            f.write("\n")
if __name__ == '__main__':
    getData(sys.argv[1],sys.argv[2])
