from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser 
import pickle
import os
from datetime import datetime
import pandas 
import numpy as np
from sklearn import preprocessing




dir = os.getcwd()
path = os.path.join(dir,"model")
files = os.listdir(path)


#rfr_model=pickle.load(open(path,'rb+'))
model_list = []


for i in files:
    name = os.path.join(path,i)
    model = pickle.load(open(name,'rb+'))
    model_list.append(model)
print("models loaded.")

path2 = os.path.join(dir,"merged_model","linearRegressorCombined_model.pkl")
#print(os.listdir(path2))
merged_model = pickle.load(open(path2,'rb+'))

scalerfile = os.path.join(dir,'scaler.sav')
mm = pickle.load(open(scalerfile, 'rb'))


def convert_to_dateString(arr):
    ans = []
    for i in arr:
        x = i.split('-')
        x_ = x[2]+"-"+x[1]+"-"+x[0]
        ans.append(x_)
    return ans

csv_list = []
csv_files = os.listdir(os.path.join(dir,"csv_data"))


@api_view(['GET'])
def ReadCsv(request):
    datano = int(request.GET['data_no'])
    pd = pandas.read_csv(os.path.join(dir,"csv_data",csv_files[datano]))
    pd = pd.dropna()
    date = list(pd["Date"])
    nav = list(pd["Open"])
    return Response({"fund_name":csv_files[datano].split('.')[0],"Nav_Length":len(nav),"leangth-date":len(date),"Nav":nav,"Date":date})


@api_view(['GET'])
def index(request):
    day = 3
    month = 11
    year = 2022
    dur = 3
    ans,date_arr = predict_future_nav(2,dur,day,month,year)
    return Response({"data":ans,"date":date_arr}) 

@api_view(['GET'])
def fundnames(request):
    fundname = ['sbi consumption opportunities fund.csv',
    'sbi contra fund.csv',
    'SBI Equity Hybrid Fund.csv',
    'sbi focused fund.csv',
    'sbi healthcare opportunities fund.csv',
    'SBI Large & Midcap Fund.csv',
    'SBI Magnum Equity ESG Fund.csv',
    'SBI Magnum Income Fund.csv',
    'SBI Nifty Index Fund.csv',
    'sbi small cap.csv']
    return Response([ele.split(".")[0] for ele in fundname])

@api_view(['POST'])
def getNav(request):
    data = JSONParser().parse(request)
    modelno = data["fundno"]
    day = int(data["day"])
    month = int(data["month"])
    year = int(data["year"])
    input = [day,month,year]
    value = model_list[int(modelno)].predict([input])
    print(value[0])
    return Response(round(value[0],2))
    
def PredictBestMutualFund_merged(day,month,year,duration,algo):
    start = []
    end = []
    ans_start = []
    ans_end = []
    ans = []
    m = duration[0]
    y = duration[1]
    
    ele = (month+m)//12
    m = (month+m)%11
    
    y =y+ele+year
    input_start = [[day,month,year,0,0,0,0,0,0,0,0,0,0]]*10
    input_end = [[day,m,y,0,0,0,0,0,0,0,0,0,0]]*10
    
    for i in range(10):
        x = input_start[i].copy()
        start.append(x)
        y = input_end[i].copy()
        end.append(y)
    
    for i in range(len(start)):
        start[i][i+3] = 1
        end[i][i+3] = 1
        x = algo.predict([start[i]])
        y = algo.predict([end[i]])
        ans_x = np.array(x[0]).reshape(-1,1)
        ans_x = mm.inverse_transform(ans_x)
        ans_x = ans_x[0][0]
        
        ans_y = np.array(y[0]).reshape(-1,1)
        ans_y = mm.inverse_transform(ans_y)
        ans_y = ans_y[0][0]
        
        ans_start.append(ans_x)
        ans_end.append(ans_y)
        ans.append(CalculateReturn(ans_x,ans_y))
        
    return ans

def PredictBestMutualFund(day,month,year,duration,algo):
    start = []
    end = []
    ans_start = []
    ans_end = []
    ans = []
    m = duration[0]
    y = duration[1]
    
    ele = (month+m)//12
    m = (month+m)%13
    y =y+ele+year
    
    input_start = [[day,month,year]]*len(algo)
    input_end = [[day,m,y]]*len(algo)
    for i in range(len(algo)):
        x = input_start[i].copy()
        start.append(x)
        y = input_end[i].copy()
        end.append(y)
    
    for i in range(len(start)):
        x = algo[i].predict([start[i]])
        y = algo[i].predict([end[i]])
        ans_start.append(x[0])
        ans_end.append(y[0])
        ans.append(CalculateReturn(x[0],y[0]))
    return ans


def CalculateReturn(start,end):
    returns = (end-start)/start
    returns = returns*100
    
    return returns
    
fund_list = ['SBI Consumption Opportunities Fund',
 'SBI Contra Fund',
 'SBI Equity Hybrid Fund',
 'SBI Focused Fund',
 'SBI Healthcare Opportunities Fund',
 'SBI Large & Midcap Fund',
 'SBI Magnum Equity ESG Fund',
 'SBI Magnum Income Fund',
 'SBI Nifty Index Fund',
 'SBI small cap']

def get_max_return_fund(l):
    max_return = 0
    index = -1
    for i in range(len(l)):
        if l[i]>max_return:
            max_return = l[i]
            index = i
    return [round(max_return,3),index]


def get_top3_max_return_fund(l):
    exist = []
    max_return = []
    fundno = []
    for i in range(3):
        max = 0
        index = -1
        for j in range(len(l)):
            if l[j] > max and l[j] not in exist:
                max = l[j]
                index = j
        exist.append(max)
        max_return.append(round(max,2))
        fundno.append(fund_list[index])

    return max_return,fundno

def getFundName(ans_list):
    return fund_list[get_max_return_fund(ans_list)[1]]

@api_view(["POST"])
def getBestMF(request):
    data = JSONParser().parse(request)
    date = datetime.now()

    day = date.day
    month = date.month
    year = date.year
    
    dur_m = int(data["dur_m"])
    dur_y = 0

    value = PredictBestMutualFund(day,month,year,[dur_m,dur_y],model_list)
    print(value)
    ans,fn = get_top3_max_return_fund(value)
    
    data_dict = {}
    data_dict["ans_list"] = value
    data_dict["max_ans"] = ans
    data_dict["Fund_name"] = fn
    return Response(data_dict)

def generate_future_input_arr(duration,day,month,year):
    #algo = model_list[fundno]
    input_arr = []

    for i in range(duration):
        if month+i == 12:
            if i == 0:
                for j in range(day,31):
                    input_arr.append([j, (month+i), year])
            else:
                for j in range(1,31):
                    input_arr.append([j, (month+i), year])
        else:
            if i == 0:
                for j in range(day,31):
                    input_arr.append([j, (month+i)%12, year+((month+i)//12)])
            else:
                for j in range(1,31):
                    input_arr.append([j, (month+i)%12, year+((month+i)//12)])
    return input_arr  

def convertToDate(arr):
    ans = []
    for i in arr:
        #print(i)
        x = str(i[2])+"-"+str(i[1])+"-"+str(i[0])
        ans.append(str(x))
    return ans


def predict_future_nav(modelno,duration,day,month,year):
    input_arr = generate_future_input_arr(duration,day,month,year)

    algo = model_list[modelno]
    ans = []
    for i in range(len(input_arr)):
        ans.append(algo.predict([input_arr[i]])[0])

    new_input = convertToDate(input_arr)
    return ans,new_input

@api_view(["POST"])
def future_nav(request):
    data = JSONParser().parse(request)
    model_no = int(data["modelno"])
    duration = int(data["duration"])
    date = datetime.now()

    day = date.day
    month = date.month
    year = date.year

    ans,date_arr = predict_future_nav(model_no,duration,day,month,year)
    return Response({"fund_name":csv_files[model_no].split('.')[0],"Nav":ans,"Date":date_arr})
    
    
@api_view(["POST"])
def all_future_nav(request):
    data = JSONParser().parse(request)
    duration = int(data["duration"])
    all_data = []
    date = datetime.now()

    day = date.day
    month = date.month
    year = date.year
    
    date_arr = []
    for i in range(len(fund_list)):
        ans,date_arr = predict_future_nav(i,duration,day,month,year)
        all_data.append(ans)
    
    return Response({"data":all_data,"fund_name":fund_list,"dates":date_arr})
        
    
    
@api_view(["POST"])
def bestMFMerged(request):
    data = JSONParser().parse(request)
    date = datetime.now()

    day = date.day
    month = date.month
    year = date.year
    
    dur_m = int(data["dur_m"])
    dur_y = 0

    value = PredictBestMutualFund_merged(day,month,year,[dur_m,dur_y],merged_model)
    print(value)
    ans,fn = get_top3_max_return_fund(value)
    
    data_dict = {}
    data_dict["ans_list"] = value
    data_dict["max_ans"] = ans
    data_dict["Fund_name"] = fn
    return Response(data_dict)

    
    