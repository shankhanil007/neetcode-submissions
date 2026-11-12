class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        hmapT = {}
        for ch in t:
            hmapT[ch] = hmapT.get(ch, 0) + 1
        
        have = 0
        required = len(t)
        hmapS = {}
        l, r = 0, 0
        min_length = float('inf')
        ans = ""

        while r < len(s):
            ch = s[r]
            hmapS[ch] = hmapS.get(ch, 0) + 1
            if ch in hmapT and hmapS[ch] <= hmapT[ch]: #### IMMMPP when to increase HAVE
                have += 1
            
            while have == required:
                window = r - l + 1
                if window < min_length:
                    min_length = window
                    ans = s[l: l + window]
                char_to_delete = s[l]
                hmapS[char_to_delete] -= 1
                if char_to_delete in hmapT and hmapS[char_to_delete] < hmapT[char_to_delete]:  #### IMMMPP when to reduce HAVE and it should be after decreasing
                    have -= 1
                l += 1

            r += 1
        return ans