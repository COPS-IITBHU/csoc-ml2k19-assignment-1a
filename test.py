import pickle
import numpy as np

with open('C:/Users/amang/Downloads/array.pickle', 'rb') as p:
    arr = pickle.load(p)

#Task1
## begin code
print(np.size(arr))
## end code

#Task2
## begin code
arr=np.reshape(arr, (20,50))
##end code

#Task3
## begin code
arr_T=arr.T
print(arr_T)
##end code

#Task4
## begin code
m_arr=np.matrix(arr)
m_arr_T=np.matrix(arr_T)

multy=m_arr*m_arr_T
## end code

#Task5
## begin code
print(m_arr.sum(axis=1))
## end code

#Task6
## begin code
print(np.cbrt(multy))
## end code

#Task7
## begin code
print(np.sin(multy))
print(np.cos(multy))
print(np.arctan(multy))
## end code

def normalizeRows(x):
    # begin code
    v=np.linalg.norm(x, ord=2, axis=1, keepdims=True)
    return x/v

x = np.array([
    [0, 5, 7],
    [7, 3, 4]])
print("normalizeRows(x) = " + str(normalizeRows(x)))

VARIABLE_NAME=np.arctan(multy)
with open('submission.pickle', 'wb') as p:
    pickle.dump(VARIABLE_NAME, p)


    
    
    
    
    
    
    
    
    
    