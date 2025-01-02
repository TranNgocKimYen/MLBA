from numpy import nan as NA
import pandas as pd

data = pd.DataFrame([[1., 6.5, 3.],
                     [1., NA, NA],
                     [NA, NA, NA],
                     [NA, 6.5, 3.]])
print(data)
print("-"*10)
cleaned=data.fillna(data.mean())
print(cleaned)


#Điền giá trị NaN = 0
cleaned = data.fillna(0)
print(cleaned)

#Điền giá trị trung vị median vào NaN
cleaned = data.fillna(data.median())
print(cleaned)

#Điền giá trị mode va NaN
cleaned = data.fillna(data.mode().iloc[0])
print(cleaned)

#Điền giá trị interpolate
cleaned = data.interpolate()
print(cleaned)