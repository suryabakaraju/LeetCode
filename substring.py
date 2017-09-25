class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)== 0:
            length = 0
        elif len(s)==1 or s == len(s)*s[0]:
            length = 1
        
        elif [s.count(c) for c in s] == [1]*len(s):
            length = len(s)


        else:
            i = s[0];
            length = len(i);
            for j in range(1,len(s)):
                if s[j] not in i:
                    i = i+s[j]
                    if len(i)>length:
                        length = len(i)
                else:
                    try:
                        i = i[((i.index(s[j]))+1):]+s[j]
                        if len(i) > length:
                            length = len(i)
                    except IndexError:
                        i = s[j]
            
        return length
        