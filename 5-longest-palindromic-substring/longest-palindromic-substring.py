class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        start = 0
        end = 0

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            
            return left + 1, right - 1

        for i in range (len(s)):
            odd_start, odd_end = expand(i, i)
            odd_length = (odd_end - odd_start + 1)
            best_length = (end - start + 1)

            if odd_length > best_length:
                start = odd_start
                end = odd_end

            even_start, even_end = expand(i, i + 1)
            even_length = (even_end - even_start + 1)
            
            best_length = (end - start + 1)

            if even_length > best_length:
                start = even_start
                end = even_end

        return s[start: end + 1]