# Calculate the volume and surface area on the STL model using Python
# Author: Yaswin Prakash

import math

def Calculate():
    file = open(r'$FilePath',"r")
    lines = file.readlines()
    file.close()
    
    ReqList = []
    Volume = SurfaceArea = 0
    
    for i in lines:
        if 'normal' in i:
            ReqA = i.split()
            ReqList.append([float(ReqA[-3]), float(ReqA[-2]), float(ReqA[-1])])
        if 'vertex' in i:
            ReqB = i.split()
            ReqList.append([float(ReqB[-3]), float(ReqB[-2]), float(ReqB[-1])])
    
    def FindLength(a, b):
        return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2 )
    
    def Area(d, e, f):
        a = FindLength(d, e)
        b = FindLength(e, f)
        c = FindLength(f, d)
        s = (a+b+c)/2.0
        return math.sqrt(s * (s-a) * (s-b) * (s-c))
    
    def Centroid(l, m, n):
        return (l[0]+m[0]+n[0])/3, (l[1]+m[1]+n[1])/3, (l[2]+m[2]+n[2])/3
    
    for k in range(0, len(ReqList), 4):
        nCap = ReqList[k]
        Cen = Centroid(ReqList[k+1], ReqList[k+2], ReqList[k+3])
        Fa = Cen[0]/3
        Fb = Cen[1]/3
        Fc = Cen[2]/3
        AofTri = Area(ReqList[k+1], ReqList[k+2], ReqList[k+3])
        SurfaceArea = SurfaceArea + AofTri
        Volume = Volume + (((nCap[0]*Fa) + (nCap[1]*Fb) + (nCap[2]*Fc)) * AofTri)
    
    print('Total Surface Area of the STL model = ', SurfaceArea)
    print('Volume of the STL model = ', Volume)

Calculate()
