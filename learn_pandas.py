import pandas as pd 
import numpy as np 
#create data frame 
new_array = np.arange(0,20).reshape(5,4)
print(new_array)
data_create =pd.DataFrame(data=np.arange(0,20).reshape(5,4),index=['row1',"row2",'row3','row4','row5'],columns=['col1','col2','co]3','col4'])
print(data_create.head(2))#shows data from top 2
print(data_create.tail(2))#data from bottom 2
print(type(data_create)) #datframe in answer
print(data_create.info())#gives datatype of columnes
print(data_create.describe())
print(data_create['col1']) #its datatype is series because have only one column
print(data_create[['col1' , 'col2']])#its datatype is dataframe  have muktiple column and in tabular form
print(data_create.loc['row3']) #use loc for row
print(data_create.head())
print(data_create.iloc[0:2,2:]) #byr using both column and index number
print(data_create.iloc[:,[0,-1]]) #will give first ad last columnpront
print(data_create.iloc[:,1:].values) #convert it into array removes rows and column
#basic operations
print(data_create.isnull().sum())# this gives a if null values are there and gives sum of null values 

df = pd.DataFrame(data=[[1,np.nan,3],[1,2,3]],index=['row1','row2'],columns=['c1','c2','c3'])#np.nan gives null valuse

print(df)
print(df.isnull().sum())
print(df['c1'].value_counts())
print(df['c1'].unique())
print(df>1)
print(df[df['c2']>1])
# print(df.loc[['row1','row2'],:]) 