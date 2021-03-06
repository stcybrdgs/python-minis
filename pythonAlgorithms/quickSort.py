# quickSort.py
'''
- quick sort is a 'divide and conquer' algorithm-- ie, it breaks data down into
  smaller parts that are easier to work with.
- it uses recursion to perform sorting
- generally performs better than merge sort O(n log n)
- performs data sorting in place and doesn't need extra memory to do its work
- worst case scenario occurs on a fully sorted or mostly sorted list, in which case
  the performance can occasionally degrade to quadratic time complexity O(n^2)
- to do quicksort, your algorithm needs to start by finding the pivot point and
  then partition the list
'''
# globals =============================
items = [20, 6, 8, 53, 56, 505, 23, 87, 41, 49, 19]

# functions ===========================
def quickSort(dataSet, first, last):
	if first < last:
		# find the split point
		pivotIndex = partition(dataSet, first, last)
		
		# sort the two partitions
		quickSort(dataSet, first, pivotIndex - 1)
		quickSort(dataSet, pivotIndex + 1, last)
	
def partition(dataValues, first, last):
	# choose the first item as the pivot value
	pivotValue = dataValues[first]
	
	# establish the upper and lower indices
	lower = first + 1
	upper = last
	
	# search for the split point
	done = False
	
	while not done:
		# advance lower index
		while lower <= upper and dataValues[lower] <= pivotValue:
			lower += 1

		# advance upper index
		while upper >= lower and dataValues[upper] > pivotValue:
			upper -= 1

		# if indices cross, we have found the split point
		if upper < lower:
			done = True # invoke breaking condition for the while loop
		# else swap upper and lower indices
		else:
			temp = dataValues[lower]
			dataValues[lower] = dataValues[upper]
			dataValues[upper] = temp
		
	# once the split point is found, swap the pivot value into the array
	temp = dataValues[first]
	dataValues[first] = dataValues[upper]
	dataValues[upper] = temp
	
	# return the split point index
	return upper
		
# main ================================
def main():
	global items
	
	# show starting array
	print(items)
	
	# run the quick sort
	quickSort(items, 0, len(items)-1)
	
	# show ending array
	print(items)

	# end
	print('Done.')

if __name__ == '__main__' : main()	