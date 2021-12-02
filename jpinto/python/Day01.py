def countingIncreases(arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] > arr[i-1]:
            count += 1
    print("Number of increases: \t" + str(count))


def countingIcreasesSum(arr):
    temp1 = 0
    temp2 = 0
    count = 0
    for i in range(len(arr)-2):
        temp1 = arr[i-1] + arr[i] + arr[i+1]
        temp2 = arr[i] + arr[i+1] + arr[i+2]
        if temp1 < temp2:
            count += 1
    print("Number of three sum increases: \t" + str(count))


arr = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

# print ("Array:\t " + str(arr))
countingIncreases(arr)
countingIcreasesSum(arr)
