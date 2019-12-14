# -*- coding: utf-8 -*-
import os
import re
import pandas as pd
def find_s(path,end):
  files= os.listdir(path) #得到文件夹下的所有文件名称

  for file in files: #遍历文件夹
     if not os.path.isdir(file): #判断是否是文件夹，不是文件夹才打开
         if file.endswith("reaction"+end):
           reaction_log1= open(path+"/"+file).read(); #打开文件


         if file.endswith("ts"+end):
           TS_log = open(path+"/"+file).read(); #打开文件

         if file.endswith("product"+end):
           products_log = open(path+"/"+file).read(); #打开文件


  li=[]
  li.append(reaction_log1)

  li.append(TS_log)
  li.append(products_log)

  pattern="(Gibbs\s\w+\s*\w+=\s+)([0-9]+.[0-9]+)"
  pattern1="(zero-point\sEnergies=\s+)(-[0-9]+.[0-9]+)"
  pattern2="(thermal\s\w+\s*\w+=\s+)(-[0-9]+.[0-9]+)"
  GFE=[]
  Zero_energy=[]
  thermal_Energies=[]
  thermal_Enthalpies=[]
  thermal_Free_Energies=[]
  i=0
  for i in range(len(li)):
   GFE.append(float(re.findall(pattern,li[i])[0][1]))
   Zero_energy.append(float(re.findall(pattern1,li[i])[0][1]))
   thermal_Energies.append(float(re.findall(pattern2,li[i])[0][1]))
   thermal_Enthalpies.append(float(re.findall(pattern2,li[i])[1][1]))
   thermal_Free_Energies.append(float(re.findall(pattern2,li[i])[2][1]))

  y=[]
  y.append(GFE[0])
  y.append(GFE[1])
  y.append(GFE[2])
 return y


G=[]
for i in range(5):
 b=repr(i+1)
 end=b+".log"
 G.append((find_s(r"C:\Users\lenovo\Desktop\Spyder\os",end)))
new=pd.DataFrame(G,index=['a','b','c','d','e'],columns=['Reaction','Ts','Product'])
print(new)
f2 = open('test.txt','w')
f2.write(str(new))
f2.close()
