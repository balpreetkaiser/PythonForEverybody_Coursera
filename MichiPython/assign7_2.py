# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
count = 0
res = 0.0
sum_total = 0.0
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count + 1
    pos = line.find(':')
    mini_str = line[pos+1:]
    imm_num = float(mini_str)
    sum_total = sum_total+imm_num
res = sum_total/count
print "Average spam confidence:", res

