# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 12:33:20 2022

@author: Bruce
"""

print("Hello World")

a = 3
print(a)
a = "abc"
print(a)
a =4
b = 5
print(a+b)
print(a*b)

my_list = [10,20,30,40]
print(my_list[0])
print(my_list[1])
print(my_list[-1])
print(my_list[-2])

my_list_2 = [10, "abc", 30, 40]
print(my_list_2[-3])

if 3 > 4:
    print("within if loop")
print("outside loop")

new_list = []
for i in range(10):
    print(i)
    new_list.append(i*3)

print(new_list)

def calculatateSum(a,b):
    return a+b, a/b

var1, var2 = calculatateSum(10,2)
print(var1)
print(var2)

with open("test_file.txt", "w") as f:
    f.write("sample content 1")
    
with open("test_file.txt", "a") as f:
    f.write("sample content 2")
    
with open("test_file.txt", "w") as f:
    f.write("sample content 3")
    

import numpy as np

sample_list = [10, 20, 30 , 40, 50, 60]

sample_numpy_1d_array = np.array(sample_list)

print(sample_numpy_1d_array)

sample_numpy_2d_array = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])

new_arr = sample_numpy_2d_array.reshape(2,6)

new_arr2 = sample_numpy_2d_array.reshape(1,-1)

new_arr3 = sample_numpy_2d_array.reshape(-1,)

new_sample = sample_numpy_2d_array[1:3,2:4]

import pandas as pd

sample_series = pd.Series([10,20,30,40])

sample_series_2 = pd.Series([10,20,30,40],['A', 'B', 'C', 'D'])


x = sample_series_2[2]

y = sample_series_2['C']

sample_dataframe = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])

sample_dataframe2 = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9],[10,11,12]],['Row1', 'Row2', 'Row3', 'Row4'],['Column1','Column2','Column3'])


j = sample_dataframe2['Column3']

k = sample_dataframe2[['Column1', 'Column3']]

l = sample_dataframe2.loc['Row1']

m = sample_dataframe2.loc[['Row2'],['Column3']]

p = sample_dataframe2.iloc[0:2, 1:3]

sample_dataframe2.iloc[1:2, 2:4]

sample_dataframe2.iloc[:, :-1]

type(sample_dataframe2.iloc[:, :-1])

new_numpy_array_2 = sample_dataframe2.iloc[:, :-1].values

#get only greater than 4
sample_dataframe2[sample_dataframe2['Column1']>4]

import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8,9,10]
y = [10,25,35,40,50,60,80,90,95,100]

plt.plot(x,y)

plt.scatter(x,y)
plt.xlabel('X')
plt.ylabe('Y')
plt.title('Sample plot')
plt.plot(x,y)














