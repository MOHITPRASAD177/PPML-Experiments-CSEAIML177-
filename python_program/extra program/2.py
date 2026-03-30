#convert series from strings to numeric with error handling
import pandas as pd
#note: errors='coerce'
#this is the key concept


#2.convert mixed type series to datetime and filter invalid dates
import pandas as pd
s= pd.Series(['2023-01-01'])

#convert to datetime
dt_s = pd.to_datetime(s,errors='coerce')#invalid values = converted to NAT
#filter valid dates liks nan or nat
valid_dates = dt_s.dropna()
print(valid_dates)



#3.convert numeric strings with commas to floats
import pandas as pd
s=pd.Series(['1,000','2,500','3,750'])
#remove commas and convert to float
float_s = s.str.replace(',',"").astype(float)#after removing the commas converts strings to float type
print(float_s)

#note: .str.replace() -> used for string cleaning
#remove special characters before conversion


#4.convert series to categorical and display category codes
import pandas as pd
s =  pd.Series(['apple','banana','apple','orange'])
#convert to categorical
cat_s = s.astype('category')
#display category codes
print(cat_s.cat.codes)

s =  pd.Series(['apple','banana','apple','orange'])
p = pd.Series(['lion','cat','dog','tiger','monkey','dog','cat'])
#converts to categorical
cat_s = s.astype('category')
print(cat_s)
animal = p.astype('category')
print(animal)
#displaying category codes
print(cat_s.cat.codes)
print(animal.cat.codes)



#how are category codes assigned in pandas
'''when you convert a series to categorical, pandas does two things:
1.find unique values(categories)
2.sort the categories(default behaviour)
by default, pandas sort categories alphabetically
'''



#create dataframe and print it
import pandas as pd
df = pd.DataFrame({'X':[78,85,96,80,86],
'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]})
print(df)    



'''write a pandas program to create a DataFrame from a dictionary where values are lists of unequal lengths by filling missing values with none.'''
import pandas as pd
data = {
    'A' : [1,2,3],
    'B' : [4,5],
    'C' : [6,7,8,9]
}
df = pd.DataFrame(dict([(k,pd.Series(v)) for k, v in data.items()]))
df = df.where(pd.notnull(df), None)
print(df)


'''write a Pandas program to create a DataFrame from a dictionary
and then transpose it, ensuring that data types remain consistent.'''
import pandas as pd
# create dictionary
data = {
    'A': [1, 2, 3],
    'B': [4.0, 5.5, 6.1],
    'C': ['x', 'y', 'z']
}
# create DataFrame
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)
print("\nData Types:")
print(df.dtypes)

# transpose DataFrame
df_transposed = df.T

print("\nTransposed DataFrame:")
print(df_transposed)
print("\nData Types after Transpose:")
print(df_transposed.dtypes)


'''write a pandas program to split the following dataframe into groups based on school code. also check the type of GroupBy object.'''


pd.set_option('display.max_columns', None)
student_data = pd.DataFrame({
    'school_code':
['s001','s002','s003','s001','s002','s004'],
    'class':['V','V','VI','VI','V','VI'],
    'name': ['m','c','a','t','b','n'],
    'date_of_birth': ['15/01/2002','20/08/2000','11/01/2009','16/06/2002','23/09/2001','07/12/2004'],
    'age': [12,12,13,14,12,13],
    'height':[173,192,186,167,151,159],
    'weight': [35,32,33,30,31,32],
    'address': ['street1','street2','street3','stree4','street5','stree6']
}, index=['s1','s2','s3','s4','s5','s6'])
result = student_data.groupby('school_code')
print("Type of GroupBy object:", type(result))
result = student_data.groupby(['school_code'])    
for name,group in result:
    print("\ngroup:")
    print(name)
    print(group)
print("\ntype of the object:")
print(type(result))



'''write a pandas program to split a dataset to group by two columns and count by each row.'''

'''write a pandas program to merge two dataframes on a single column id.'''
#create two sample dataframes
df = pd.DataFrame({
    'ID' : [1,2,3],
    
})   