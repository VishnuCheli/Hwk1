#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    s = input()

    from collections import OrderedDict
    OD=OrderedDict()
    checkList=[]
    
    for l in s:
        if(l not in checkList):
            OD[l]=(s.count(l))
            checkList.append(l)
        List=sorted(OD.items(),key=lambda x:(-x[1],x[0]))

print(List[0][0],List[0][1])
print(List[1][0],List[1][1])
print(List[2][0],List[2][1])