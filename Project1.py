import numpy as np
import math
def calF(p,flag):
    x1 = np.array([], dtype=np.int64).reshape(0, len(a[0]))

    for i in p:
        v = i - 1;
        x1 = np.append(x1, np.array([a[v]]), axis=0)
        # print(v,a[v])

    # print(x1)

    # cal the entropy of this array
    res1 = 0
    res2 = 0
    for i in range(len(x1)):
        if x1[i][-1] == 0:
            res1 += 1;
        else:
            res2 += 1;

    # print(res1,res2)
    e = 0
    if res1 != 0:
        e += ((res1 / len(x1)) * math.log((1 / (res1 / len(x1))), 2))
    if res2 != 0:
        e += ((res2 / len(x1)) * math.log((1 / (res2 / len(x1))), 2))
    # print("entropy of",p,"is",e)
    if e == 0:
        # print("no need to classify this partition further", p)
        return 0;

    # now chk entropy for each attribute

    maxGain = -9999
    maxAttribute = 0
    col_len = len(x1[0]) - 1

    for i in range(col_len):  # for each attribute
        ecal = np.array([[0, 0], [0, 0], [0, 0]])
        attr_entropy = 0
        attr_entropy1 = 0
        attr_entropy2 = 0
        attr_entropy3 = 0
        for j in range(len(x1)):
            if x1[j][i] == 0:
                ecal[0][x1[j][-1]] += 1
            elif x1[j][i] == 1:
                ecal[1][x1[j][-1]] += 1
            else:
                ecal[2][x1[j][-1]] += 1

        # print(ecal)
        if (ecal[0][0] + ecal[0][1]) != 0:
            if ecal[0][0] != 0:
                attr_entropy1 = (ecal[0][0] / (ecal[0][0] + ecal[0][1]) * math.log(
                    (1 / ((ecal[0][0] / (ecal[0][0] + ecal[0][1])))), 2))
            if ecal[0][1] != 0:
                attr_entropy1 += (ecal[0][1] / (ecal[0][0] + ecal[0][1]) * math.log(
                    (1 / ((ecal[0][1] / (ecal[0][0] + ecal[0][1])))), 2))
            attr_entropy1 *= ((ecal[0][0] + ecal[0][1]) / len(x1))
            # print("0",attr_entropy1)

        if (ecal[1][0] + ecal[1][1]) != 0:
            if ecal[1][0] != 0:
                attr_entropy2 = (ecal[1][0] / (ecal[1][0] + ecal[1][1]) * math.log(
                    (1 / ((ecal[1][0] / (ecal[1][0] + ecal[1][1])))), 2))
            if ecal[1][1] != 0:
                attr_entropy2 += (ecal[1][1] / (ecal[1][0] + ecal[1][1]) * math.log(
                    (1 / ((ecal[1][1] / (ecal[1][0] + ecal[1][1])))), 2))
            attr_entropy2 *= ((ecal[1][0] + ecal[1][1]) / len(x1))
            # print("1",attr_entropy2)

        if (ecal[2][0] + ecal[2][1]) != 0:
            if ecal[2][0] != 0:
                attr_entropy3 = (ecal[2][0] / (ecal[2][0] + ecal[2][1]) * math.log(
                    (1 / ((ecal[2][0] / (ecal[2][0] + ecal[2][1])))), 2))
            if ecal[2][1] != 0:
                attr_entropy3 += (ecal[2][1] / (ecal[2][0] + ecal[2][1]) * math.log(
                    (1 / ((ecal[2][1] / (ecal[2][0] + ecal[2][1])))), 2))
            attr_entropy3 *= ((ecal[2][0] + ecal[2][1]) / len(x1))
            # print("2",attr_entropy3)
        attr_entropy = attr_entropy1 + attr_entropy2 + attr_entropy3
        if (e - attr_entropy) > maxGain:
            maxAttribute = i
        maxGain = max(maxGain, (e - attr_entropy))

    F = maxGain * (len(x1) / len(a))
    if flag == 1:
        a0 = []
        a1 = []
        a2 = []
        for j in range(len(x1)):
            if x1[j][maxAttribute] == 0:
                a0.append(p[j])
            elif x1[j][maxAttribute] == 1:
                a1.append(p[j])
            else:
                a2.append(p[j])
        i = 0
        if len(a0) != 0:
            f.write(str(key)+str(i)+" "+str(a0)+"\n")
            i += 1
        if len(a1) != 0:
            f.write(str(key)+str(i)+" "+str(a1)+"\n")
            i += 1
        if len(a2) != 0:
            f.write(str(key)+str(i)+" "+str(a2)+"\n")
    return F
    # print("maxGain is: ", maxGain, "maxAttr: ",maxAttribute, "F: ", maxGain*(len(x1)/len(a)))

print("Enter names of the files dataset input-partition output-partition")
dataset = input()
inputpartitn = input()
outputpartitn = input()

with open(dataset) as f:
    row, col = [int(x) for x in next(f).split()] # read first line
    a = []
    for line in f: # read rest of lines
        a.append([int(x) for x in line.split()])

d = {}
with open(inputpartitn) as f:
        for line in f:
            temp = []
            key, val = line.rstrip().split(None,1)
            temp.append([int(x) for x in val.split()])
            d[key] = temp

maxF = 0
maxKey = ""
for key in d:
    # print("calF",calF(d[key][0]))
    res = calF(d[key][0],0)
    if maxF < res:
        maxF = res
        maxKey = key

with open(outputpartitn,'w') as f:
    for k,v in d.items():
        if k != maxKey:
            f.write(str(k)+ " "+ str(v[0]))
            f.write("\n")
        else:
            res = calF(d[k][0],1)













