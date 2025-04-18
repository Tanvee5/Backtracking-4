# Problem 2 : Brace Expansion
# Time Complexity : O(n*k^n) where n is the number of character group and k is the average number of character in a group
# Space Complexity : O(n*k^n) where n is the number of character group and k is the average number of character in a group
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this :
'''
None
'''

# Your code here along with comments explaining your approach
from typing import List
class Solution:
    def expand(self, s: str) -> List[str]:
        # defin result array that store the list of the all the words that can formed using s string
        result = []
        # define groups array that will store all the group of the character
        groups = []
        # variable i that will be used as pointer for traversing the s string and set to 0
        i = 0
        
        # travers through s string
        while i < len(s):
            # define group that will store current group character 
            group = []
            # if the current character is '{' then store all the character enclosed in the '{}' in the group list
            if s[i] == '{':
                # increment the i pointer to get the next character
                i += 1
                # loop till '}' is encountered
                while s[i] != '}':
                    # check if the character is not ',' then append the character in the group list
                    if s[i] != ',':
                        group.append(s[i])
                    # increment the i pointer
                    i += 1
            # else if is alphabet then append to the group list
            else:
                group.append(s[i])
            # increment the i pointer
            i += 1
            # sort the group list to get the words in lexicographical order
            group.sort()
            # append the current group in the groups list
            groups.append(group)
        
        # call backtrack function with paramter groups 0, [](current path) and result
        self.backtrack(groups, 0, [], result)
        # return result
        return result
    
    # backtrack function
    def backtrack(self, groups: List[List[str]], idx: int, path: List[str], result: List[str]) -> None:
        # base case when the idx is equal to the length of the groups list
        if idx == len(groups):
            # if it is equal then append the path to the result and return
            result.append(''.join(path))
            return
        
        # logic
        # loop through each character in the idx group in the groups list
        for c in groups[idx]:
            # action
            # append the character to the current path
            path.append(c)
            # recurse
            # call backtrack fucntion with paramter groups, idx+1, path and result
            self.backtrack(groups, idx+1, path, result)
            # backtrack
            # remove the last character from the current path to explore other options
            path.pop()
