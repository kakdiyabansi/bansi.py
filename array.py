"""#ien()-number of elements
from array import array
arr=array('i',[10,20,30,40,50])
print(len(arr))"""

"""#append[x]-add element at end
from array import array
arr=array('i',[10,20,30])
print(arr)"""

"""#insert
from array import array
arr=array('i',[10,20,40])
arr.insert(2,30)
print(arr)"""

"""#remove
from array import array
arr=array('i',[10,20,30,20,40])
arr.remove(20)
print(arr)"""

"""#pop
from array import array
arr=array('i',[10,20,30,40])
x=arr.pop()
print("remove:",x)
print(arr)"""

"""#index
from array import array
arr=array('i',[10,20,30,40])
print(arr.index(30))"""

"""#count
from array import array
arr=array('i',[10,20,30,20,40])
print(arr.count(20))"""

#revese
from array import array
arr=array('i',[10,20,30,40])
arr.reverse()
print(arr)