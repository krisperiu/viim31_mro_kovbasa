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
points1 = [[],[],[],[],[],[]]
points = []
kolvpoints = 0
for i in range(2):
    triangles[i].dataf(f'Triangle{i+1}.txt')
    print(triangles[i].f_t)
    plt.plot([triangles[i].f_t[0][0],triangles[i].f_t[1][0],triangles[i].f_t[2][0],triangles[i].f_t[0][0]],[triangles[i].f_t[0][1],triangles[i].f_t[1][1],triangles[i].f_t[2][1],triangles[i].f_t[0][1]])

for i in range(2):
    while (triangles[i].c < x[i]):
        a = [random.random()*25.0, random.random()*30.0]
        p1 = (triangles[i].f_t[0][0] - a[0]) * (triangles[i].f_t[1][1] - triangles[i].f_t[0][1]) - (triangles[i].f_t[1][0] - triangles[i].f_t[0][0]) * (triangles[i].f_t[0][1] - a[1])
        p2 = (triangles[i].f_t[1][0] - a[0]) * (triangles[i].f_t[2][1] - triangles[i].f_t[1][1]) - (triangles[i].f_t[2][0] - triangles[i].f_t[1][0]) * (triangles[i].f_t[1][1] - a[1])
        p3 = (triangles[i].f_t[2][0] - a[0]) * (triangles[i].f_t[0][1] - triangles[i].f_t[2][1]) - (triangles[i].f_t[0][0] - triangles[i].f_t[2][0]) * (triangles[i].f_t[2][1] - a[1])
        if (p1>=0 and p2>=0 and p3>=0) or (p1<=0 and p2<=0 and p3<=0):
            plt.scatter(a[0],a[1])
            points1[i].append([a[0],a[1]])
            points.append([str(a[0]),str(a[1])])
            triangles[i].c +=1
for i in range(3):
    kolvpoints += triangles[i].c
    print(triangles[i].c)
print(kolvpoints)

def ho_kashiyap(array):
    x_mas = []
    z = []
    schet=0
    for i in range(len(array[0])):
        x_mas.append([array[0][i][0], array[0][i][1], 1])
        z.append([1])
    for i in range(len(array[1])):
        x_mas.append([array[1][i][0], array[1][i][1], 1])
        z.append([-1])
    x_mas=np.asarray(x_mas)
    z=np.asarray(z)
    V = z * x_mas
    e = -np.inf * np.ones([len(z), 1])
    y = np.ones([len(z), 1])
    while np.any(e < 0):
        w = np.dot(np.linalg.pinv(V), y)
        e = y - np.dot(V, w)
        y = y - e * (e < 0)
        schet+=1
        if (schet>=1000):
            break
    x1=np.array([0,25])
    x2=-(w[2]+x1*w[0])/w[1]
    plt.ylim(0,30)
    plt.plot([x1[0],x1[1]],[x2[0],x2[1]],'black')
    schet=0

x=ho_kashiyap(points1)
with open('out.txt','w') as fileout:
    for i in range(kolvpoints):
        fileout.write('('+ points[i][0]+','+points[i][1]+')'+'\n')
