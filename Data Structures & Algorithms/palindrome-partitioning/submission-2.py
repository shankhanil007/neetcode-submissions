class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        ans = []

        def isPallindrome(string):
            l, h = 0, len(string)-1
            while l<=h:
                if string[l] != string[h]:
                    return False
                l+=1
                h-=1
            return True
            
        def helper(string, curr):

            if not string:
                ans.append(curr[:])
                return

            for i in range(1, len(string)+1):
                curr_string = string[:i]
                if isPallindrome(curr_string):
                    curr.append(curr_string)
                    helper(string[i:], curr)
                    curr.pop()
            
        helper(s, [])
        return ans
