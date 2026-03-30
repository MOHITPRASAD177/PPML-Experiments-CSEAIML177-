# #create a numpy array with elements [10,20,30,40]
# import numpy as np
# arr = np.array([10,20,30,40])
# print(arr)


# #create a 2d array and display its shape and dimensions
# arr_2D = np.array([[1,2,3] , [4,5,6]])
# print("Shape of the array:", arr_2D.shape)
# print("Dimensions of the array:", arr_2D.ndim)


# #create array using zeroes ones and empty
# zero_arr = np.zeros((2,3))
# print("Array of zeroes:", zero_arr)
# ones_arr = np.ones((3,4))
# print("Array of ones:", ones_arr)
# empty_arr = np.empty((2,2))
# print("Array of empty values:", empty_arr)


# #convert 1d array into 2d array
# one_d_arr = np.array([1,2,3,4,5,6])
# two_d_arr = one_d_arr.reshape(2,3)  
# print("1D array:", one_d_arr)
# print("2D array:", two_d_arr)


# #access specific elements and slices in an array
# arr = np.array([10,20,30,40,50])
# print("element at index 2 :",arr[2])
# print("slice from index 1 to 3:", arr[1:4])


# #perform addition, subtraction, multiplication on arrays
# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])
# print("Addition:", arr1 + arr2)
# print("Subtraction:", arr1 - arr2)
# print("Multiplication:", arr1 * arr2)



# #find mean, median and standard deviation
# data = np.array([10, 20, 30, 40, 50])
# mean = np.mean(data)
# median = np.median(data)
# std_dev = np.std(data)
# print("Mean:", mean)
# print("Median:", median)
# print("Standard Deviation:", std_dev)


# #sort elements in ascendind and descendind order
# arr = np.array([10,20,30,45,23,15])
# sorted_arr_asc = np.sort(arr)
# sorted_arr_desc = np.sort(arr)[::-1]
# print("in ascendind order:",sorted_arr_asc)
# print("sorted in descendind:",sorted_arr_desc)



# #perform matrix multiplication.(dot() or @)
# matrix1 = np.array([[1,2],[3,4]])
# matrix2 = np.array([[5,6],[7,8]])
# re_dot = np.dot(matrix1, matrix2)
# re_at = matrix1 @ matrix2
# print("using dot",re_dot)
# print("using @:",re_at)



# #find transpose of a matrix
# matrix = np.array([[1,2],[3,4]])
# transpose_matrix = matrix.T
# print("Original Matrix:", matrix)
# print("Transpose Matrix:", transpose_matrix)


# #find maximum and minimum values
# arr = np.array([10,20,30,80,5])
# print("Maximum value:", np.max(arr))
# print("Minimum value:", np.min(arr))


# #extract elements greater than 10
# arr = np.array([5, 10, 15, 20, 25])
# greater_10 = arr[arr > 10]
# print("Element greater than 10:", greater_10)


# #generate random numbers
# random = np.random.rand(100)
# print("random numbers",random)



# #save and load numpy array
# arr = np.array([1, 2, 3, 4])
# np.save('my_array', arr) # Save array
# loaded_arr = np.load('my_array.npy')
# print("Loaded array:", loaded_arr)


#panda
#create a panda series
import pandas as pd
data = [10,20,30]
labels = ['a','b','c']
series = pd.Series(data, index=labels)
print("Pandas Series:")
print(series)


#create dataframe from dictionary
dict = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
df = pd.DataFrame(dict)
print(df)


#load csv and show info
df = pd.read_csv('C:\\Users\\mohit_a2o9gf3\\Downloads\\city_day.csv.zip')
print(df.info())
#select rows and columns
print(df.loc[0])
print(df.iloc[0:2, 0:2])
#add new column