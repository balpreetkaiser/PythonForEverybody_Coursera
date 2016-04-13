inp_score = raw_input("Enter the score between 0.0 and 1.0:")
score = float(inp_score)

if (score < 0) or (score >1):
    print "Score out of range"
    exit()
elif score >= 0.9:
    print "A"
elif score >=0.8:
    print "B"
elif score >= 7:
    print "C"
elif score >=0.6:
    print "D"
else:
    print "F"
