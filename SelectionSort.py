def selection_sort(lst):
    n = len(lst)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if lst[j] < lst[min_index]: #select the minimum element in each loop
                min_index = j
        
        lst[i], lst[min_index] = lst[min_index], lst[i]  

    
lst = [4, 3, 2, 1]
selection_sort(lst)
print(lst)




