#Author name:Akshay kumar-190970013
import pandas as pd 
import datetime as dt

def downsampling(files):
    path1 = 'C:\\Users\\user\\Documents\\Deliverable\\'
    for i in files:
        df = pd.read_csv(path1+i+'.csv')
        if i=='Detail_67_':
            df['Absolute Time'] = pd.to_datetime(df['Absolute Time'])
            include = df[df['Absolute Time'].dt.second==0]
            print(include.head(15)) 
        else:
            df['Realtime'] = pd.to_datetime(df['Realtime'])
            include = df[df['Realtime'].dt.second==0]
            print(include.head(15))         
        include.to_csv(path1+i+'Downsampled.csv', index=False)

df = pd.DataFrame()
files=['Detail_67_','DetailVol_67_','DetailTemp_67_']
downsampling(files)
