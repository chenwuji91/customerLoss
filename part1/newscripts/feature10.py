import sys
import datetime

def getday(daytime):
    date = datetime.datetime.strptime(daytime,"%Y-%m-%d")
    return date.weekday()

def getfeature(inputfile,outputfile):
    f = file(outputfile,"w+")
    with open(inputfile) as fin:
        fin.readline()
        for line in fin:
            data = line.strip().split("\t")
            visitday = getday(data[2])
            arriveday = getday(data[3])
            f.write("f10_1:%s\tf10_2:%s\t#A:%s\n"%(str(visitday),str(arriveday),data[1]))
        f.close()

if __name__ == '__main__':
    getfeature(sys.argv[1],sys.argv[2])
