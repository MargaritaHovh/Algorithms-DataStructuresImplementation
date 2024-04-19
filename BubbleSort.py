def bubble_sort(lst):
    for i in range (len(lst) - 1):    #range(len(lst)) also work but outer loop will repeat one time more than needed.
        for j in range(len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

lst = [4,3,2,1]
bubble_sort(lst)
print(lst)