fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    if line == '': continue
    words=line.split()
    #print words
    for word in words:
        if word not in lst:
        	lst.append(str(word))
    
lst.sort()
print lst
#print line.rstrip()
