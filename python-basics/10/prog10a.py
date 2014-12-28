def intersection(list1,list2):
	return (list(set(list1)&set(list(list2))))

def union(list1,list2):
	return (list(set(list1)|set(list(list2))))

list1=[1,2,3,4,5,6,7,8,9]
list2=[2,4,6,8,0]

print(intersection(list1,list2))
print(union(list1,list2))
