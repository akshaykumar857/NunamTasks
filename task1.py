#Author name:Akshay kumar-190970013
import pandas as pd
import csv

def combine(listdata,listname):
    path1 = 'C:\\Users\\user\\Downloads\\Data Engineer\\'
    path2 = 'C:\\Users\\user\\Documents\\Deliverable\\'
    df = pd.DataFrame()
    for k in listname:
        for i in listdata:
            xl=pd.ExcelFile(path1+i)
            for j in xl.sheet_names:
                if j.startswith(k):
                    df_tmp = xl.parse(j)
                    df = df.append(df_tmp)
        df.to_csv(path2+k+'.csv',index = False, header=True)

listdata=['data.xls','data_1.xls']
listname=['Detail_67_','DetailVol_67_','DetailTemp_67_']
combine(listdata,listname)

