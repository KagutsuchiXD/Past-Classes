from numpy.random import randint

def print_func(thing):
	if False:
		print(thing)

def selection(A, k):
	"""
	:param A Some Array
	:param k kth smallest element
	"""
	return sorted(A)[k]

def mult_selection(A, K):
	"""
	:param A An array of unsorted numbers
	:param K An array of sorted numbers to find in A.
	"""
	answers = []
	static_K = K
	for element in A:
		print_func("______________________________")
		print_func("Testing A: " + str(element))

		offset = 0
		found = False
		while not found:
			if len(K) == 0:
				print_func("__ Base Case: No more searching")
				break
			# Mid is the midpoint of K
			mid = len(K) // 2
			# Pivot is the point in A to move K
			pivot = selection(A, K[mid])
			# Split K into left and right (K_l and K_r respectively)
			K_l = K[:mid]
			K_r = K[mid+1:]
			print_func(str(K_l) + ' ' + str(K[mid]) + ' ' + str(K_r))
			print_func("Selection on Pivot = " + str(pivot) + " | Against = " + str(element))
			# Test condidtions
			if pivot == element:
				print_func("**** Found ****")
				answers.append(pivot)
				break
			elif element < pivot:
				print_func("Going Left")
				K = K_l
			else:
				print_func("Going Right")
				K = K_r
		K = static_K
	return answers

def test_selection():
	A = []
	K = []
	n = 1000
	m = n // 2
	while len(A) < n:
		num = randint(0, n * 10)
		if num not in A:
			A.append(num)
	while len(K) < m:
		num = randint(0, n)
		if num not in K:
			K.append(num)
	K = sorted(K)

	solution = [sorted(A)[k] for k in K]

	mine = mult_selection(A, K)

	if sorted(solution) != sorted(mine):
		print("Unsorted A:", A)
		print('Sorted A  :', sorted(A))
		print("K:", K)
		print("______________________________")
		print("$ My Solutions $:", mine)
		print("$    Actual    $:", solution)
		print("$    Valid?    $:", sorted(solution) == sorted(mine))
		print("______________________________")

