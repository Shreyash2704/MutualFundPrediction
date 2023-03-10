import pandas as pd
import numpy
import os
import datetime


dir_ = os.getcwd()
file = os.path.join(dir_,"dataset","SBI Contra Fund 5year.csv")

df = pd.read_csv(file)
df = df.dropna()
df = df.drop(columns=["High","Low","Close","Adj Close","Volume"],axis=1)
daily_return = [0]
open_ = list(df["Open"])

for i in range(1,len(open_)):
    ele = (open_[i]-open_[i-1])/open_[i-1]
    daily_return.append(ele*100)

month_return = {}
dates = list(df["Date"])

for i in range(len(dates)):
    ele = dates[i].split("-")
    date = datetime.date(int(ele[0]),int(ele[1]),int(ele[2]))
    if str(date.month)+"-"+str(date.year) in month_return.keys():
        month_return[str(date.month)+"-"+str(date.year)].append(daily_return[i])
    else:
        month_return[str(date.month)+"-"+str(date.year)] = [daily_return[i]]

for k,v in month_return.items():
    ele = sum(v)/len(v)
    month_return[k] = ele


avg_month_return = []
for i in list(df["Date"]):
    ele = i.split("-")
    date = datetime.date(int(ele[0]),int(ele[1]),int(ele[2]))
    avg_month_return.append(month_return[str(date.month)+"-"+str(date.year)])
rfr = [0.21]*len(avg_month_return)

pdr = [0.0]+daily_return[0:len(daily_return)-1]
excess_return = []
for i in range(len(daily_return)):
    excess_return.append((pdr[i])-rfr[i])


#df["daily_return"] = daily_return
df["avg_month_return"] = avg_month_return
df["risk_free_rate"] = rfr
df["excess_return"] = excess_return
df["previous_close"] = [0.0]+open_[0:len(open_)-1]
df["previous_day_return"] = [0.0]+daily_return[0:len(daily_return)-1]
print(df)
df.to_csv("SBI Contra fund featured data.csv")