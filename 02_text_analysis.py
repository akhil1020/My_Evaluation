# 2. Text Analysis with Constraints
# Given a large paragraph of text, write a Python program that:
# • Counts the frequency of each word, ignoring common stop words (the, is, at, on, in, and,
# etc.).
# • Allows efficient querying, for example:
# • "Return the top 3 most frequent words starting with the prefix 'th'."
# • Optimize for performance.

#-------------solution--------->
import re
from collections import defaultdict, Counter

# Define a basic set of common stop words
STOP_WORDS = set([
    'the', 'is', 'at', 'on', 'in', 'and', 'a', 'an', 'of', 'to', 'with', 'that', 'this', 'for', 'from'
])

# Trie node structure
class TrieNode:
    def __init__(self):
        self.children = {}
        self.words = set()

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            node.words.add(word)
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.words.add(word)

    def get_words_with_prefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return set()
            node = node.children[char]
        return node.words

# Main analyzer class
class TextAnalyzer:
    def __init__(self, text):
        self.word_freq = Counter()
        self.trie = Trie()
        self.process_text(text)

    def process_text(self, text):
        words = re.findall(r'\b[a-z]+\b', text.lower())
        filtered_words = [word for word in words if word not in STOP_WORDS]
        self.word_freq = Counter(filtered_words)
        for word in self.word_freq:
            self.trie.insert(word)

    def query_top_n_with_prefix(self, prefix, n):
        words = self.trie.get_words_with_prefix(prefix.lower())
        return sorted(words, key=lambda w: self.word_freq[w], reverse=True)[:n]

# Example Usage
paragraph = """
The thunder rolled in the distance as the thoughtful thinker sat on the porch.
There was a thrill in the air, thick with anticipation and the smell of rain.
"""

analyzer = TextAnalyzer(paragraph)
print(analyzer.query_top_n_with_prefix("th", 3))  # Top 3 words starting with 'th'
