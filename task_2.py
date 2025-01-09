from trie import Trie

class LongestCommonWord(Trie):

    def find_longest_common_word(self, strings) -> str:
        # Перевірка на коректність вхідних даних
        if not isinstance(strings, list) or not all(isinstance(s, str) for s in strings):
            raise ValueError("Input must be a list of strings")

        # Якщо масив порожній, повертаємо пустий рядок
        if not strings:
            return ""

        # Знаходимо слово з мінімальною довжиною для оптимізації
        shortest = min(strings, key=len)

        # Виконуємо перевірку кожного символу в мінімальному слові
        for i in range(len(shortest)):
            char = shortest[i]
            for word in strings:
                if word[i] != char:
                    return shortest[:i]

        # Якщо всі символи мінімального слова збігаються, це і є спільний префікс
        return shortest

if __name__ == "__main__":
    # Тести
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    assert trie.find_longest_common_word(strings) == "fl"

    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    assert trie.find_longest_common_word(strings) == "inters"

    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    assert trie.find_longest_common_word(strings) == ""

    print("All tests passed!")
