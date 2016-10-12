#!/usr/bin/env python2.7

class Matrix():
    def __init__(self, *args):
        argsLen=len(args)/2.
        toArgsLen=0
        if(argsLen%2 != 0):
            raise Exception
        argsLen=int(argsLen)
        self.nr=argsLen
        self.matx=[[ [] for i in range(self.nr)] for i in range(self.nr)]
        for i in range(self.nr):
            for j in range(self.nr):
                self.matx[i][j]=args[toArgsLen]
                toArgsLen+=1

    def __str__(self):
        matxStr=''
        for i in range(self.nr):
            for j in range(self.nr):
                matxStr += (str(self.matx[i][j]) + " ")
            matxStr+="\n"
        return matxStr


    def __add__(self,matx2):
        if (len(self.matx) >= len(matx2.matx)):
            nr = len(matx2.matx)
        else:
            nr=len(self.matx)
        for i in range(nr):
            for j in range(nr):
                self.matx[i][j] += matx2.matx[i][j]
        return self.matx


# Testing code
mtx=Matrix(5,1,3,2)
mtx2=Matrix(10,10,10,10)
print mtx
print mtx2

mtx+mtx2
print (mtx)

