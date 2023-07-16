d = int(input("Total number of input: "))
D = []
for i in range(1, d + 1):
num = int(input("Enter number {}: ".format(i)))
D.append(num)
max_num = D[0]
loc = 1
for k in range(1, d):
if max_num < D[k]:
max_num = D[k]
loc = k + 1
print("Highest number is:", max_num)
print("Location of Highest Number:", loc)
