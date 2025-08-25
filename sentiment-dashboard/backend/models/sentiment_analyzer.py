from typing import Tuple

class SentimentAnalyzer:
    POSITIVE_WORDS = {"good", "great", "excellent", "amazing", "love", "like", "happy", "wonderful", "positive"}
    NEGATIVE_WORDS = {"bad", "terrible", "awful", "hate", "dislike", "sad", "horrible", "negative"}

    def analyze(self, text: str) -> Tuple[float, str]:
        if not text:
            return 0.0, "neutral"
        words = [w.strip(".,!?;:").lower() for w in text.split()]
        pos = sum(1 for w in words if w in self.POSITIVE_WORDS)
        neg = sum(1 for w in words if w in self.NEGATIVE_WORDS)
        total = pos + neg
        score = 0.0 if total == 0 else (pos - neg) / total
        label = "positive" if score > 0.2 else "negative" if score < -0.2 else "neutral"
        return float(score), label