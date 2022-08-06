def mergeSort(arr) :
	if len(arr)>1 :
		mid = len(arr)//2
		left = arr[:mid]
		right = arr[mid:]

		mergeSort(left)
		mergeSort(right)

		lptr, rptr, aptr = 0, 0, 0
		while lptr<len(left) and rptr<len(right) :
			if left[lptr] < right[rptr] :
				arr[aptr] = left[lptr]
				lptr += 1

			else :
				arr[aptr] = right[rptr]
				rptr += 1

			aptr += 1

		while lptr<len(left) :
			arr[aptr] = left[lptr]
			aptr += 1
			lptr += 1

		while rptr<len(right) :
			arr[aptr] = right[rptr]
			aptr += 1
			rptr += 1


arr = [1,5,2,6,4,3,11,2,10]
mergeSort(arr)
print(arr)
