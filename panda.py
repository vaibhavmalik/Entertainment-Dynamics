

num = int(input())		# Number of elemnts in an array

arr = []				# Array of numbers
te = input()
te = te.split()

for i in range(num):
	arr.append(int(te[i]))

freq = [0 for i in range (128)]		# Contains the number of times a particular Xor value comes (index represent the Xor value)

for i in range (num):
	temp = [0 for k in range (128)]

	for j in range (128):
		if j == arr[i]:
			temp[j] = 1
		elif freq[j] != 0:
			temp [j^arr[i]] += freq[j]
	for j in range (128):
		freq[j] += temp[j]

ans = 0

for i in range(128):
	if freq[i]>1:
		ans += (freq[i]%(10^9+7)) * ((freq[i]-1)%(10^9+7)) * (2^{-1)%(10^9+7))

ans = ans % 1000000007
print (int(ans))
