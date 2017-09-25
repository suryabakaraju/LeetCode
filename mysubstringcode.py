# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 19:34:07 2017

@author: surya
"""
s = 'nfpdmpi';
if len(s)==0:
    print(0)
elif len(s)==1 or s == len(s)*s[0]:
    print(1);
if [s.count(c) for c in s] == [1]*len(s):
    print(len(s))



i = s[0];
length = len(i)
for j in range(1,len(s)):
    if s[j] not in i:
        i = i+s[j]
        print(i)
        if len(i)>length:
            length = len(i)
    else:
        try:
            i = i[((i.index(s[j]))+1):]+s[j]
            print(i,j)
            if len(i) > length:
                length = len(i)
        except IndexError:
            i = s[j]
            
print(length)
    

#for c in s:
 #   vals.append(s.count(c))
#print(vals)
#keys = list(s)
#print(keys)
#print(dict(zip(keys,vals)))
