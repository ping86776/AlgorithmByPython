class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        a = []
        for i in range(0, len(A)):
            a.append(A[i][::-1])
            for j in range(0, len(a[i])):
                a[i][j] ^= 1
        return a

if __name__ == '__main__':
    arr = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
    print(Solution().flipAndInvertImage(arr))