class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        ans = []

        def isPallindrome(word):
            l, h = 0, len(word)-1
            while l<=h:
                if word[l] != word[h]:
                    return False
                l += 1
                h -= 1
            return True
        
        def helper(string, curr_list):

            if string == "":
                ans.append(curr_list[:])

            for partition in range(1, len(string)+1):
                curr_str = string[:partition]
                if isPallindrome(curr_str):
                    curr_list.append(curr_str)
                    helper(string[partition:], curr_list)
                    curr_list.pop()

            
        helper(s, [])
        return ans
