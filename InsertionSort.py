def InsertionSort(lst):
     for i in range(1, len(lst)):

        key = lst[i]

        # Move elements of lst greater than key, to one position ahead
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    
    

srtList =[9,2,4,0,1,5,7,8,3,6]
InsertionSort(srt
