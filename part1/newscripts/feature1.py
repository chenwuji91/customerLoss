import sys
import datetime

def strtodatetime(datestr,format):      
    return datetime.datetime.strptime(datestr,format)

def datediff(beginDate,endDate):  
    format="%Y-%m-%d";  
    bd=strtodatetime(beginDate,format)  
    ed=strtodatetime(endDate,format)      
    oneday=datetime.timedelta(days=1)  
    count=0
    while bd!=ed:  
        ed=ed-oneday  
        count+=1
    return count

def getfeature(inputfile,outputfile):
    f = file(outputfile,"w+")
    with open(inputfile) as fin:
        fin.readline()
        for line in fin:
            tmpdata = line.strip().split("\t")
            days = datediff(tmpdata[2],tmpdata[3])
            f.write("f1_0:%d\t#A:%s\n"%(days,tmpdata[1]))
    f.close()

if __name__ == '__main__':
    getfeature(sys.argv[1],sys.argv[2])

