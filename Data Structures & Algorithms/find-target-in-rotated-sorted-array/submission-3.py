class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, h = 0, len(nums) - 1
        
        while l <= h:
            mid = (l + h) // 2
            
            # Found the target instantly
            if nums[mid] == target:
                return mid
            
            # Step 1: Check if the left half is perfectly sorted
            if nums[l] <= nums[mid]:
                # Step 2: Check if target sits within this sorted left half
                if nums[l] <= target < nums[mid]:
                    h = mid - 1  # Search left
                else:
                    l = mid + 1  # Search right
                    
            # Step 3: Otherwise, the right half must be perfectly sorted
            else:
                # Step 4: Check if target sits within this sorted right half
                if nums[mid] < target <= nums[h]:
                    l = mid + 1  # Search right
                else:
                    h = mid - 1  # Search left
                    
        return -1  # Target was not found