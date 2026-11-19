class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        letters = {}
        for i in range(len(order)):
            letters[order[i]] = i

        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]

            for i in range(min(len(word1), len(word2))):
                if letters[word2[i]] < letters[word1[i]]:
                    return False
                elif letters[word1[i]] < letters[word2[i]]:
                    break
            else:
                if len(word2) < len(word1):
                    return False
        return True