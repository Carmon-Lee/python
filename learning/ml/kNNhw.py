import numpy as np
import os
import operator


def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort()
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]


def img2vector(filename):
    fr=open(filename)
    returnVec=np.zeros((1,1024))
    for i in range(32):
        line=fr.readline()
        for j in range(32):
            returnVec[0,32*i+j]=int(line[j])
    return returnVec
    # print(returnVec)


img2vector("machinelearninginaction/Ch02/digits/testDigits/0_0.txt")
def handwritingClass():
    hwLabels=[]
    digitDir='machinelearninginaction/Ch02/digits/trainingDigits'
    files=os.listdir(digitDir)
    m=len(files)
    trainmaterial=np.zeros((m,1024))
    for i in range(m):
        file=files[i]
        fileStr=file.split('.')[0]
        classNumStr=fileStr.split('_')[0]
        hwLabels.append(classNumStr)
        trainmaterial[i,:]=img2vector(digitDir+"/"+file)
    testfileDir='machinelearninginaction/Ch02/digits/testDigits'
    testfiles=os.listdir(testfileDir)
    errorcount=0.0
    mTest=len(testfiles)
    for i in range(mTest):
        file = testfiles[i]
        fileStr = file.split('.')[0]
        classNumStr = fileStr.split('_')[0]
        vectorundertest=img2vector(testfileDir+"/"+file)
        classfierResult=classify0(vectorundertest,trainmaterial,hwLabels,3)
        # print(classfierResult,classNumStr)
        if(classfierResult!=classNumStr):
            errorcount+=1.0
    print('error rate:%f'%(errorcount/float(mTest)))

handwritingClass()

