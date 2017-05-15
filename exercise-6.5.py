text = "X-DSPAM-Confidence:    0.8475";
colon_pos=text.find(':')
s_len=len(text)
#print colon_pos, s_len
num_s=text[colon_pos+1:s_len]
num_ss=num_s.strip()
#print num_s, num_ss
num_f =float(num_ss)
print num_f