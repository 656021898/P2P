import pandas

df = pandas.read_excel("test_data/testCase.xlsx",sheet_name="testCaseRead")
data = df.head()#获取每行数据，默认前5行
print(df.index.values)#获取行号并打印输出
print(df.columns.values)#获取所有列名并打印输出
print(df.sample(3).values)#打印指定行数的值
print(df["id"].values)#打印指定列的值
data11 = df.loc[[0,1,2],].values#读取某一行的数据,注意2个中括号
data21 = df.loc[[0,1,2],["id","module"]].values#读取某几行ID和module这2列的数据
data31 = df.loc[:,["id","module"]].values#读取所有行的id、module列的数据
data41 = df.loc[:,:]#读取所有行所有列的数据
print(data11)
print(data21)
print(data31)
print(data41)
