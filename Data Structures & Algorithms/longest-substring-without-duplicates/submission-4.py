class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        maxi = 0
        l = 0
        char_idx_map = {}

        for idx, ch in enumerate(s):
            if ch in char_idx_map and l <= char_idx_map[ch]:
                l = char_idx_map[ch] + 1
            char_idx_map[ch] = idx
            maxi = max(maxi, idx - l + 1)
        
        return maxi

















        maxi = 0
        l = 0
        char_index_map = {}  # Stores character -> its last seen index

        for r, ch in enumerate(s):
            # If we've seen the character AND it's inside our current window
            if ch in char_index_map and char_index_map[ch] >= l:
                # Fast-forward 'l' to the index right AFTER the last occurrence
                l = char_index_map[ch] + 1
            
            # Update or insert the character's newest position
            char_index_map[ch] = r
            
            # Calculate the window size
            maxi = max(maxi, r - l + 1)
            
        return maxi
