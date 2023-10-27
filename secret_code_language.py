# Coding

# if the word contain atleast 3 characters,remove the first letter and append it at the end

st="Harry is good"
Coding=True
if(Coding):
    if(len(st)>=3):
        st=st[1:] + st[0]
        print(st)
           
else:
    pass

# now append 3 random characters at the starting and at the end

st=input("Enter message")
Coding=True
if(Coding):
    if(len(st)>=3):
        r1 = "kcs"
        r2 = "adj"
        st=r1 + st[1:] + st[0] + r2
        print(st)
           
else:
    pass


st=input("Enter message")
words=st.split(" ")
Coding=True
if(Coding):
    nwords=[]
    for word in words:
        if(len(st)>=3):
           r1 = "kcs"
           r2 = "adj"
           stnew=r1 + word[1:] + word[0] + r2
           nwords.append(stnew)
        else:
             nwords.append(word[::-1])
    print(" ".join(nwords)) 
else:
    pass


# Decoding

st=input("Enter message")
words=st.split(" ")
Coding=input("1 for Coding or 0 for Decoding")
Coding=True if (Coding=="1") else (False)
if(Coding):
    nwords=[]
    for word in words:
        if(len(st)>=3):
           r1 = "kcs"
           r2 = "adj"
           stnew=r1 + word[1:] + word[0] + r2
           nwords.append(stnew)
        else:
             nwords.append(word[::-1])
    print(" ".join(nwords)) 
else:
     nwords=[]
     for word in words:
        if(len(st)>=3):
           stnew=word[3:-3]
           stnew=stnew[-1] + stnew[:-1]
           nwords.append(stnew)
        else:
             nwords.append(word[::-1])
     print(" ".join(nwords))