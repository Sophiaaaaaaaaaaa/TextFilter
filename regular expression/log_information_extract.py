# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 20:21:37 2019

@author:sophia
"""
import re
from matplotlib import pyplot
import matplotlib.pyplot as plt
from tkinter import *
li=[]
reaction_log1= open('Spyder  Python\\propylene.log').read()
reaction_log2=open(r'Spyder  Python\\bh3.log').read()
TS_log=open(r'Spyder  Python\3-ts-1.log').read()
products_log=open(r'Spyder  Python\p-mark.log').read()
li.append(reaction_log1)
li.append(reaction_log2)
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


 
x = ['reaction','TS','Product']
y=[]
y.append(abs(thermal_Free_Energies[0]+thermal_Free_Energies[1]))
y.append(y[0]-abs(thermal_Free_Energies[2])/y[0]*100)
if (abs(thermal_Free_Energies[3])/(abs(thermal_Free_Energies[0]+thermal_Free_Energies[1]))>1):
    y.append(y[0]-abs(thermal_Free_Energies[3])/y[0]*100)
else:
    y.append(y[0]+abs(thermal_Free_Energies[3])/y[0]*100)
# 创建窗口
root = Tk()
# 创建并添加Canvas
cv = Canvas(root,  width = 200, height = 200, background='white')
cv.pack(fill=BOTH, expand=YES)
cv.create_rectangle(30,y[0], 55, y[0]+1,
    outline='black', # 边框颜色
    fill="black", # 填充颜色
    width=5 # 边框宽度
    )

cv.create_rectangle(80, y[1], 105, y[1]+1,
    outline='black', # 边框颜色0
    fill="black", # 填充颜色
    width=5 # 边框宽度
    )
cv.create_line(
                  55, y[0]+1,
                  80, y[1],
                  fill='black',  # 红色
                  dash=(4, 4)  # 虚线
             )

cv.create_rectangle(130, y[2], 155,y[2]+1,
    outline='black', # 边框颜色
    fill="black", # 填充颜色
    width=5 # 边框宽度
    )
cv.create_line(
                  105, y[1]+1,
                  130, y[2],
                  fill='black',  # 黑色
                  dash=(4, 4)  # 虚线
             )

root.mainloop()

print(y)
