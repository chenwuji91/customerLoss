import sys

#def getData(inputfile):
#    with open(inputfile) as fin:
#        for line in fin:
#            data = line.strip().split("\t")
#        print data[44]

def getfeature(inputfile,outputfile):
    f = file(outputfile,"w+")
    with open(inputfile) as fin:
        fin.readline()
        for line in fin:
            tmpdata = line.strip().split("\t")
            for i in xrange(4,len(tmpdata)):
                f.write("f2_%d:%s\t"%(i,tmpdata[i]))
            f.write("#A:%s\n"%(tmpdata[1]))
    f.close()

if __name__ == '__main__':
#    getData(sys.argv[1])
     getfeature(sys.argv[1],sys.argv[2])
