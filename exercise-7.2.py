# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
lcount=0
flcount=0
conf_total=0.0
avg_conf=0.0
for line in fh:
    lcount=lcount+1
    if not line.startswith("X-DSPAM-Confidence:") : continue
    flcount = flcount + 1
    colon_pos=line.find(':')
    s_len=len(line)
	#print colon_pos, s_le
    num_s=line[colon_pos+1:s_len]
    num_ss=num_s.strip()
    #print num_s, num_ss
    num_f =float(num_ss)
    conf_total=conf_total+num_f
    #print line
    
avg_conf=conf_total/flcount
print "Average spam confidence:",avg_conf
#print "Done"
