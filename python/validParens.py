def checkPair(s,pair="()"):
    unclosedPair = 0
    for c in s:
        #counting the opens
        if c==pair[0]:
            unclosedPair+=1
        #close an unclosedPair
        if c==pair[1]:
            unclosedPair-=1
        if unclosedPair<0:
            #started with a closing char, exit
            return False
    print "I have %d unclosedPairs" % unclosedPair
    return unclosedPair==0

def checkPairs(s):
    return checkPair(s) and checkPair(s,"{}") and checkPair(s,"[]")
