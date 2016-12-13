def decrypt(e,offset):
    #alphabet
    a='abcdefghijklmnopqrstuvwxyz'
    #offset by thirteen, added a space to the end to convert spaces too
    c=a[offset:]+a[:offset]
    d = ""

    #for each character in e
    for i in e:
        #get the character in 'e' in the same position it is in 'a'
        #i.e. if we are in the 4th position in a, return the 4th pos in 'e'
        if i not in a:
            d+=i
        else:
            d+=c[a.index(i)]
    return d


e= "lbh zhfg hayrnea jung lbh unir yrnearq.(*&(*&(*&)))!!!!!!   |"
for offset in range(26):
    print decrypt(e,offset)
