l = input("enter the array : ") #enter the inputs with space
k = int(input("enter the number : "))
arr = list(map(int, l.split(' ')))
arr.sort()
c = 0
i = 0
for a in set(arr):
	i = i+1
	if k == a:
		print("index =" ,arr.index(a))
		c = 1
		break
	elif k < a:
		print("index =", arr.index(a))
		c = 1
		break
if c == 0:
	print ("index =",i)
