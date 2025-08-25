from fastapi import APIRouter, Depends
from .schemas import AnalyzeRequest, AnalyzeResponse, SentimentResult
from models.sentiment_analyzer import SentimentAnalyzer
from models.phrase_extractor import PhraseExtractor

router = APIRouter()


def get_analyzer() -> SentimentAnalyzer:
    return SentimentAnalyzer()


def get_phrase_extractor() -> PhraseExtractor:
    return PhraseExtractor()


@router.post("/analyze", response_model=AnalyzeResponse)
async def analyze(
    payload: AnalyzeRequest,
    analyzer: SentimentAnalyzer = Depends(get_analyzer),
    extractor: PhraseExtractor = Depends(get_phrase_extractor),
):
    score, label = analyzer.analyze(payload.text)
    phrases = extractor.extract(payload.text)
    return AnalyzeResponse(sentiment=SentimentResult(score=score, label=label), keyPhrases=phrases)