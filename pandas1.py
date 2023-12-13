import numpy as np 
# list =[1,2,34,4]
# hi = np.array(list)
# print(hi )
# print(type(hi)) 

#shape 
list1 =[1,2,3,4,5,6,7]
list2 =[2,3,4,1,6,7,8]
list3 =[9,8,7,6,5,3,7]
array = np.array([list1,list2,list3]) #2d arry
print(type(array))
#indexing in pandas
# print(array[2])

# #slicing 
# print(array[:2])

# print(array.shape) #gives number o rows and number of coloums
# change values
print(array[:,3]) #it will only show the 3rd column as output
print(array[:,[0,-1]])
print(array.reshape(7,3))
new = np.arange(1,20).reshpe()
print(new)
np.zeros((4,3))