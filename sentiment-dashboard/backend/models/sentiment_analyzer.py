class SentimentAnalyzer:
    """Very simple placeholder sentiment analyzer.

    Replace with a real model or pipeline in the future.
    """

    def predict(self, text: str) -> tuple[str, float]:
        text_lower = text.lower()
        if any(word in text_lower for word in ["love", "great", "awesome", "good", "happy"]):
            return ("positive", 0.9)
        if any(word in text_lower for word in ["hate", "bad", "terrible", "awful", "sad"]):
            return ("negative", 0.9)
        return ("neutral", 0.5)