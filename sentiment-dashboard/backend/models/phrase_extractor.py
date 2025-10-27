from typing import List
import re

class PhraseExtractor:
    WORD_RE = re.compile(r"[A-Za-z][A-Za-z\-']+")

    def extract(self, text: str) -> List[str]:
        if not text:
            return []
        words = [w.lower() for w in self.WORD_RE.findall(text)]
        # naive: return unique bigrams and any capitalized tokens as phrases
        bigrams = {f"{a} {b}" for a, b in zip(words, words[1:]) if a not in {"and", "the", "a", "an"} and b not in {"and", "the", "a", "an"}}
        phrases = list(bigrams)
        phrases.sort()
        return phrases[:10]