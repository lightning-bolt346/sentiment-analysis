from fastapi import APIRouter
from pydantic import BaseModel
from ..models.sentiment_analyzer import SentimentAnalyzer
from ..models.phrase_extractor import PhraseExtractor

router = APIRouter()

class AnalyzeRequest(BaseModel):
    text: str

class AnalyzeResponse(BaseModel):
    label: str
    score: float
    key_phrases: list[str]

_analyzer = SentimentAnalyzer()
_extractor = PhraseExtractor()

@router.post("/analyze", response_model=AnalyzeResponse)
async def analyze(request: AnalyzeRequest) -> AnalyzeResponse:
    label, score = _analyzer.predict(request.text)
    key_phrases = _extractor.extract(request.text)
    return AnalyzeResponse(label=label, score=score, key_phrases=key_phrases)