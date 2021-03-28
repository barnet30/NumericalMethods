import numpy as np
from math import factorial
import pandas as pd
from matplotlib import pyplot as plt
from KursProject.task1 import x_array, f_array


def add(p1,p2):

    x = [0]*(max(p1[0][1],p2[0][1])+1)
    for i in p1+p2:
        x[i[1]]+=i[0]
    res =  [[x[i],i] for i in range(len(x)) if x[i]!=0]
    res.sort(key = lambda r: r[1], reverse= True)
    return res

def mul(p1,p2):

    x = [0]*(p1[0][1]*p2[0][1]+2)
    for i in p1:
        for j in p2:
            x[i[1]+j[1]]+=i[0]*j[0]
    res = [[x[i],i] for i in range(len(x)) if x[i]!=0]
    res.sort(key = lambda r: r[1], reverse= True)
    return res

def mul_numb(p1, numb):
    res = [[i[0] * numb,i[1]] for i in p1]
    return res

def poly_val(p1, value):
    poly = p1
    poly.sort(key=lambda r:r[1])
    res = poly[0][0]
    x = 1
    for i in range(1, len(poly)):
        x *= value
        res += x*poly[i][0]
    return res

n = len(x_array)

lagranz = [(0,0),(0,0)]
poly = list()

for i in range(n):
    denom = 1
    for j in range(n):
        if i!=j:
            denom *= (x_array[i] - x_array[j])
            if j==0 or (i==0 and j==1):
                poly = [[1,1],[-x_array[j],0]]
            else:
                poly = mul(poly,[[1,1],[-x_array[j],0]])

    if f_array[i]!=0:
        coef = f_array[i]/denom
        poly = mul_numb(poly, coef)
        lagranz = add(lagranz,poly)
print(lagranz)

print(poly_val(lagranz, x_array[2]),f_array[2])