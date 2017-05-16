name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
tm_hist=dict()
count = 0
for line in handle:
    if line == '':continue
    if 'From ' in line:
        words=line.split()
        #print words
        tm=words[5][:2]
        #print tm
        tm_hist[tm]=tm_hist.get(tm,0)+1
        
        count = count +1
#print tm_hist
tm_list=list()
for h,c in tm_hist.items():
    tm_list.append((h,c))
tm_list.sort()
#print tm_list
for k,v in tm_list:
    print k,v
#print sorted( [ (v,k) for k,v in tm_hist.items() ] )

#print "There were", count, "lines in the file with From as the first word"
