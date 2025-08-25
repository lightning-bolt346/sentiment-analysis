class PhraseExtractor:
    """Naive key phrase extractor placeholder."""

    def extract(self, text: str) -> list[str]:
        tokens = [t.strip(".,!?;:") for t in text.split()]
        phrases = [t for t in tokens if len(t) > 4]
        # Deduplicate while preserving order
        seen: set[str] = set()
        unique_phrases: list[str] = []
        for p in phrases:
            if p not in seen:
                seen.add(p)
                unique_phrases.append(p)
        return unique_phrases[:10]