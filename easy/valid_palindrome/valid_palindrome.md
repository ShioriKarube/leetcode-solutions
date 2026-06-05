# Valid Palindrome (Easy)

## Problem Description

Given a string s, return true if it's a palindrome, otherwise return false.
A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

**Example:**

Input: s = "Was it a car or a cat I saw?"

Output: true

--- 
## Approach
### Approach: Two Pointers 
```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1

        return True
```
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
- **Pros:** Single pass, no extra data structures, efficient
- **Cons:** Requires careful pointer management
---

## Why I Chose This Approach 

The two pointer approach is optimal for this problem because it allows us to compare characters from both ends simultaneously while skipping non-alphanumeric characterse in a single pass. This avoids the overhead of creating a filtered string and uses constant extra space.

---

## Walkthrough (Example) 

Input: s = "Was it a car or a cat I saw?"
1. Initialize l=0, r = 27
2. Skip non-alphanumeric characters from both ends
3. After lowercasing, compare 'w' with 'w' → match, move pointer inward
4. Continue comparing: 'a' with 'a', 's' with 's', etc
5. All comparison match, return True

---

## Key Insights
1. Use built-in method .isalnum() to check if a character is alphanumeric-this handles both letter checking and digit checking in one call
2. The two-pointer approach automatically handles non-alphanumeric characters by skipping over them rather than filtering them out
3. This is a single-pass alogrithm: we iterate through the string at most once, making it more efficient than preprocessing approaches
