import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import csv
import numpy as np

data=pd.read_csv("data_korona_dki_x.txt",sep=",")
print(data)
print("Describe :",data.describe())

x=[]
y=[]
z=[]
xx=[]

with open("data_korona_dki_x.txt","r") as csvfile:
    plots=csv.reader(csvfile,delimiter=",")
    for row in plots:
        x.append(row[0])
        y.append(int(row[1]))
        z.append(int(row[2]))
        xx.append(int(row[3]))
        
fig,ax=plt.subplots()                

ax.plot(x,y,marker="o",label="Kasus Baru")
ax.plot(x,z,marker="x",label="Meninggal")
ax.plot(x,xx,marker="+",label="Sembuh")
plt.title("Data Korona Jakarta")
plt.xlabel("Tanggal")
plt.ylabel("Jumlah")
plt.xticks(rotation=90)
legend=ax.legend(loc="upper left", shadow=True)

for i,j in zip(x,y):
    ax.annotate('%s' %j,xy=(i,j),xytext=(4,0), textcoords='offset points')    

for a,b in zip(x,z):
    ax.annotate('%s' %b,xy=(a,b),xytext=(4,0), textcoords='offset points')    

for d,e in zip(x,xx):
    ax.annotate('%s' %e,xy=(d,e),xytext=(4,0), textcoords='offset points')        
#plt.xticks(x)
#plt.yticks(y)

# move_figure(fig,50,50)
print(plt.show())