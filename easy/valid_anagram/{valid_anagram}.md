# {valid_anagram} (Easy)

## Problem Description

Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

**Example:**

Input: s = "racecar", t = "carrace"
Output: true

Input: s = "jar", t = "jam"
Output: false

--- 
## Approaches
### Approach 1: Sorting 
```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
	if len(s) != len(t):
	    return False
	return sorted(s) == sorted(t)
```

- **Time Complexity:** O(nlogn)
- **Space Complexity:** O(1)
- **Pros:** Simple and intuitive
- **Cons:** Overhead
---

### Approach 2: HashMap (Counter)
```python
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t:str) -> bool:
	if lens(s) != len(t):
	    return False
	return Counter(s) == Counter(t)
```
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
- **Pros:** Linear time, clean and readable
- **Cons:** Slight overhead from Counter object creation
---

## Why I Chose This Approach 

I chose the Counter approach because it runs in O(n) time, which is more efficient than sorting. The early length check also filters out abvious non-anagrams before any character counting is needed.

---

## Walkthrough (Example) 

s = "racecar", t = "carrace"
1. len("racecar") == len("carrace") → pass
2. Counter("racecar") → {'r': 2, 'a': 2, 'c': 2, 'e': 1}
3. Counter("carrace") → {'r': 2, 'a': 2, 'c': 2, 'e': 1}
4. Both Counters are equal →return True

---

## Key Insights

1. An anagram is essentially about character frequency, and Counter captures this directly
2. Checking the length upfront eliminates obvious mismatches early
3. Since input is limited to lowercase letters, space is bounded at 26 entries → O(1)

