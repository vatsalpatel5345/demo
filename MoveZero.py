arr = [0,1,2,0,4,0,0,0,0,0,0,0,6,4,12,0,5,0,5]

arr.sort()
count = arr.count(0)
for i in range(count):
	arr.remove(arr[i])
print(arr, count)
