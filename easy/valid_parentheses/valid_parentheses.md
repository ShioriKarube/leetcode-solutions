# Valid Parentheses (Easy)

## Problem Description

Given a string containing '(', ')', '{', '}', '[' and ']', determine whether the brackets are properly matched and ordered. 

**Example:**

- Input: s = "([{}])", Output: true
- Input: s = "[(])", Output: false

--- 
## Approach
### Approach: Stack
```python
class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        stack = []
        for char in s:
            if char in brackets:
                if not stack or stack.pop() != brackets[char]:
                    return False
            else:
                stack.append(char)

        return not stack
```
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)
- **Pros:** Simple and clean; handles all three bracket types with single dict
- **Cons:** Requires O(n) extra space for the stack
---

## Why I Chose This Approach 

Brackets follow a LIFO (Last In, First Out) rule-the most recently opened bracket must be closed first. A stack models this naturally. Each opening bracket is pushed onto the stack, and each closing bracket is checked against the top of the stack. If they match, pop and continue; if not, return false immediately

---

## Walkthrough (Example) 

Input: 's = "([{}])"'

**Step 1:** '(' →opening bracket, push to stack
- Stack: '['(']'

**Step 2:** '[' → opening bracket, push to stack
- Stack: '['(', '[']'

**Step 3:** '{' → opening bracket, push to stack
- Stack: '['(', '[', '{']'

**Step 4:** '}' → closing bracket, pop '{' from stack → matches '{'
- Stack: '['(', '[']'

**Step 5:** ']' →closing bracket, pop '[' from stack → matches '['
- Stack: '['(']'

**Step 6:** ')' →closing bracket, pop '(' from stack → matches '('
- Stack: '[]'

Stack is empty → return 'True'

---

## Key Insights
1. Brackets are LIFO - the last opened must be the first closed. A stack captures this directly.
2. Returning 'not stack' at the end catches unmatched opening brackets.
3. Checking 'not stack' before 'stack.pop()' prevents an IndexError when a closing bracket appears with nothing on the stack.
