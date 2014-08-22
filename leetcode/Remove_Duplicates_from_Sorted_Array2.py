class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A:
            return len(A)
        else:
            for ele in A:
                while A.count(ele) - 2 > 0:
                    A.remove(ele)
        
            return len(A)

if __name__ == "__main__":
    A = [-1, 0, 0, 0, 0, 3, 3]
    s = Solution()
    s.removeDuplicates(A)
    print len(A), A
