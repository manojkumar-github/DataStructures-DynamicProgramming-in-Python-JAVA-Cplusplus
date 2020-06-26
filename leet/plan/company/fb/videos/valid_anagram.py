"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
"""

def is_anagram(s, t):

    len_s = len(s)
    len_t = len(t)

    if len(s) != len(t):
        return False

    return sorted(s)==sorted(t)

def is_anagram_dict(s, t):

    len_s = len(s)
    len_t = len(t)

    if len(s) != len(t):
        return False

    adict = {}
    for i in range(len_s):
        if s[i] in adict:
            adict[s[i]] += 1
        else:
            adict[s[i]] = 1

        if t[i] in adict:
            adict[t[i]] -= 1
        else:
            adict[t[i]] = -1
    if sum(adict.values()) == 0:
        return True
    else:
        return False


print(is_anagram("anagram", "nagaram"))

print(is_anagram_dict("anagram", "nagaram"))

