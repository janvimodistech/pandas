from io import StringIO
import pandas as pd
file_path = 'Book1.csv'
df = pd.read_csv (file_path)
print(df.head())
data = ('col1,col2,col3\n'
         'x,y,1\n'
         'c,d,2\n'
         'w,e,3\n'
           )
print(type(data))#its a string type data 
 #to convert in memory file use string.io 
a= StringIO(data)
b = pd.read_csv((a),usecols=['col1','col2'])
b = pd.read_csv(a)
print(b['col1'])
print(b.to_csv('test.csv'))
#datatpyes in CSV
data1 = ('col1,col2,col3,col4\n'
          '1,2,3,4\n'
          '2,9,7,6')
new = pd.read_csv(StringIO(data1),dtype='int')
print(new)

print(new.info())
print(new.isnull())
new.head()
data1 = ('col1,col2,col3,col4\n'
          '1,2,3,4\n'
          '2,9,7')
new = pd.read_csv(StringIO(data1),dtype={'col1':int,'col2':float})
print(new.info())
data = ('index,a,b,c\n'
           '4,apple,bat,5.7\n'
            '8,orange,cow,10')
new= pd.read_csv(StringIO(data),index_col=0)
new1= pd.read_csv(StringIO(data),usecols=['a','b','c'],index_col=0)
print(new1)
new2 = pd.read_csv('https://download.bls.gov/pub/time.series/cu/cu.item',sep='\t')   
print(new2)