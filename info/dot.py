import pandas as pd
import matplotlib.pyplot as plt
import math


df=pd.read_excel("C:\\Users\\ACER\\Desktop\\info\\data.xlsx",index_col=False)

#print(df.head())

# x=df["Fat"]
# y=df["SNF"]
# R=df["Result"]


t_df=df[df["Result"]=="T"]
f_df=df[df["Result"]=="F"]




ip1=float(input("Enter Fat percent in milk: "))
ip2=float(input("Enter SNF percent in Milk: "))
ip3=int(input("Enter How many clusters? "))

l=[]
for i in range(0,(len(df["Fat"]))):
    s=math.sqrt((ip1-df["Fat"][i])**2+(ip2-df["SNF"][i])**2)
    l.append(s)
dic=pd.DataFrame({"fat":df['Fat'],"snf":df["SNF"],"result":df["Result"],"distance":l})
dic["Rank"]=dic["distance"].rank(ascending=True)
dic.sort_values("Rank",inplace=True)


v=dic.head(ip3)
kk=(v["result"])


sol=max(set(v["result"]))

c1=sol.count("T")
c2 = len([x for x in kk if x == "F"])

if c1>c2:
    print("Okay") 

elif c2>c1:
    print("Not okay")

elif c1==c2:
    print("Okay")

plt.scatter(t_df["Fat"],t_df["SNF"],label="Good",color='green')
plt.scatter(f_df["Fat"],f_df["SNF"],label="bad",color="red")
plt.scatter(ip1,ip2,label="New Data",color="violet")
plt.xlabel("Fat",color="black")
plt.ylabel("SNF",color="black")
plt.title("Quality of Milk")
plt.legend()
plt.show()

