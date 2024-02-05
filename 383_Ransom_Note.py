# n = len(ransomNote), m = len(magazine)
# time: O(n+m)
# space: O(n+m)

from typing import List

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        def countChar(input_str):
            char_dict = {}
            for char in input_str:
                if char not in char_dict:
                    char_dict[char] = 1
                else:
                    char_dict[char] += 1
            return char_dict

        ransomNoteDict = countChar(ransomNote)
        magazineDict = countChar(magazine)

        for key in ransomNoteDict.keys():
            if key not in magazineDict.keys():
                return False
            if magazineDict[key] < ransomNoteDict[key]:
                return False

        return True
