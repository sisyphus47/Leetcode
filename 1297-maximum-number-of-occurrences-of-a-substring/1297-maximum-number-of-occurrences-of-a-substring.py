from collections import defaultdict, Counter

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        counts = defaultdict(int)
        char_count = Counter()
        unique = 0
        left = 0

        for right in range(len(s)):
            char = s[right]
            char_count[char] += 1
            if char_count[char] == 1:
                unique += 1

            # Maintain window of size minSize
            if right - left + 1 > minSize:
                left_char = s[left]
                char_count[left_char] -= 1
                if char_count[left_char] == 0:
                    unique -= 1
                left += 1

            if right - left + 1 == minSize and unique <= maxLetters:
                substring = s[left:right + 1]
                counts[substring] += 1

        return max(counts.values(), default=0)
