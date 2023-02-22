def insertion_sort(arr):
    count=0
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
            count+=1
        arr[j+1]=key
        count+=1
    return count

arr=[1,2,3,4,5,6,7]
count=insertion_sort(arr)
print("Sorted array is",arr)
print("number is",count)