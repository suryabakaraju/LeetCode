class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        if x==0 and y==0 or x==y:
            return 0;
        r1,r2,di = [],[],[];
        if x >1:
            while x >1:
                r1.append(x%2)
                x = int(x/2)
            r1.append(1)
            print(r1)
        elif x==1:
            r1=[1]
        if y >1:
            while y >1:
                r2.append(y%2)
                y = int(y/2)
            r2.append(1)
            print(r2)
        elif y==1:
            r2=[1]
        diff = abs(len(r1)-len(r2))
        if len(r1)>len(r2):
            r2.extend(diff*[0])
            r2.reverse()
            r1.reverse()
            for i,j in zip(r1,r2):
                di.append(abs(i-j))
        else:
            r1.extend(diff*[0])
            r1.reverse()
            r2.reverse()
            for i,j in zip(r1,r2):
                di.append(abs(i-j))
        return sum(di)
        