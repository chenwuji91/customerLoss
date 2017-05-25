f = file("newtest.txt","w+")
with open("yanzhengji_final.csv") as fin:
    for line in fin:
        f.write("0\t"+line)
f.close()
