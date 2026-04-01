class Solution:
    def isValid(self, s: str) -> bool:
        """
        string s and contains different types of brackets

        s is valid iff 
        1. every open bracket is closed by the same type of close bracket
        2. open brackets are closed in the correct order
        3. every close bracket has a corresponding open bracket of the same type

        return true if s is a valid string, false otherwise

        we should use a stack here

        also a hashmap i believe that maps closing braces to open braces 

        so we push all open braces onto the stack, whenever we approach a closing brace, we see the brace it maps and do a peek to the top of the stack
        if the top of the stack is not that, then its false

        lets say we have s = "([{}])"
        stack = [([]
        so we push on all openings and pop when closing and its correct brace, it works
        """

        stack = []
        bracket_map = {
            "}": "{",
            "]": "[",
            ")": "(",
        }

        for bracket in s:
            if bracket not in bracket_map:
                stack.append(bracket)

            elif not stack:
                return False
            
            elif stack[-1] == bracket_map[bracket]:
                stack.pop()
            
            else:
                return False

        return len(stack) == 0
            