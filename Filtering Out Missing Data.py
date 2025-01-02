from numpy import nan as NA
import pandas as pd

data = pd.DataFrame([[1., 6.5, 3.],
                     [1., NA, NA],
                     [NA, NA, NA],
                     [NA, 6.5, 3.]])
print(data)
print("-"*10)
#Xóa tất cả các dòng có NA
cleaned = data.dropna()
print(cleaned)
print("-"*10)
#Chỉ xoa cac dong có tat ca NA
cleaned2=data.dropna(how='all')
print(cleaned2)
print("-"*10)
#Xóa các cột có giá trị NA
cleaned3 = data.dropna(axis=1)
print(cleaned3)
print("-"*10)
#Xóa các cột có tất cả giá trị là NA (hong có cột nào NA hết nen nhu cu)
cleaned4 = data.dropna(how='all', axis=1)
print(cleaned4)
print("-"*10)
#Giữ lại các hàng có ít nhất 2 giá trị không NaN.
cleaned5 = data.dropna(thresh=2)
print(cleaned5)






