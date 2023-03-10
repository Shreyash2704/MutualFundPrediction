import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split

def ConvertDateintoDay_Month_Year(df):
    #newdf = pd.DataFrame()
    df.Date = pd.to_datetime(df.Date)
    #df["Nav"] = df.Nav
    df["day"] = df.Date.dt.day
    df["month"] = df.Date.dt.month
    df["year"] = df.Date.dt.year
    df["day_of_week"] = df.Date.dt.dayofweek
    df = df.drop(columns=["Unnamed: 0","Date"],axis=1)
    return df

directory =  os.path.join(os.getcwd())
file = r"SBI Contra fund featured data.csv"
df = pd.read_csv(os.path.join(directory,file))
df = ConvertDateintoDay_Month_Year(df)
print(df)

newdf = pd.get_dummies(df, columns=['day_of_week', 'month'])

mm = preprocessing.MinMaxScaler()

col_names = list(newdf.columns)
scaled_df = mm.fit_transform(newdf)
scaled_df = pd.DataFrame(scaled_df,columns = col_names)
scaled_df