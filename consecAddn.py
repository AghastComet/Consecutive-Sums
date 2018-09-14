added=[0]
subed=[0]
def findTotal(added=added,subed=subed):
	total=0
	for i in added:
		total+=i
	for i in subed:
		total-=i
	return total

target=int(input())
total=0
while True:
	if total<target:
		added+=[added[-1]+1]
	else:
		subed+=[subed[-1]+1]
	total=findTotal()
	if total==target:
		for i in added:
			if not i in subed:
				print(i,end=' ')
		print()
	if added[-1]==target:
		break
