import enum
from re import A
import numpy as np
from scipy.interpolate import lagrange

# import fraction
# np.set_printoptions(formatter={'all':lambda x: str(fraction.Fraction(x).limit_denominator())})

# f(x): x^3+3x+8

a_1 = [0,1,0,0,0,0,0]
b_1 = [0,1,0,0,0,0,0]
c_1 = [0,0,1,0,0,0,0]

a_2 = [0,0,1,0,0,0,0]
b_2 = [0,1,0,0,0,0,0]
c_2 = [0,0,0,1,0,0,0]

a_3 = [3,0,0,0,0,0,0]
b_3 = [0,1,0,0,0,0,0]
c_3 = [0,0,0,0,1,0,0]

a_4 = [0,0,0,1,1,0,0]
b_4 = [1,0,0,0,0,0,0]
c_4 = [0,0,0,0,0,1,0]

a_5 = [8,0,0,0,0,1,0]
b_5 = [1,0,0,0,0,0,0]
c_5 = [0,0,0,0,0,0,1]

a_i = [a_1,a_2,a_3,a_4,a_5]
b_i = [b_1,b_2,b_3,b_4,b_5]
c_i = [c_1,c_2,c_3,c_4,c_5]

constraints = [a_i,b_i,c_i]
c_names = ['a','b','c']

A_i = []
B_i = []
C_i = []

polys = [A_i,B_i,C_i]

s = [1, 3, 9, 27, 9, 36, 44]

for k in range(len(a_1)):
    for i in range(3):
        x = []
        y = []
        for j in range(len(constraints[i])):
            x.append(j+1)
            y.append(constraints[i][j][k])
        pp = lagrange(x,y)
        polys[i].append(pp)
        #print(c_names[i]+"_"+ str(k+1) + " = " + str(pp) + "\n")
        
p = np.dot(A_i,s)*np.dot(B_i,s)-np.dot(C_i,s)

# print(p)
# for c in p.c:
    # print(format(c, '.60g'))

# check zeroes
for i in range(len(a_i)):
    print(abs(round(p(i+1),3)))


