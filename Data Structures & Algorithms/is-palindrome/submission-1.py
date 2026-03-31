class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        given string s, return true if its a palindrome, otherwise false
        read same forward and backward, case insensitive and ignores non alphanumeric chars

        first thing, get rid of spaces, numbers, punctuation, capitals
        then two pointers, one on left one on right
        check if same then increment each
        terminate when false or when right > left
        """

        l, r = 0, len(s) - 1

        while l < r:
            while l<r and not s[l].isalnum():
                l += 1
            while l<r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1

        return True

            