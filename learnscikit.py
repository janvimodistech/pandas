import sklearn
# from sklearn.datasets import load_iris
# print(load_iris(return_X_y=True))
# x,y = load_iris(return_X_y=True)
# from sklearn.linear_model import LinearRegression
#data cleanng
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_openml

# Fetch Titanic dataset
df = fetch_openml('titanic', version=1, as_frame=True)['data']

# Calculate the percentage of missing values
mis_val_percent = pd.DataFrame((df.isnull().sum()) / len(df) * 100)

# Set the index to column names for better plotting
mis_val_percent.set_index(mis_val_percent.index, inplace=True)

# Plotting using Seaborn for better styling
plt.figure(figsize=(10, 6))
sns.barplot(x=mis_val_percent.index, y=mis_val_percent[0])
plt.title('Percentage of Missing Values')
plt.ylabel('Percentage')
plt.xlabel('Columns')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better visibility
# plt.show()
print('size of dataset ',(df.shape))
a= df.drop(['body'],axis = 1, inplace =True)
print('size of dataset ',(df.shape))
#value imputaliton 
from sklearn.impute import SimpleImputer
 
# b = df.age.isnull().sum()
# print(b)
imp = SimpleImputer(strategy='mean')
df['age'] = imp.fit_transform(df[['age']])
b = df.age.isnull().sum()
print(b)
# plt.show()
def get_parameters(df):
    parameters = {}
    for col in df.columns[df.isnull().any()]:
        if df[col].dtype == 'float64' or df[col].dtype=='int64' or df[col].dtype=='int32':
            strategy = 'mean'
        else :
            strategy = 'most_frequent'    
        missing_values = df[col][df[col].isnull()].values[0]
        parameters[col]={'missing_values': missing_values, 'strategy' : strategy} 
    return parameters
parameters = get_parameters(df)
print(parameters)
for col, param in parameters.items():
 missing_values = param['missing_values']
 strategy = param['strategy']
 imp = SimpleImputer(missing_values=missing_values,strategy=strategy)
 df[col]=imp.fit_transform(df[[col]])
no_null_left = df.isnull().sum() 
print(no_null_left)