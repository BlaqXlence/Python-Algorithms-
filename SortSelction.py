def SortSelection(srtList):
    for i in range(len(srtList)):
        min_idx = i
        for j in range(i+1,len(srtList)):
            if srtList[j] < srtList[min_idx]:
             min_idx = j
        srtList[i],srtList[min_idx] = srtList[min_idx],srtList[i]
    
    

srtList =[9,2,4,0,1,5,7,8,3,6]
SortSelection(srtList)
print(srtList)
