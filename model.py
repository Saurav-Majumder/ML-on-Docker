import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

ds = pd.read_csv('SalaryData.csv')

ds.columns
ds.info()

x = ds['YearsExperience'].values.reshape(30,1)
y = ds['Salary']



model = LinearRegression()

# algo 
model.fit(x , y)

model.coef_

model.predict([[ 1.1 ]] )
model.intercept_

input=int(input("Enter the years of experience: "))
output=model.predict([[user_input]])
print(f"The salary for {input} years of experience will be {output} ")




