def merge_sort(arr):
    if len(arr)>1:
        q = len(arr)//2
        l = arr[:q]
        r = arr[q:]
        merge_sort(l)
        merge_sort(r)
        i = j = k = 0
        while i<len(l) and j <len(r):
            if l[i]<r[j]:
                arr[k] = l[i]
                i+=1
            else:
                arr[k] = r[j]
                j+=1
            k+=1
        while i < len(l):
            arr[k] = l[i]
            i+=1
            k+=1
        while j < len(r):
            arr[k] = r[j]
            j+=1
            k+=1
            
arr = [5,2,4,7,1,3,2,6]
print(f"Original array is - {arr}")
merge_sort(arr)
print(f"Sorted  array is - {arr}")