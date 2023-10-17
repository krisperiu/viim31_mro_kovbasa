import numpy as np
import matplotlib.pyplot as plt
import random
class Triangle():
    def __init__(self):
        self.c = 0
    def dataf(self, points):
        self.datafile = points
        txt = open(self.datafile,'r')
        self.f_t=[]  
        for i, s in enumerate(txt):
            st=s.strip().lstrip('(').rstrip(')')  
            if ',' in s:
                res=[e.strip() for e in st.split(',')]
            else:
                res=st.split()
            try:    
                res=map(float, res) 
            except ValueError:
                print ('Element {} "{}" is invalid'.format(i,s))
                continue   
            self.f_t.append(list(res)) 
        txt.close


x = []
datafile = open('data.txt','r')
lines = datafile.readlines()
for line in lines:
    LineT=line.strip()
    x.append(int(LineT))

tr1=Triangle()
tr2=Triangle()
tr3=Triangle()
tr4=Triangle()
tr5=Triangle()
tr6=Triangle()
triangles = [tr1,tr2,tr3,tr4,tr5,tr6]
points = []
kolvpoints = 0
for i in range(6):
    triangles[i].dataf(f'Triangle{i+1}.txt')
    print(triangles[i].f_t)
    plt.plot([triangles[i].f_t[0][0],triangles[i].f_t[1][0],triangles[i].f_t[2][0],triangles[i].f_t[0][0]],[triangles[i].f_t[0][1],triangles[i].f_t[1][1],triangles[i].f_t[2][1],triangles[i].f_t[0][1]])

for i in range(6):
    while (triangles[i].c < x[i]):
        a = [random.random()*25.0, random.random()*30.0]
        p1 = (triangles[i].f_t[0][0] - a[0]) * (triangles[i].f_t[1][1] - triangles[i].f_t[0][1]) - (triangles[i].f_t[1][0] - triangles[i].f_t[0][0]) * (triangles[i].f_t[0][1] - a[1])
        p2 = (triangles[i].f_t[1][0] - a[0]) * (triangles[i].f_t[2][1] - triangles[i].f_t[1][1]) - (triangles[i].f_t[2][0] - triangles[i].f_t[1][0]) * (triangles[i].f_t[1][1] - a[1])
        p3 = (triangles[i].f_t[2][0] - a[0]) * (triangles[i].f_t[0][1] - triangles[i].f_t[2][1]) - (triangles[i].f_t[0][0] - triangles[i].f_t[2][0]) * (triangles[i].f_t[2][1] - a[1])
        if (p1>=0 and p2>=0 and p3>=0) or (p1<=0 and p2<=0 and p3<=0):
            plt.scatter(a[0],a[1])
            points.append([str(a[0]),str(a[1])])
            triangles[i].c +=1
for i in range(6):
    kolvpoints += triangles[i].c
    print(triangles[i].c)
print(kolvpoints)
with open('out.txt','w') as fileout:
    for i in range(kolvpoints):
        fileout.write('('+ points[i][0]+','+points[i][1]+')'+'\n')