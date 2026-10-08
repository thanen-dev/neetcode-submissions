class Solution:
    def isPalindrome(self, s: str) -> bool:
        storage = ''
        for i in s:
            if i.isalnum():
                storage += i.lower()
        if storage == storage[::-1]:
            return True
        else:
            return False
