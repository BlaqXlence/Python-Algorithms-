def bubbleSort(lst):
     for i in range(len(lst)):
        for j in range(0, len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
               lst[j], lst[j + 1] = lst[j + 1], lst[j]
    
    

srtList =[9,2,4,0,1,5,7,8,3,6]
bubbleSort(srtList)
print(srtList)
