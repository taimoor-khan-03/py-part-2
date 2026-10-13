import numpy as np;
import pandas as pd;

data = {
    'name' : ['Alice', 'Bob', 'Charlie', 'David', 'Eva' ],
    'age' : [25, 30, 35, 40, 45],   
    'city' : ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
}

# df = pd.DataFrame(data);
df2 = pd.to_csv('C:/Users/helloWorld/OneDrive/Desktop/marks.csv',index=False);

# print(df2.size, '\n' , df2.dtypes , '\n' , df2.shape , '\n' , df2.ndim , '\n' , df2.columns , '\n' , df2.index);
# print(df2.iloc[1:4 , 1]);        
print(df2.loc[1:4 , df2.columns[0:1]]);        
df2['math'] = [95, 88, 92, 85, 90, 87];
df2['science'] = [90, 85, 88, 92, 95, 89];
df2['total'] = df2['math'] + df2['science'];
print(df2);


# # print(df);
# print(df.iloc[1:4][['name','age']]);
# print("="*50);
# print(df.loc[1:4, ['name','age']]);


# marks =  np.array([[85, 90, 78], [92, 88, 95], [75, 80, 70], [88, 92, 85], [90, 85, 88]]);

# print(marks.shape)
# print(marks.size)
# print(marks.dtype)
# print(marks[2][2])

# Python list - requires a loop or comprehension
# prices_list = [120, 250, 80, 340, 190]
# discounted_list = [p * 0.9 for p in prices_list]
# print("List:", discounted_list)

# # NumPy array - vectorised operation
# prices = np.array([120, 250, 80, 340, 190])
# discounted = prices * 0.9
# print("Array:", discounted)

#  2x(2,3)
# a =  np.array([[
#     [
#         [1,2,4]
#     ]
#     ,
#     [
#         [2,3,4]
#     ],

#     [
#         [1,2,4]
#     ]
#     ]
# ])

# print(a)
# print(a.shape,'\n',a.ndim,'\n',a.size, '\n', a.dtype);
# print(a[0,1,0,1:2]);



# x =  np.array([[1,2], 
#                [3,4]]);

# y = np.array([[11,12],
#               [13,14]]);

# print(x + y)
# print(x - y)
# print(x * y);
# print(x @ y)
# print(x / y)
# print(x // y)
# print(x % y)
# print(x ** y)
# print(y.transpose())
