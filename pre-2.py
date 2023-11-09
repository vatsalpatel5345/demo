import time
def pushZerosToEnd(arr, n):
	count = 0 
	for i in range(n):
		if arr[i] != 0:
			
			arr[count] = arr[i]
			count+=1
	while count < n:
		arr[count] = 0
		count += 1
		
arr = [0,1,2,0,4,0,0,0,0,0,0,0,6,4,12,0,5,0,5]
n = len(arr)
start = time.time()
pushZerosToEnd(arr, n)
end = time.time()
execution_time = (end-start) * 10**3
print("Array after pushing all zeros to end of array:")
print(arr)
print(execution_time + "ms")
