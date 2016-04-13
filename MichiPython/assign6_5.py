text = "X-DSPAM-Confidence:     0.8475"
pos = text.find(':')
#print pos
interm_res = text[pos+1:]
res = float(interm_res)
print res
