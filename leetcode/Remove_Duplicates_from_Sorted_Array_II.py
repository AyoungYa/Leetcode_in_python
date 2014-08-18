"""
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array A = [1,1,1,2,2,3],

Your function should return length = 5, and A is now [1,1,2,2,3].
"""
__author__ = 'Yang'



class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        length = len(A)
        if length <= 2:
           return length
        # elif length == 3:
        #     if A[0] == A[1] == A[2]:
        #         return 1
        else:
            i = 1
            j = length - 1

            while(i <= j):
                if A[i - 1] != A[i]:
                    i += 1
                else:
                    t = A.count(A[i])
                    if t < 3:
                        i += 1
                    else: # A[i] de geshu >= 3
                        i += 1
                        while t - 2:
                            jnum = A[j]
                            if A[i: ].count(jnum) > 2:
                                j = A.index(jnum) + 1

                            if j <= i:
                                A[: i + 1] = sorted(A[: i + 1])
                                print A
                                return i

                            A[i] = jnum
                            j -= 1
                            i += 1
                            t -= 1
            A[: i] = sorted(A[: i])
            print A
            return i

    def removeDuplicates2(self, A):
        if not A:
            return len(A)
        else:
            for ele in A:
                while A.count(ele) - 2 > 0:
                    A.remove(ele)
            return len(A)
if __name__ == "__main__":

    A1 = []
    A2 = [1]
    A3 = [1, 1, 1]
    A7 = [1, 1, 1, 1]
    A6 = [1, 1, 1, 1, 3, 3]
    A4 = [1, 1, 1, 2, 2, 2]
    A5 = [0, 1, 2, 2, 2, 2, 3, 4, 5, 5, 5, 6]

    s = Solution()
    print "A1\t", s.removeDuplicates(A1)
    print "A2\t", s.removeDuplicates(A2)
    print "A3\t", s.removeDuplicates(A3)
    print "A4\t", s.removeDuplicates(A4)
    print "A5\t", s.removeDuplicates(A5)
    print "A6\t", s.removeDuplicates(A6)
    print "A7\t", s.removeDuplicates(A7)







