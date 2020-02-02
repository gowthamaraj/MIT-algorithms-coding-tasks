# div and conq approach
from datetime import datetime
import listmaker
#function: peak finder
def peak_finder(data_item,l,r):
    #check for the corner cases
    len_ = len(data_item)
        #element of size 1
    if len_ == 1:
        return data_item[0]
        #start
    elif data_item[0]>=data_item[1]:
        return data_item[0]
        #end
    elif data_item[len_-1]>=data_item[len_-2]:
        return data_item[len_-1]
    return recurser(data_item,l+1,r-1)
    
    
def recurser(data_item,l,r):
    #base case - check if current >= prev and current >= next
    mid = (l+r)//2
    current = data_item[mid]
    prev = data_item[mid-1]
    next = data_item[mid+1]
    
    # else,
        # if next >=current, go right
        # else,right
    if current >= prev and current >= next:
        return current
    elif current <= prev:
        return recurser(data_item,l,mid-1)
    else:
        return recurser(data_item,mid+1,r)


data_list = listmaker.list_gen(50)
print(data_list)
start_time = datetime.now()
print(peak_finder(data_list,0,len(data_list)-1))
end_time = datetime.now()
print((end_time-start_time).microseconds)
