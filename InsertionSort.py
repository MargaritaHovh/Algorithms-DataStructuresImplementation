def insertion_sort(lst):
    for j in range(1, len(lst)):
        key = lst[j]    #hamematelu hamar enq pahum u henc es enq texadrum
        i = j - 1 
        while i >= 0 and lst[i] > key:       
            lst[i+1] = lst[i]
            i = i - 1
        lst[i+1]= key                                                       
    
lst = [5,2,4,6,1,3] 
insertion_sort(lst)
print(lst)

