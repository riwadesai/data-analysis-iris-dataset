import pandas as pd
from numpy import array
import numpy as np
import matplotlib.pyplot as plt
import math


data1 = pd.read_csv("/Users/riwadesai/Documents/mathfordatascience/Iris_Data.txt")
x = list(data1.columns)
Iris_Data = array(data1)
print("No. of observations: ",len(Iris_Data))
print("No. of variables: ",len(Iris_Data[0]))
setosa = []
versicolor=[]
virginica=[]
for i in range(len(Iris_Data)): 
    if Iris_Data[:,4][i]=="Setosa":
        setosa.append(Iris_Data[i])
    elif Iris_Data[:,4][i]=="Versicolor":
        versicolor.append(Iris_Data[i])
    else:
        virginica.append(Iris_Data[i]) 
setosa = array(setosa)
virginica = array(virginica)
versicolor = array(versicolor)   
data = [Iris_Data,setosa,versicolor,virginica]
name = ['Iris Data', 'Setosa', 'Versicolor', 'Virginica']
for i in range(len(data)):
    data[i] = data[i][:, :-1]
def mean(data):
    x=0
    for i in range(len(data)):
        x=x+data[i]
    return x/len(data)
def min(data):
    x = data[0]
    for i in range(len(data)):
        if(x>=data[i]):
            x = data[i]
    return x
def max(data):
    x = data[0]
    for i in range(len(data)):
        if(x<=data[i]):
            x = data[i]
    return x
def median(data):
    median = len(data)//2
    return data[median]
def qua(data):
    data = np.sort(data)
    m = len(data)//2
    med = data[m]
    q3 = median(data[m:])
    q1 = median(data[:m])
    return q1,med,q3
def summary(data,x):
    for i in range(len(data[0])):
        dq1,dmed,dq3 = qua(data[:,i])
        print(x[i],"\n", "Min. :" , min(data[:,i]),"\n","1st Qu. :",dq1,"\n","Median :",dmed,"\n","Mean :",round(mean(data[:,i]),3),"\n", "3rd Qu. :",dq3,"\n","Max. :", max(data[:,i]),"\n")
def plot(data,x):
    plt.title("Scatter plot")
    plt.xlabel(x[0])
    plt.ylabel(x[2])
    plt.scatter(data[:,0],data[:,2])
    plt.draw()
    plt.show()
def plot3(data1,data2,data3,x):
    plt.title("Scatter plot")
    plt.xlabel(x[0])
    plt.ylabel(x[2])
    plt.scatter(data1[:,0],data1[:,2], color = 'pink', label = 'Setosa')
    plt.scatter(data2[:,0],data2[:,2], color = 'teal', label = 'Versicolor')
    plt.scatter(data3[:,0],data3[:,2], color = 'orange', label = 'Virginica')
    plt.legend()
    plt.draw()
    plt.show()
def covariance(Iris_Data):
    r = len(Iris_Data[0])
    c = len(Iris_Data[0])
    cov_matrix = np.empty((r,c))
    for i in range(len(Iris_Data[0])):
        for j in range(len(Iris_Data[0])):
            sum = 0
            for k in range(len(Iris_Data)):
                x_xi = Iris_Data[k][i]- round(mean(Iris_Data[:,i]))
                y_yi = Iris_Data[k][j]- round(mean(Iris_Data[:,j]))
                product = x_xi*y_yi
                sum = sum+ product
            cov = sum/(len(Iris_Data)-1)
            cov_matrix[i][j] = cov
    print(cov_matrix)
def correlation(Iris_Data):
    r = len(Iris_Data[0])
    c = len(Iris_Data[0])
    cor_matrix = np.empty((r,c))
    for i in range(len(Iris_Data[0])):
        for j in range(len(Iris_Data[0])):
            sum = 0
            sum_x_xi2 = 0
            sum_y_yi2 = 0
            for k in range(len(Iris_Data)):
                x_xi = Iris_Data[k][i]- round(mean(Iris_Data[:,i]))
                y_yi = Iris_Data[k][j]- round(mean(Iris_Data[:,j]))
                product_ = x_xi*y_yi
                sum = sum + product_
                x_xi2 = (x_xi**2)
                sum_x_xi2 = sum_x_xi2 + x_xi2
                y_yi2 = (y_yi**2)
                sum_y_yi2 = sum_y_yi2 + y_yi2
            product = math.sqrt(sum_x_xi2)*math.sqrt(sum_y_yi2)
            cor = sum/product
            cor_matrix[i][j]=cor
    print(cor_matrix)
def printing(x,y,z):
    for i in range(len(x)):
        print("summary statistics and plot for the entire data ",y[i],":") 
        summary(x[i],z)
        plot(x[i],z)
    for i in range(len(x)):
        print("Covariance matrix for",y[i],":")
        covariance(x[i])
        print("\n")
        print("Correlation matric for",y[i],":")
        correlation(x[i])
        print("\n")
    plot3(x[1],x[2],x[3],z)
printing(data,name,x)
