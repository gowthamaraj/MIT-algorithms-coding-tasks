# naive approach
from datetime import datetime

#function: peak finder
def peak_finder(data_item):
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
    #loop
    for i in range(1,len_-1):
        current = data_item[i]
        pre = data_item[i-1]
        next = data_item[i+1]
        if current>=pre and current>=next:
            return current
        #if current >= pre and current >= next, return current


data_list = [24, 97, 37, 7, 26, 43, 59, 61, 85, 17, 49, 59, 11, 42, 91, 3, 47, 30, 61, 69, 70, 64, 7, 90, 77, 95, 72, 9, 40, 35, 95, 64, 50, 92, 98, 89, 38, 20, 72, 1, 6, 23, 92, 56, 19, 16, 90, 83, 37, 15]
start_time = datetime.now()
print(peak_finder(data_list))
end_time = datetime.now()
print((end_time-start_time).microseconds)
