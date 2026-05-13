from collections import Counter

class Solution:
    def findSubstring(self, s, words):

        if not s or not words:
            return []

        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count

        target = Counter(words)
        result = []

        for i in range(len(s) - total_len + 1):

            seen = {}

            for j in range(word_count):

                start = i + j * word_len
                word = s[start:start + word_len]

                if word not in target:
                    break

                seen[word] = seen.get(word, 0) + 1

                if seen[word] > target[word]:
                    break

            else:
                result.append(i)

        return result