def countingIncreases(arr):
    count=0
    for i in range (len(arr)):
        if arr[i] > arr[i-1]:
            count+=1
    print ("Number of increases: \t" + str(count))

arr=[199, 200, 208, 210, 200, 207, 240, 269, 260, 263];

print ("Array:\t " + str(arr))
countingIncreases(arr)