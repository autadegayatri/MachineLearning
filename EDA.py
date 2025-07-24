import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')
data=pd.read_csv("used_cars_data.csv")
print(data.head())
print(data.tail())
print(data.info())
print(data.isnull().sum())
print((data.isnull().sum()/len(data))*100)
print(data.ununique())
data=data.drop(['S.No.'],axis=1)
from datetime import date

data['Car_Age']=date.today().year - data['Year']
print(data.head())
data.info()
data['Brand']=data.Name.str.split().str.get(0)
data['Model']=data.Name.str.split().str.get(1)+data.Name.str.split().str.get(2)
print(data[['Name','Brand','Model']].head())
print(data.head())
data['repassing']=np.where(data['Car_Age']>=15,'true','false')
data['repassing']=np.where(data['Car_Age']>15)
print(data.head())
print(data.Brand.unique())
print(data.Brand.nunique())
searchfor=['Isuzu' ,'ISUZU','Mini','Land']
data[data.Brand.str.contains('|'.join(searchfor))].head(5)
data["Brand"].replace({"ISUZU": "Isuzu", "Mini": "Mini Cooper","Land":"Land Rover"}, inplace=True)
print(data.head())
print(data.Brand.unique())
print(data.describe(include='all'))
print(data.head())
cat_col=data.select_dtypes(include=['object']).columns
num_col=data.select_dtypes(include=['number']).columns.tolist()
print("Categorical Columns:",cat_col)
print("Numerical Columns:",num_col)

# bar chart
categories=['Diesel','Petrol','CNG']
values=[30,45,67]
plt.bar(categories,values)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Categorical Values')
plt.show()

# pie chart
categories=['Diesel','Petrol','CNG']
colors=['red','blue','green']
values=[30,45,67]
plt.pie(values,labels=categories,colors=colors)
plt.show()

categories=data['Fuel_Type']
values=data['Fuel_Type'].value_counts()
values.plot(kind='bar')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Categorical Values')
plt.show()

values=data['Fuel_Type'].value_counts()
values.plot(kind='pie')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Categorical Values')
plt.show()

# histogram

Car_Age = data['Car_Age']
plt.hist(Car_Age, bins=20, color='cornflowerblue', edgecolor='black')
plt.xlabel('car age Ranges')
plt.ylabel('car age')
plt.title('Histogram')
plt.grid(True)

plt.show()

plt.hist(data['Price'], bins=20, color='skyblue', edgecolor='black')
plt.xlabel('Price')
plt.ylabel('Number of Cars')
plt.title('Distribution of Car Prices')
plt.grid(True)
plt.show()


# Histogram=categorical and numerical
for fuel in data['Fuel_Type'].unique():
    subset=data[data['Fuel_Type']==fuel]
    plt.hist(subset['Price'], bins=20,label=fuel)
plt.xlabel('Fuel Type')
plt.ylabel('price')
plt.title('histogram')
plt.legend()
plt.show()

#Scatter Plot=numerical and numerical
carAge=data['Car_Age']
carPrice=data['Price']
plt.scatter(carAge, carPrice,color='purple')
plt.xlabel('Car Age')
plt.ylabel('Car Price')
plt.title('Scatter Plot')
plt.show()

fuel=data['Fuel_Type']
price=data['Price']
plt.bar(fuel, price)
plt.xlabel('Fuel Type')
plt.ylabel('Price')
plt.title('Bar Chart for Fuel Type vs Price')
plt.show()



















