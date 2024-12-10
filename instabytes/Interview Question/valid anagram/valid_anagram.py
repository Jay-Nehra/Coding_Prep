"""
Given two strings s and t, return true if t is an 
anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:
1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.


Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""

from collections import Counter, defaultdict
from loguru import logger


def valid_anagram_counter(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)

def valid_anagram_sort(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)

def valid_anagram_dict(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    char_count = defaultdict(int)

    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    for char in t:
        if char not in char_count or char_count[char] == 0:
            return False
        char_count[char] -= 1

    return True if all(count == 0 for count in char_count.values()) else False

def main() -> None:
    s = input("Enter the first string: ")
    t = input("Enter the second string: ")
    logger.info(f"Input strings: s={s}, t={t}")
    result = valid_anagram_counter(s, t)
    logger.info(f"Is anagram: {result}")

if __name__ == "__main__":
    main()  
