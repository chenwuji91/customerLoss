f = file("newdata/datapoint.test","w+")
with open("yanzhengji_final.csv") as fin:
    fin.readline()
    for line in fin:
        data = line.strip().split("\t")
        if len(data) != 50:
            continue
        f.write("0\t#A:%s\n"%data[0])
    f.close()
