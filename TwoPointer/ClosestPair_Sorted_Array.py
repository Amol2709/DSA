class Solution:
    def solve(self, A, B, C):
        i = 0 # on start of A
        j = len(B) - 1
        ans = [i, j]
        min_diff = 2e9
        while i < len(A) and j >= 0:
            two_sum = A[i] + B[j]
            diff = abs(two_sum - C)
            if diff < min_diff:
                ans = [i, j]
                min_diff = diff
            elif diff == min_diff:
                # if current i is less than prev i
                if i < ans[0]:
                    ans = [i, j]
                # if current i is same as prev u but smaller j is found then
                # also update ans
                elif ans[0] == i and j < ans[1]:
                    ans = [i, j]
            
            if two_sum >= C:
                j -= 1
            else: 
                i += 1
        return [A[ans[0]], B[ans[1]]]