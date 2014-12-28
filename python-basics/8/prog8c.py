freq = {}
line = input("Enter a sentence :\n")
a=line.split()
for word in a:
    freq[word] = freq.get(word,0)+1
words=[]
words = freq.keys()
print(words)
list1=[]
for i in words:
	list1.append(i)
print (list1)
list1.sort()
for w in list1:
    print (w,':',freq[w])
