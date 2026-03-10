"""#basic
from array import array
arr=array('i',[10,20,30,40,50])
print(arr[1:4])#index 1 to 3
print(arr[:3])#start to index 2
print(arr[2:])#index 2 to end
print(arr[:])#entire array"""

"""#slicing
from array import array
arr=array('i',[10,20,30,40,50,60,70,80])
print(arr[::2])#every second element
print(arr[1::2])#every second element staring from index 1
print(arr[::3])#every thrid element"""

"""#negative
from array import array
arr=array('i',[10,20,30,40,50])
print(arr[-4: -1])
print(arr[-3:])
print(arr[: -2])"""

#reverse
from array import array
arr=array('i',[10,20,30,40,50])
print(arr[:: -1])
