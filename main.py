import time

def collatzBasic(n):
	if n % 2 == 0: #even
		return n // 2
	elif n % 2 == 1: #odd
		return n * 3 + 1
	
def collatzDerived(n):
	if (n + 0) % 2 == 0: #even
		return n // 2
	a = calculateStepCount(n)
	# notes on this algorithm:
		# (n + 1 + 2^a) % 2^(a+1) == 0
			# a=1: is n + 3 divisible by 4?
			# a=2: is n + 5 divisible by 8?
			# a=3: is n + 9 divisible by 16?
			# ...
			# when the answer is yes:
			# 	will take a steps to get to an even number e:
			#		e = (3^a * (n + 1) - 2^a) / 2^a
			# 		  = (3/2)^a * n + (3/2)^a - 1
			#		  = (3/2)^a * (n + 1) - 1
			#		  = (3^a / 2^a) * (n + 1) - 1
		# ( n mod 2^(a+1) + 1 mod 2^(a+1) + 2^a mod 2^(a+1) ) mod 2^(a+1) == 0
		# ( n mod 2^(a+1) + 1 + 2^a ) mod 2^(a+1) == 0
	n = (3/2)**a * (n + 1) - 1
	if n % 1 != 0: # ensure the division-generated float is still really an int
		raise ValueError('expected whole number but got: ', n)
	return int(n)
	
def calculateStepCount(n):
	a = 1
	addend = 3
	while (n + addend) % 2**(a + 1) != 0:
		addend = 2**(a + 1) + 1
		a += 1
	return a
	
def runCollatzSequence(nFirst, nLast, method):
	start = time.time()
	for a in range(nFirst, nLast):
		n = a
		steps = 0
		print(str(a) + ": " + str(n), end="")
		while n != 1:
			n = method(n)
			steps += 1
			# print(" > " + str(n), end="")
		print(" (" + str(steps) + " steps)")
	end = time.time()
	print('%.3g' % (end - start) + "s execution time")


print("collatz step performance, original vs. Chris's method...")
print()

# temporary: individual user input
	# try:
		# input = int(input("Starting int: "))
	# except ValueError:
		# print("! Invalid int")
	# n = input
		
	# print()
	# print("naive way:")
	# print(n)
	# while n != 1:
		# n = collatzBasic(n)
		# print(n)
		
	# n = input
	# print()
	# print("derived way:")
	# print(n)
	# while n != 1:
		# n = collatzDerived(n)
		# print(n)
	
print()
print("n=1->30, naive way:")
print("(validate with https://oeis.org/A006577/list)")
runCollatzSequence(1, 30, collatzBasic)

print()
print("n=1->30, derived way:")
runCollatzSequence(1, 30, collatzDerived)

print()
print("[next steps: optimize calculateStepCount() and test for n <= 1000]")
print()
