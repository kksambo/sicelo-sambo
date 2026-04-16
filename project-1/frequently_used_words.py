"""
This module tracks the most frequently used words using a Top-N approach.
"""

from collections import defaultdict
import heapq
import re
import time
from typing import DefaultDict, List, Tuple


class WordFrequencyTracker:
    """
    Tracks word frequency and returns top N most frequent words.
    """

    def __init__(self, n: int = 10) -> None:
        self.n: int = n
        self.freq: DefaultDict[str, int] = defaultdict(int)

    def process_word(self, word: str) -> List[Tuple[str, int]]:
        """
        Process a single word and update top-N tracking.
        Returns current top N words.
        """
        word = word.lower()
        self.freq[word] += 1
        return self.get_top_n()

    def get_top_n(self) -> List[Tuple[str, int]]:
        """Return top N most frequent words as list of tuples (word, count)."""
        return heapq.nlargest(self.n, self.freq.items(), key=lambda x: x[1])


# Demo usage
if __name__ == "__main__":
    TEXT: str = input("Please enter a text to process: ")

    tracker: WordFrequencyTracker = WordFrequencyTracker(n=5)

    # Extract words only letters only
    words: List[str] = re.findall(r"[a-zA-Z]+", TEXT)

    for w in words:
        result: List[Tuple[str, int]] = tracker.process_word(w)
        print(result)
        time.sleep(1)