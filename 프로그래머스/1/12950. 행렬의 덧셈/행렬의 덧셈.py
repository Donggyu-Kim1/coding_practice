def solution(arr1, arr2):
    arr3 = []
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            arr3.append(arr1[i][j]+arr2[i][j])
    
    arr4 = []
    for l in range(0,len(arr3),len(arr1[0])):
        arr4.append(arr3[l:l+len(arr1[0])])
        
    return arr4
                   