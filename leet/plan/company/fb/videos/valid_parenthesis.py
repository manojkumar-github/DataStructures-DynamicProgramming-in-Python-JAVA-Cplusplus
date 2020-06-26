"""
Given a string containing just the characters
'(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
"""


def valid_parenthesis(ip_string):

    stack = []
    # closing brackets to opening brackets map
    mapping = {")": "(", "}": "{", "]": "["}

    for char in ip_string:
        if char in mapping:
            top_element = stack.pop() if stack else "#"
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)

    return len(stack) == 0


print(valid_parenthesis("()"))
print(valid_parenthesis("()[]{}"))
print(valid_parenthesis("(]"))
print(valid_parenthesis("([)]"))
print(valid_parenthesis("{[]}"))
