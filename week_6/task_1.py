def fib(n):
	'''
	Returns the nth element in the fibonacci sequence.
	Implemented in recursive form.
	'''
	if n <= 1:
		return n
	return fib(n - 1) + fib(n - 2)

def fib_mem(n, computed = {0: 0, 1: 1}):
	'''
	Returns the nth element in the fibonacci sequence.
	Implemented in memoization recursive form for increased efficiancy.
	'''
	if n not in computed:
		computed[n] = fib_mem(n - 1, computed) + fib_mem(n - 2, computed)
	return computed[n]

print("Simple recursive implementation:")
for n in range(20):
	print(f"fib[{n}]: {fib(n)}")

print("\nMemoization implementation:")
for n in range(2000):
	print(f"fib[{n}]: {fib_mem(n)}")