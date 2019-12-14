
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 21:30:16 2019

@author: lenovo
"""
import math
import itertools
class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y
def combination(n,m):
    list1=[]
    for i in range (n):
       list1.append(i+1) 
    iter = itertools.combinations(list1,m)   
    LC=list(iter)
    return LC
def GetAreaOfPolyGonbyVector(points):
    # 基于向量叉乘计算多边形面积
    area = 0
    if(len(points)<3):

         raise Exception("error")
    cohesion=len(points)-1
    for i in range(cohesion):
        p1 = points[i]
        p2 = points[i + 1]

        triArea = (p1.x*p2.y - p2.x*p1.y)/2
        area += triArea
        if (i == (cohesion-1)):
         p1 = points[i+1]
         p2 = points[0]
         triArea = (p1.x*p2.y - p2.x*p1.y)/2
         area += triArea
    return abs(area)
def func1(one_list):
  '''''
  去除列表的重复元素
  '''
  return list(set(one_list))
dict_a = {
          '1':[1.73,2],
          '2':[3.46,1],
          '3':[3.46,-1],
          '4':[1.73,-2],
          '5':[-1.73,-2],
          '6':[-3.46,-1],
          '7':[-3.46,1],
          '8':[-1.73,2],
          
          
          
          }#由于萘的中心9 10 号碳并不能取代，故去除，取边长为2
n=8
m=3
LC=combination(n,m)
number=len(LC)
end=[]
area1=[]
for i in range(number):
    x=[]
    y=[]
    serial_number=[]# C的序号和坐标
    for j in range(m):
        c=str(LC[i][j])
        x.append(dict_a[c][0])
        y.append(dict_a[c][1])
        serial_number.append(c)
    
    points = []
    for index in range(len(x)):
         points.append(Point(x[index],y[index]))
    area =round( GetAreaOfPolyGonbyVector(points),3)
    area1.append(area)
    serial_number.insert(0,area)
    end.append(serial_number)
count=0
area1=func1(area1)
print("面积种类",area1)
for i in range(len(area1)):
    for j in range(len(end)):
        if (end[j][0]==area1[i]):
            
            print (end[j])
            break
'''C=[2,3,4,5,6,7,8,1]
C_Number=[2,5,7,13,15,17,20,26]'''
naphthalene='C1=CC=C2C=CC=CC2=C1' #萘的SMILES代码

#根据end结果向smiles代码添加cl        
a=list(naphthalene)
a.insert(2,'(Cl)')
a.insert(5,'(Cl)')
a.insert(13,'(Cl)')
a=''.join(a)
print(a)
