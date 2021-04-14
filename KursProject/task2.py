import numpy as np
from math import factorial
import pandas as pd
from matplotlib import pyplot as plt
from KursProject.task1 import x_array,f_array,taylor

a = 0
b = 3
n=10
def make_uniform_partition(a,b,n):
    return np.linspace(a,b,num=n)

def add(p1,p2):

    x = [0]*(max(p1[0][1],p2[0][1])+1)
    for i in p1+p2:
        x[i[1]]+=i[0]
    res =  [[x[i],i] for i in range(len(x)) if x[i]!=0]
    res.sort(key = lambda r: r[1], reverse= True)
    return res

def mult(p1,p2):

    x = [0]*(p1[0][1]*p2[0][1]+2)
    for i in p1:
        for j in p2:
            x[i[1]+j[1]]+=i[0]*j[0]
    res = [[x[i],i] for i in range(len(x)) if x[i]!=0]
    res.sort(key = lambda r: r[1], reverse= True)
    return res

def mult_numb(p1, numb):
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


def interpolation_lagranz(x):
    lagranz = [(0, 0), (0, 0)]
    n = len(x)

    poly = list()

    for i in range(n):
        denom = 1
        for j in range(n):
            if i != j:
                denom *= (x[i] - x[j])
                if j == 0 or (i == 0 and j == 1):
                    poly = [[1, 1], [-x[j], 0]]
                else:
                    poly = mult(poly, [[1, 1], [-x[j], 0]])

        f_ksi = taylor(x[i])
        if f_ksi[i] != 0:
            coef = f_ksi[i] / denom
            poly = mult_numb(poly, coef)
            lagranz = add(lagranz, poly)
    return lagranz

errors = []
for i in range(n,101,20):
    x_array = make_uniform_partition(a,b,i)
    lagragnz = interpolation_lagranz(x_array)
    diff = [abs(taylor(x_value)[0] - poly_val(lagragnz,x_value)) for x_value in x_array]
    errors.append([n,max(diff)])

print(errors)
