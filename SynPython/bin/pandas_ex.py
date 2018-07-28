import pandas as pd
df=pd.DataFrame([[1,2,3], [4,5,6]])
print(df)
df2=pd.DataFrame([[7,8,9],[10,11,12]],index=['row1', 'row2'],columns=['C1', 'C2', 'C3'])
print(df2)

df3=pd.read_csv(r'C:\training\log\out6.csv')
print(df3)

df4=df3['PIC']
print(df4)
df4.to_csv('out11.csv', index=False)
df4.to_excel('out12.xlsx')

df5=df3[['DT', 'PIC']]
df6=df3['PIC'].value_counts()
print(df6)

import matplotlib.pyplot as plt
df6.plot()
#plt.show()..it will show on screen

plt.savefig('g1.pdf') #save as pdf file in your current working dir i.e. bin..if you want to save at different location , type the entire path.

df7=df3['ID'].describe()
print('df7=.............')
print(df7)
df8=df3['ID'].count()
print('df8=.............')
print(df8)
df9=df3['ID'].min()
print('df9=..........')
print(df9)

df10=df3.head(2)
df11=df3.tail(2)
print('df10=.............')
print(df10)
print('df11=.............')
print(df11)

df12=df3[df3['PIC'].str.endswith('jpg')]
print('df12=.............')
print(df12)
df13=df3[df3['ID']<5]
print('df13=.............')
print(df13)

df14=df3.iloc[1]#row no 1 , iloc index location
print('df14=.............')
print(df14)

df15=df3.iloc[1:10]#1to10 rows
print('df15=............')
print(df15)
df16=df14.T#Transpose
print('df16=.............')
print(df16)
df17=df3.iloc[1:10, 2:4]#1 to 10-1 th row 2nd to 4-1 column
print('df17=.............')
print(df17)
df18=df3.iloc[[2,4,6],[1,3]]# 2nd row, 4th row, 6th row and 1st and 6th column
print('df18=.............')
print(df18)


